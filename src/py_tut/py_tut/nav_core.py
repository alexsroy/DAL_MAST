"""Navigation core: which way to point the boat to reach the next waypoint.

Plain Python with no ROS imports, so it can be unit tested anywhere and run
inside a simulator. navigation.py wraps it in a ROS node.

Frames and units
----------------
World frame: ENU, the Xsens MTi's convention. x is east, y is north, in
metres from a local projection around the previous waypoint. Headings and
bearings are degrees counter-clockwise from east, in [0, 360).

The windvane reports the apparent wind angle relative to the bow, clockwise
(NMEA MWV with reference R). wind_from_world() turns it into the world
direction the wind is coming FROM, which is what the tacking logic needs.

The strategy
------------
The boat follows the leg from the previous waypoint (A) to the next one (B):

* Reaching: when B itself can be sailed to, aim at a point on the leg a
  little ahead of the boat (line-of-sight guidance). That steers back onto
  the leg after any drift and ends exactly at B. If the line asks the boat
  to point higher than it can, it sails close-hauled instead.
* Beating: when B is within the no-go zone, sail close-hauled on one tack.
  Tack when the boat reaches the edge of the corridor around the leg, or
  when B can be fetched on the other tack (the layline), but never sooner
  than min_tack_interval_s after the last tack.
* Stalled tacks: whenever the heading asked for has the wind on the other
  bow (a tack, from either mode), the boat has tack_timeout_s to get the
  wind tack_done_deg onto that bow. If it is still less than half that
  onto it, it has stalled head to wind (a boat that isn't moving can't be
  turned by its rudder): it sails close-hauled on whichever bow the wind is
  on to build speed, and isn't asked to tack again for tack_retry_s. The vane
  decides which bow the wind is on, as it does for controls.py, which
  feathers the wing while asked to tack, so the two always agree.
* Beating starts on the tack on the side the boat was last steered to, so
  a mark near the edge of the no-go zone, whose bearing GPS noise moves by
  several degrees, can't flip the target back and forth across the wind.

Hysteresis on the no-go limit stops the boat flipping between reaching and
beating when the course sits right at the edge of the no-go zone.
"""

import math
from dataclasses import dataclass, field

EARTH_RADIUS_M = 6_371_008.8


def wrap180(deg):
    """An angle in degrees, wrapped into [-180, 180)."""
    return (deg + 180.0) % 360.0 - 180.0


def to_local(lat, lon, lat0, lon0):
    """(x east, y north) in metres from (lat0, lon0); accurate to a few cm over a lake."""
    k = math.radians(1.0) * EARTH_RADIUS_M
    return ((lon - lon0) * k * math.cos(math.radians(lat0)), (lat - lat0) * k)


def to_latlon(x, y, lat0, lon0):
    """The inverse of to_local()."""
    k = math.radians(1.0) * EARTH_RADIUS_M
    return (lat0 + y / k, lon0 + x / (k * math.cos(math.radians(lat0))))


def bearing(frm, to):
    """ENU direction in degrees from point frm to point to, in [0, 360)."""
    return math.degrees(math.atan2(to[1] - frm[1], to[0] - frm[0])) % 360.0


def wind_from_world(heading_enu, vane_cw):
    """The world direction (ENU degrees) the wind comes from.

    heading_enu: the boat's heading, ENU degrees.
    vane_cw: the windvane's apparent wind angle, clockwise from the bow.

    This is the apparent wind turned into the world frame. At Windbound's
    speeds it is within a few degrees of the true wind on a reach and within
    about 15 degrees close-hauled; once the firmware forwards wind speed, a
    true-wind correction with the boat's velocity belongs here.
    """
    return (heading_enu - vane_cw) % 360.0


