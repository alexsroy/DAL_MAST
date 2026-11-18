"""Tests for control_law: plain pytest, no ROS needed.

    cd src/py_tut && python -m pytest test/test_control_law.py
"""

import pytest

from py_tut.control_law import (SIDE_HYSTERESIS_DEG, angle_of_attack, crossing_the_wind,
                                rudder_command, sail_target, shortestAngle, thrust_sail_offset,
                                wing_side)


def test_shortest_angle_wraps_any_difference():
    assert shortestAngle(10, 350) == pytest.approx(20)
    assert shortestAngle(-170, 400) == pytest.approx(150)      # the old one gave -210
    assert shortestAngle(0, 0) == 0


def test_rudder_is_symmetric_and_limited():
    for error in (5, 20, 80):
        assert rudder_command(error, 0, 0, 0.8, 0.4, 30) == pytest.approx(
            -rudder_command(-error, 0, 0, 0.8, 0.4, 30))
    assert rudder_command(170, 0, 0, 0.8, 0.4, 30) == 30
    assert rudder_command(-170, 0, 0, 0.8, 0.4, 30) == -30


def test_rudder_eases_off_as_the_boat_turns_toward_its_target():
    # 20 deg off course: the heading is closing on the target at 10 deg/s.
    still = rudder_command(20, 0, 0, 0.8, 0.4, 30)
    turning = rudder_command(20, 0, -10, 0.8, 0.4, 30)
    assert 0 < turning < still


def test_rudder_works_across_north():
    assert rudder_command(355, 5, 0, 1.0, 0, 30) == pytest.approx(-10)


def test_wing_side_puts_the_thrust_toward_the_bow():
    # Wind on the starboard beam (90 clockwise): side -1 points the thrust to 90 - 65 = 25 deg off the bow.
    assert wing_side(90, 0) == -1
    assert wing_side(270, 0) == 1
    # The side doesn't depend on where the boat points (the old code compared with the heading).
    offset = angle_of_attack + thrust_sail_offset
    assert abs(((90 - offset) + 180) % 360 - 180) < abs(((90 + offset) + 180) % 360 - 180)


def test_wing_side_holds_near_the_switch_point():
    # Dead downwind (180), both sides are equally good: keep the side already set.
    assert wing_side(180, 1) == 1 and wing_side(180, -1) == -1
    assert wing_side(180 + SIDE_HYSTERESIS_DEG / 4, -1) == -1


def test_a_tack_crosses_the_wind_and_a_gybe_or_a_course_change_does_not():
    # ENU headings: wind from the north (90). Starboard tack heads 135, port tack 45.
    assert crossing_the_wind(45, 135, 45)            # starboard to port: through the eye
    assert crossing_the_wind(-45, 45, 135)           # and back
    assert not crossing_the_wind(45, 135, 120)       # bearing away on the same tack
    assert not crossing_the_wind(150, 300, 240)      # a gybe: the wind crosses the stern
    assert not crossing_the_wind(45, 135, 135)       # on course


def test_the_wing_feathers_while_tacking_and_trims_otherwise():
    sail, side = sail_target(45, 135, 45, -1)
    assert (sail, side) == (45, -1)                  # pointing into the wind: no drive
    sail, side = sail_target(45, 135, 140, -1)
    assert sail == pytest.approx((45 + side * angle_of_attack) % 360)
    sail, side = sail_target(45, 135, None, 1)       # no target yet: trim as usual
    assert sail == pytest.approx((45 + side * angle_of_attack) % 360)
