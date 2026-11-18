"""Turns the target heading and the wind into sail, flap and rudder targets.

Angles
  heading_direction, heading_target_direction: ENU degrees (the MTi's yaw).
  wind_direction: the windvane's apparent wind angle, clockwise from the bow.
  sail_angle_target: the wing's angle in the windvane's frame, [0, 360);
    the STM32 adds its encoder's centre (180) and turns the wing there.
  rudder_angle_target: degrees, positive when the heading is counter-
    clockwise of the target (the existing sign), within +/- max_rudder_deg.

When following is off, the rudder centres and the wing feathers into the
apparent wind, so the boat stops driving instead of holding a last target.
The wing also feathers while the boat tacks (control_law.sail_target).
"""

import math
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool, Float32

from py_tut.control_law import rudder_command, sail_target, wrap180

HEADING_RATE_TAU_S = 0.3


class controlConfigurationService(Node):

    def __init__(self):
        super().__init__('controls')
        self.declare_parameter('rudder_kp', 0.8)          # degrees of rudder per degree off course
        self.declare_parameter('rudder_kd', 0.4)          # per degree/second of turn
        self.declare_parameter('max_rudder_deg', 30.0)    # past about 25 degrees a rudder stalls and brakes

        self.windVane_subscription = self.create_subscription(Float32, 'wind_direction', self.wind_callback, 10)
        self.compass_subscription = self.create_subscription(Float32, 'heading_direction', self.compass_callback, 10)
        self.targetHeading_subscription = self.create_subscription(Float32, 'heading_target_direction', self.heading_target_callback, 10)
        self.following_subscription = self.create_subscription(Bool, 'following', self.following_callback, 10)

        self.targetSailAngle_publisher = self.create_publisher(Float32, 'sail_angle_target', 10)
        self.targetFlapAngle_publisher = self.create_publisher(Float32, 'flap_angle_target', 10)
        self.targetRudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle_target', 10)

        self.windAngle = 0.0
        self.heading = 0.0
        self.headingRate = 0.0               # degrees per second, smoothed
        self._last_heading = None
        self.targetHeading = None            # nothing to steer to until navigation says
        self.following = True
        self.wingSide = 1

        self.sailTimer = self.create_timer(0.1, self.sail_pub_callback)
        self.flapTimer = self.create_timer(0.1, self.flap_pub_callback)
        self.rudderTimer = self.create_timer(0.1, self.rudder_pub_callback)

    def wind_callback(self, msg):
        self.windAngle = msg.data

    def compass_callback(self, msg):
        now = time.monotonic()
        if self._last_heading is not None:
            then, previous = self._last_heading
            dt = now - then
            if dt > 1e-3:
                rate = wrap180(msg.data - previous) / dt
                k = 1.0 - math.exp(-dt / HEADING_RATE_TAU_S)
                self.headingRate += (rate - self.headingRate) * k
        self._last_heading = (now, msg.data)
        self.heading = msg.data

    def heading_target_callback(self, msg):
        self.targetHeading = msg.data

    def following_callback(self, msg):
        self.following = msg.data

    def sail_pub_callback(self):
        msg = Float32()
        if self.following:
            sail, self.wingSide = sail_target(self.windAngle, self.heading, self.targetHeading,
                                              self.wingSide)
            msg.data = float(sail)
        else:
            msg.data = float(self.windAngle % 360)       # feathered: no drive
        self.targetSailAngle_publisher.publish(msg)

    def flap_pub_callback(self):
        # The flap isn't driven yet (the STM32 ignores targetFlapAngle), and the
        # old logic compared the windvane's angle with the compass heading,
        # which are in different frames. Rebuild it on the wing side above.
        pass

    def rudder_pub_callback(self):
        msg = Float32()
        if not self.following or self.targetHeading is None:
            msg.data = 0.0
        else:
            msg.data = float(rudder_command(self.heading, self.targetHeading, self.headingRate,
                                            self.get_parameter('rudder_kp').value,
                                            self.get_parameter('rudder_kd').value,
                                            self.get_parameter('max_rudder_deg').value))
        self.targetRudderAngle_publisher.publish(msg)


def main():
    rclpy.init()
    control_service = controlConfigurationService()
    try:
        rclpy.spin(control_service)
    except KeyboardInterrupt:
        pass
    finally:
        control_service.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