class AngleFilter:
    """A low-pass filter for an angle: an exponential moving average of its
    unit vector, so it averages correctly across 0/360."""

    def __init__(self, tau_s):
        self.tau_s = tau_s
        self.x = self.y = None
        self.t = None

    def update(self, deg, now_s):
        c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        if self.x is None:
            self.x, self.y = c, s
        else:
            k = 1.0 - math.exp(-max(now_s - self.t, 0.0) / self.tau_s)
            self.x += (c - self.x) * k
            self.y += (s - self.y) * k
        self.t = now_s
        return self.value

    @property
    def value(self):
        return None if self.x is None else math.degrees(math.atan2(self.y, self.x)) % 360.0


@dataclass
class NavConfig:
    tack_angle_deg: float = 45.0         # how far off the wind to sail when beating
    no_go_deg: float = 45.0              # courses closer to the wind than this can't be sailed
    hysteresis_deg: float = 7.0          # stop beating only once the course is this far clear
    corridor_half_width_m: float = 30.0  # tack before drifting further than this off the leg
    lookahead_m: float = 25.0            # line-of-sight distance along the leg
    min_tack_interval_s: float = 12.0    # let a tack finish and the boat build speed
    layline_overstand_deg: float = 3.0   # tack a little past the layline so B is fetched
    tack_done_deg: float = 20.0          # a tack is through once the wind is this far onto the new bow
    tack_timeout_s: float = 20.0         # a tack not half through by now has stalled: give it up
    tack_retry_s: float = 30.0           # after giving up, build speed this long before trying again


@dataclass
class NavState:
    beating: bool = False
    tack: int = 0                        # +1 starboard tack, -1 port tack, 0 not beating
    last_tack_s: float = -math.inf
    tacks: int = 0
    tacking_since: float | None = None   # since when the boat has been asked to tack
    no_tack_before_s: float = -math.inf  # after a stalled tack, build speed until then
    hold_side: int = 0                   # and stay close-hauled on this bow (+1 starboard)
    failed_tacks: int = 0
    last_steer: float | None = None


@dataclass
class Guidance:
    heading: float          # the heading to steer, ENU degrees in [0, 360)
    mode: str               # "reaching" or "beating"
    tack: int               # +1 starboard, -1 port, 0 reaching
    leg_bearing: float      # A to B, ENU degrees
    cross_track_m: float    # positive when the boat is left of the leg
    along_track_m: float    # distance from A along the leg
    distance_m: float       # straight to B
    reason: str = ""        # why the boat tacked, on the tick it did
    extra: dict = field(default_factory=dict)


def tack_heading(wind_from, tack, cfg):
    """Close-hauled heading on a tack. Starboard tack (+1) has the wind on the
    starboard bow, so the heading is counter-clockwise of the wind."""
    return (wind_from + tack * cfg.tack_angle_deg) % 360.0


def guide(cfg, st, now_s, boat, heading, wind_from, a, b, vane_cw=None):
    """The heading to steer this tick.

    cfg, st: NavConfig and the NavState carried between ticks.
    boat, a, b: (x, y) metres of the boat, the previous and the next waypoint.
    heading: the boat's heading; wind_from: where the wind comes from (ENU).
    vane_cw: the windvane's latest reading, clockwise from the bow; without
    it, the bow the wind is on comes from heading and wind_from.
    """
    g = course(cfg, st, now_s, boat, heading, wind_from, a, b)
    vane = wrap180(heading - wind_from if vane_cw is None else vane_cw)
    if now_s < st.no_tack_before_s:
        if asked_to_tack(vane, wrap180(vane + g.heading - heading), cfg.tack_done_deg):
            g.heading = tack_heading(wind_from, st.hold_side, cfg)
            if g.mode == "beating":
                st.tack = g.tack = st.hold_side

    there = wrap180(vane + g.heading - heading)   # where the vane will read on the new heading
    if not asked_to_tack(vane, there, cfg.tack_done_deg):
        st.tacking_since = None
    elif st.tacking_since is None:
        st.tacking_since = now_s
    elif (now_s - st.tacking_since > cfg.tack_timeout_s
          and vane * math.copysign(1.0, there) < cfg.tack_done_deg / 2):
        st.failed_tacks += 1
        st.hold_side = 1 if vane >= 0 else -1         # the bow the wind is still on
        st.no_tack_before_s = now_s + cfg.tack_retry_s
        st.tacking_since = None
        g.heading = tack_heading(wind_from, st.hold_side, cfg)
        g.reason = "tack stalled"
        if g.mode == "beating":
            st.tack = g.tack = st.hold_side
    st.last_steer = g.heading
    return g


