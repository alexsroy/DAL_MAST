"""Tests for nav_core: plain pytest, no ROS needed.

    cd src/py_tut && python -m pytest test/test_nav_core.py
"""

import math
import random

import pytest

from py_tut.nav_core import (AngleFilter, NavConfig, NavState, bearing, guide, to_latlon,
                             to_local, wind_from_world, wrap180)

NORTH, EAST, SOUTH, WEST = 90.0, 0.0, 270.0, 180.0      # ENU degrees


def test_wrap180_handles_any_size_of_angle():
    for raw, wrapped in [(0, 0), (180, -180), (-180, -180), (190, -170), (-190, 170),
                         (400, 40), (-570, 150), (720, 0), (359.5, -0.5)]:
        assert wrap180(raw) == pytest.approx(wrapped)


def test_local_projection_round_trips_and_scales_longitude():
    lat0, lon0 = 44.6925, -63.553
    x, y = to_local(lat0 + 0.001, lon0 + 0.001, lat0, lon0)
    assert y == pytest.approx(111.2, abs=0.2)
    assert x == pytest.approx(111.2 * math.cos(math.radians(lat0)), abs=0.2)    # about 79 m
    assert to_latlon(x, y, lat0, lon0) == pytest.approx((lat0 + 0.001, lon0 + 0.001))


def test_bearing_is_enu():
    assert bearing((0, 0), (0, 10)) == pytest.approx(NORTH)
    assert bearing((0, 0), (-10, 0)) == pytest.approx(WEST)
    assert bearing((0, 0), (0, -10)) == pytest.approx(SOUTH)


def test_windvane_angle_turns_into_the_world_frame():
    # Heading east, the wind 90 degrees clockwise from the bow (starboard beam): from the south.
    assert wind_from_world(EAST, 90) == pytest.approx(SOUTH)
    # Heading north, wind dead ahead: from the north.
    assert wind_from_world(NORTH, 0) == pytest.approx(NORTH)
    # Heading north, wind on the port beam (270 clockwise): from the west.
    assert wind_from_world(NORTH, 270) == pytest.approx(WEST)


def test_angle_filter_averages_across_north():
    f = AngleFilter(tau_s=1.0)
    f.update(350, 0.0)
    for t in range(1, 50):
        value = f.update(10 if t % 2 else 350, t * 0.1)
    assert abs(wrap180(value - 0)) < 6


def reach(cfg=None, **kwargs):
    return guide(cfg or NavConfig(), NavState(), 0.0, **kwargs)


def test_reaching_aims_along_the_leg_and_corrects_drift():
    a, b = (0.0, 0.0), (0.0, 200.0)                                   # a leg due north
    on_line = reach(boat=(0.0, 50.0), heading=NORTH, wind_from=EAST, a=a, b=b)
    assert on_line.mode == 'reaching' and on_line.heading == pytest.approx(NORTH)
    left = reach(boat=(-20.0, 50.0), heading=NORTH, wind_from=EAST, a=a, b=b)
    right = reach(boat=(20.0, 50.0), heading=NORTH, wind_from=EAST, a=a, b=b)
    assert left.cross_track_m > 0 > right.cross_track_m
    assert wrap180(left.heading - NORTH) < 0 < wrap180(right.heading - NORTH)   # both turn back


def test_north_and_south_legs_work_like_any_other():
    """The old slope/intercept test divided by tan(90 deg) on these legs."""
    for b in [(0.0, 300.0), (0.0, -300.0), (300.0, 0.0), (-300.0, 0.0), (212.0, 212.0)]:
        leg = bearing((0, 0), b)
        g = reach(boat=(0.0, 0.0), heading=leg, wind_from=(leg + 90) % 360, a=(0, 0), b=b)
        assert g.heading == pytest.approx(leg, abs=1e-6)


def test_the_last_stretch_aims_straight_at_the_waypoint():
    g = reach(boat=(8.0, 190.0), heading=NORTH, wind_from=EAST, a=(0.0, 0.0), b=(0.0, 200.0))
    assert g.heading == pytest.approx(bearing((8.0, 190.0), (0.0, 200.0)))


