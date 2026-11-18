"""The control laws behind controls.py, with no ROS in them so they can be
tested anywhere. See controls.py for the angle conventions."""

maxFlapDeflection = 45
thrust_sail_offset = 57         # where the wing's force points, past the angle of attack
angle_of_attack = 8
SIDE_HYSTERESIS_DEG = 10        # change the wing's side only when the other is clearly better


def wrap180(deg):
    """An angle in degrees, wrapped into [-180, 180)."""
    return (deg + 180.0) % 360.0 - 180.0


def shortestAngle(referenceAngle, targetAngle):
    """referenceAngle - targetAngle, wrapped into [-180, 180). (The old version
    wrapped only once, so differences beyond +/-540 degrees came out wrong.)"""
    return wrap180(referenceAngle - targetAngle)


def wing_side(vane_cw, current_side):
    """Which side (+1 or -1) to set the wing's angle of attack on.

    Each side pushes the boat along a thrust direction (the wind's angle
    plus or minus angle_of_attack + thrust_sail_offset, in the windvane's
    frame). The better side is the one whose thrust points closest to the
    bow, which is 0 in that frame. (The old code measured it against the
    compass heading, a different frame, so the side it chose depended on
    which way the boat happened to point.)
    """
    miss = {side: abs(wrap180(vane_cw + side * (angle_of_attack + thrust_sail_offset)))
            for side in (1, -1)}
    best = min(miss, key=miss.get)
    if current_side in miss and miss[current_side] - miss[best] < SIDE_HYSTERESIS_DEG:
        return current_side
    return best


def crossing_the_wind(vane_cw, heading, target):
    """True while the turn from heading to target passes through the wind's
    eye, that is, while the boat is tacking. vane_cw is where the wind is now
    (clockwise from the bow); on the target heading it would be at
    vane_cw + target - heading, on the other bow. A gybe (both angles abaft
    the beam) doesn't count."""
    here = wrap180(vane_cw)
    there = wrap180(vane_cw + target - heading)
    return here * there < 0 and abs(here) < 90 and abs(there) < 90


def sail_target(vane_cw, heading, target, current_side):
    """The wing's angle (the windvane's frame, [0, 360)) and the side it's set on.

    While tacking, the wing feathers into the wind. Trimmed for the old tack
    it keeps pushing the bow back off the wind, harder than a rudder on a boat
    that is slowing down can turn it, and the boat stalls head to wind. With
    no target yet, it trims as usual.
    """
    if target is not None and crossing_the_wind(vane_cw, heading, target):
        return vane_cw % 360.0, current_side
    side = wing_side(vane_cw, current_side)
    return (vane_cw + side * angle_of_attack) % 360.0, side


def rudder_command(heading, target, heading_rate, kp, kd, limit):
    """Proportional on the heading error, damped by the turn rate (on the
    measurement, so a new target gives no derivative kick), the same gain
    both ways (the old code turned one way twice as hard as the other)."""
    error = shortestAngle(heading, target)
    return max(-limit, min(limit, kp * error + kd * heading_rate))