def asked_to_tack(vane, there, done_deg):
    """True while the heading asked for needs the wind on the other bow and
    it isn't yet done_deg onto that bow. vane, there: where the vane reads
    now and would read on that heading, clockwise from the bow in
    [-180, 180). A gybe (the wind abaft the beam) isn't a tack."""
    return abs(vane) < 90 and abs(there) < 90 and vane * math.copysign(1.0, there) < done_deg


def course(cfg, st, now_s, boat, heading, wind_from, a, b):
    """guide() without the watch for stalled tacks."""
    lx, ly = b[0] - a[0], b[1] - a[1]
    length = math.hypot(lx, ly)
    if length < 1e-6:                    # no leg (one waypoint): head straight for it
        ux, uy = (b[0] - boat[0], b[1] - boat[1])
        norm = math.hypot(ux, uy) or 1.0
        ux, uy, length, a = ux / norm, uy / norm, norm, boat
    else:
        ux, uy = lx / length, ly / length
    rx, ry = boat[0] - a[0], boat[1] - a[1]
    along = rx * ux + ry * uy
    cross = ux * ry - uy * rx            # z of (leg x boat): positive left of the leg
    distance = math.hypot(b[0] - boat[0], b[1] - boat[1])

    # Line of sight: a point on the leg ahead of the boat, never past B.
    if distance <= cfg.lookahead_m:
        aim = b
    else:
        ahead = min(max(along, 0.0) + cfg.lookahead_m, length)
        aim = (a[0] + ux * ahead, a[1] + uy * ahead)
    want = bearing(boat, aim)
    leg_bearing = math.degrees(math.atan2(uy, ux)) % 360.0

    def result(steer, mode, reason=""):
        return Guidance(steer % 360.0, mode, st.tack, leg_bearing, cross, along, distance, reason)

    # Beat or reach is decided by B itself: line of sight would otherwise drag
    # the boat back onto the leg on a reach while B is still upwind.
    off_b = wrap180(bearing(boat, b) - wind_from)
    limit = cfg.no_go_deg + (cfg.hysteresis_deg if st.beating else 0.0)
    if abs(off_b) >= limit:
        st.beating, st.tack = False, 0
        off_want = wrap180(want - wind_from)
        if abs(off_want) < cfg.no_go_deg:   # the line asks for more height than the boat can point
            want = wind_from + math.copysign(cfg.tack_angle_deg, off_want or off_b)
        return result(want, "reaching")

    if not st.beating:
        # Start on the tack nearest where the boat was last steered (or points).
        st.beating = True
        towards = heading if st.last_steer is None else st.last_steer
        st.tack = min((1, -1), key=lambda t: abs(wrap180(tack_heading(wind_from, t, cfg) - towards)))
        return result(tack_heading(wind_from, st.tack, cfg), "beating", "started beating")

    reason = ""
    if (st.tacking_since is None and now_s >= st.no_tack_before_s
            and now_s - st.last_tack_s >= cfg.min_tack_interval_s):
        current = tack_heading(wind_from, st.tack, cfg)
        # Which way the current tack carries the boat across the leg (+ is to the left).
        drift = ux * math.sin(math.radians(current)) - uy * math.cos(math.radians(current))
        to_b = wrap180(bearing(boat, b) - wind_from)
        fetch = cfg.tack_angle_deg + cfg.layline_overstand_deg
        if abs(cross) >= cfg.corridor_half_width_m and drift * cross > 0:
            reason = "corridor edge"
        elif st.tack > 0 and to_b <= -fetch or st.tack < 0 and to_b >= fetch:
            reason = "layline"
        if reason:
            st.tack = -st.tack
            st.last_tack_s = now_s
            st.tacks += 1
    return result(tack_heading(wind_from, st.tack, cfg), "beating", reason)