def test_an_upwind_leg_is_sailed_close_hauled_on_the_nearer_tack():
    cfg = NavConfig()
    g = reach(cfg, boat=(0.0, 0.0), heading=NORTH + 30, wind_from=NORTH, a=(0, 0), b=(0, 300))
    assert g.mode == 'beating' and g.tack == 1                      # starboard: heading NW
    assert g.heading == pytest.approx(NORTH + cfg.tack_angle_deg)
    g = reach(cfg, boat=(0.0, 0.0), heading=NORTH - 30, wind_from=NORTH, a=(0, 0), b=(0, 300))
    assert g.tack == -1 and g.heading == pytest.approx(NORTH - cfg.tack_angle_deg)


def test_tacks_at_the_corridor_edge_but_not_before_the_minimum_interval():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 30, wind, a, b)              # starboard tack: heading NW
    assert st.tack == 1
    inside = guide(cfg, st, 20.0, (-cfg.corridor_half_width_m + 5, 40), NORTH + 45, wind, a, b)
    assert inside.tack == 1 and not inside.reason
    edge = guide(cfg, st, 30.0, (-cfg.corridor_half_width_m - 1, 60), NORTH + 45, wind, a, b)
    assert edge.tack == -1 and edge.reason == 'corridor edge'
    again = guide(cfg, st, 31.0, (cfg.corridor_half_width_m + 1, 70), NORTH - 45, wind, a, b)
    assert again.tack == -1                                         # too soon to tack back
    later = guide(cfg, st, 30.0 + cfg.min_tack_interval_s, (cfg.corridor_half_width_m + 1, 70),
                  NORTH - 45, wind, a, b)
    assert later.tack == 1 and later.reason == 'corridor edge'


def test_tacks_on_the_layline_to_fetch_the_waypoint():
    cfg, st = NavConfig(corridor_half_width_m=500), NavState()
    a, b, wind = (0, 0), (0, 300), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 30, wind, a, b)               # starboard, heading NW
    # B bears 43 deg right of the wind: port tack (45 deg off) would sail just below it. Hold on.
    g = guide(cfg, st, 60.0, (-150.0, 140.0), NORTH + 45, wind, a, b)
    assert not g.reason and g.tack == 1
    # Further left, B is past the layline (45 + 3 deg overstand): tack and fetch it.
    g = guide(cfg, st, 90.0, (-220.0, 110.0), NORTH + 45, wind, a, b)
    assert g.reason == 'layline' and g.tack == -1


def test_leaving_the_no_go_zone_needs_a_margin():
    cfg, st = NavConfig(), NavState()
    a, b = (0, 0), (0, 300)
    guide(cfg, st, 0.0, (0, 0), NORTH, NORTH + 40, a, b)              # 40 deg off: beating
    assert st.beating
    g = guide(cfg, st, 1.0, (0, 0), NORTH, NORTH + cfg.no_go_deg + 2, a, b)
    assert g.mode == 'beating'                                     # inside the hysteresis band
    g = guide(cfg, st, 2.0, (0, 0), NORTH, NORTH + cfg.no_go_deg + cfg.hysteresis_deg + 1, a, b)
    assert g.mode == 'reaching'



def test_a_tack_is_through_once_the_wind_is_well_onto_the_new_bow():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 45, wind, a, b)
    guide(cfg, st, 30.0, (-cfg.corridor_half_width_m - 1, 60), NORTH + 45, wind, a, b)
    assert st.tack == -1 and st.tacking_since == 30.0
    guide(cfg, st, 33.0, (-31, 61), NORTH - 5, wind, a, b)          # just past head to wind
    assert st.tacking_since == 30.0                                 # not through yet
    guide(cfg, st, 36.0, (-31, 62), NORTH - cfg.tack_done_deg - 1, wind, a, b)
    assert st.tacking_since is None and st.failed_tacks == 0


def test_a_slow_tack_that_has_crossed_the_wind_is_not_given_up():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 45, wind, a, b)
    guide(cfg, st, 30.0, (-cfg.corridor_half_width_m - 1, 60), NORTH + 45, wind, a, b)
    g = guide(cfg, st, 31.0 + cfg.tack_timeout_s, (-31, 61), NORTH - 10, wind, a, b)
    assert g.tack == -1 and st.failed_tacks == 0                    # through: keep going
    g = guide(cfg, st, 40.0 + cfg.tack_timeout_s, (-31, 62), NORTH - 30, wind, a, b)
    assert st.tacking_since is None                                 # and settled


def test_the_windvane_decides_which_bow_the_wind_is_on():
    # The averaged wind says the boat is just through it; the vane says it isn't.
    # Believing the average stalled the boat for good in the simulator.
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 45, wind, a, b, vane_cw=40)
    guide(cfg, st, 30.0, (-cfg.corridor_half_width_m - 1, 60), NORTH + 45, wind, a, b, vane_cw=40)
    stuck = (-31, 61)
    g = guide(cfg, st, 31.0 + cfg.tack_timeout_s, stuck, NORTH - 2, wind, a, b, vane_cw=4)
    assert g.reason == 'tack stalled' and g.tack == 1


def test_a_boat_knocked_head_to_wind_without_tacking_bears_away():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 45, wind, a, b, vane_cw=40)
    assert st.tacking_since is None
    guide(cfg, st, 5.0, (-5, 10), NORTH + 45, wind, a, b, vane_cw=-3)       # a big header
    g = guide(cfg, st, 6.0 + cfg.tack_timeout_s, (-5, 10), NORTH + 45, wind, a, b, vane_cw=-3)
    assert g.reason == 'tack stalled' and g.tack == -1               # sail off on the tack it's on


def test_a_stalled_tack_is_given_up_and_tried_again_after_building_speed():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (0, 400), NORTH
    guide(cfg, st, 0.0, (0, 0), NORTH + 45, wind, a, b)
    guide(cfg, st, 30.0, (-cfg.corridor_half_width_m - 1, 60), NORTH + 45, wind, a, b)
    stuck = (-cfg.corridor_half_width_m - 2, 61)
    g = guide(cfg, st, 30.0 + cfg.tack_timeout_s - 1, stuck, NORTH + 15, wind, a, b)
    assert g.tack == -1                                             # still trying
    g = guide(cfg, st, 30.0 + cfg.tack_timeout_s + 1, stuck, NORTH + 15, wind, a, b)
    assert g.tack == 1 and g.reason == 'tack stalled' and st.failed_tacks == 1
    assert g.heading == pytest.approx(NORTH + cfg.tack_angle_deg)   # back onto the old tack
    retry_at = st.no_tack_before_s
    g = guide(cfg, st, retry_at - 1, stuck, NORTH + 45, wind, a, b)
    assert g.tack == 1                                              # still building speed
    g = guide(cfg, st, retry_at, stuck, NORTH + 45, wind, a, b)
    assert g.tack == -1 and g.reason == 'corridor edge'



def test_beating_starts_on_the_side_the_boat_was_last_steered_to():
    # A mark near the edge of the no-go zone: reaching steers to the starboard side of the
    # wind while the boat, mid-turn, still points to port. GPS noise then puts the mark just
    # inside the no-go zone. Beating must carry on to starboard, not flip back to port.
    cfg, st = NavConfig(), NavState()
    a, wind = (0, 0), NORTH
    g = guide(cfg, st, 0.0, (0, 0), NORTH - 40, wind, a, (-100, 100), vane_cw=-40)
    assert g.mode == 'reaching' and wrap180(g.heading - wind) > 0
    g = guide(cfg, st, 1.0, (0, 0), NORTH - 30, wind, a, (-90, 100), vane_cw=-30)
    assert g.mode == 'beating' and g.tack == 1


def test_a_tack_asked_for_by_a_reach_is_watched_too():
    cfg, st = NavConfig(), NavState()
    a, b, wind = (0, 0), (-100, 100), NORTH            # B 45 deg to the left of the wind
    g = guide(cfg, st, 0.0, (0, 0), NORTH - 40, wind, a, b, vane_cw=-40)
    assert g.mode == 'reaching' and st.tacking_since == 0.0
    g = guide(cfg, st, cfg.tack_timeout_s + 1, (0, 0), NORTH - 5, wind, a, b, vane_cw=-5)
    assert g.reason == 'tack stalled'
    assert g.heading == pytest.approx(NORTH - cfg.tack_angle_deg)    # off on the bow it's on
    g = guide(cfg, st, cfg.tack_timeout_s + 2, (0, 0), NORTH - 20, wind, a, b, vane_cw=-20)
    assert g.heading == pytest.approx(NORTH - cfg.tack_angle_deg)    # building speed first


# ----- a whole course with a simple boat ---------------------------------------------

def boat_speed(heading, wind_from):
    """A crude polar for a small wing-sailed boat: nothing within 35 deg of the wind."""
    off = abs(wrap180(heading - wind_from))
    if off < 35:
        return 0.15
    if off < 60:
        return 0.15 + (off - 35) / 25 * 1.0
    return 1.2 if off < 150 else 1.0


def sail_course(course, wind_mean, seed=1, minutes=40, arrive_m=10.0):
    rng = random.Random(seed)
    cfg, st = NavConfig(), NavState()
    x, y, heading = course[0][0], course[0][1], NORTH
    leg, t, dt = 1, 0.0, 0.1
    worst_cross, tack_times = {}, []
    while leg < len(course) and t < minutes * 60:
        wind = wind_mean + 10 * math.sin(t / 90) + rng.gauss(0, 3)  # slow shifts and noise
        g = guide(cfg, st, t, (x, y), heading, wind, course[leg - 1], course[leg])
        if g.reason in ('corridor edge', 'layline'):
            tack_times.append(t)
        if g.mode == 'beating':
            worst_cross[leg] = max(worst_cross.get(leg, 0), abs(g.cross_track_m))
        turn = max(-15 * dt, min(15 * dt, wrap180(g.heading - heading)))  # 15 deg/s
        heading = (heading + turn) % 360
        speed = boat_speed(heading, wind)
        x += speed * math.cos(math.radians(heading)) * dt
        y += speed * math.sin(math.radians(heading)) * dt
        if math.hypot(course[leg][0] - x, course[leg][1] - y) < arrive_m:
            leg += 1
        t += dt
    return leg, t, worst_cross, tack_times, cfg


def test_sails_a_course_with_a_dead_upwind_leg():
    # Start, a beat dead into a northerly, a reach east, a run south, a reach home.
    course = [(0, 0), (0, 250), (180, 250), (180, -60), (0, 0)]
    leg, t, worst_cross, tack_times, cfg = sail_course(course, wind_mean=NORTH)
    assert leg == len(course), f'stuck on leg {leg} after {t:.0f} s'
    assert worst_cross[1] < cfg.corridor_half_width_m + 15           # stayed near the corridor
    assert 2 <= len(tack_times) <= 20
    gaps = [b - a for a, b in zip(tack_times, tack_times[1:])]
    assert all(gap >= cfg.min_tack_interval_s - 1e-6 for gap in gaps)


@pytest.mark.parametrize('wind', [0, 45, 90, 135, 180, 225, 270, 315])
def test_gets_round_whatever_the_wind(wind):
    course = [(0, 0), (150, 150), (-100, 200), (0, 0)]
    leg, t, *_ = sail_course(course, wind_mean=wind, seed=wind)
    assert leg == len(course), f'wind from {wind}: stuck on leg {leg} after {t:.0f} s'


def test_a_tick_is_cheap():
    import time
    cfg, st = NavConfig(), NavState()
    start = time.perf_counter()
    for i in range(10000):
        guide(cfg, st, i * 0.1, (i % 50 - 25, i * 0.01), NORTH, NORTH + 5, (0, 0), (0, 400))
    per_tick_us = (time.perf_counter() - start) / 10000 * 1e6
    assert per_tick_us < 200                                        # 10 Hz needs < 100,000
