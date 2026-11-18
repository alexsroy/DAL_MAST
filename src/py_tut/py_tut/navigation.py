"""The navigation node: turns the boat's position, heading and the wind into
the heading the rudder controller (controls.py) steers to.

The decisions are in nav_core.py, which has no ROS in it; see its docstring
for the frames, the units and the strategy. This node collects the inputs,
runs nav_core.guide() ten times a second and publishes the result.

Inputs
  latitude, longitude          the boat (Xsens MTi), degrees
  heading_direction            the boat's heading (MTi yaw, ENU degrees)
  wind_direction               the windvane: apparent wind angle, clockwise from the bow
  waypoint_latitude/longitude  the waypoint being sailed to (waypointControl)
  previous_waypoint_latitude/longitude   the start of the leg
Outputs
  heading_target_direction     the heading to steer, ENU degrees in [0, 360)
  nav_state                    "reaching", "beating (starboard tack)", "tacking onto the
                               port tack", ..., "waiting for ..."
  bearing_angle, bearing, bb_coords      the leg and its corridor, for displays
"""

import math
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Float32MultiArray, String

from py_tut.nav_core import (AngleFilter, NavConfig, NavState, guide, to_latlon, to_local,
                             wind_from_world)

STALE_FIX_S = 3.0          # a position older than this stops navigation updating
WIND_TAU_S = 6.0           # the windvane is noisy; average it over a few seconds
TACK_NAMES = {1: 'starboard tack', -1: 'port tack'}


class navigationNode(Node):

    def __init__(self):
        super().__init__('navigation')
        defaults = NavConfig()
        for name, value in vars(defaults).items():
            self.declare_parameter(name, value)
        self.config = NavConfig(**{name: self.get_parameter(name).value for name in vars(defaults)})
        self.state = NavState()
        self.wind = AngleFilter(WIND_TAU_S)

        self.inputs = {}           # topic -> (value, time received)
        for topic in ('latitude', 'longitude', 'heading_direction', 'wind_direction',
                      'waypoint_latitude', 'waypoint_longitude',
                      'previous_waypoint_latitude', 'previous_waypoint_longitude'):
            self.create_subscription(Float32, topic, self.store(topic), 10)

        self.targetHeading_publisher = self.create_publisher(Float32, 'heading_target_direction', 10)
        self.bearing_publisher = self.create_publisher(Float32MultiArray, 'bearing', 10)
        self.bearingAngle_publisher = self.create_publisher(Float32, 'bearing_angle', 10)
        self.nav_state = self.create_publisher(String, 'nav_state', 10)
        self.bb_coords = self.create_publisher(String, 'bb_coords', 10)

        self.create_timer(0.1, self.tick)
        self.create_timer(1.0, self.publish_corridor)
        self.last = None

    def store(self, topic):
        def callback(msg):
            self.inputs[topic] = (msg.data, time.monotonic())
            if topic == 'wind_direction' and 'heading_direction' in self.inputs:
                self.wind.update(wind_from_world(self.inputs['heading_direction'][0], msg.data),
                                 time.monotonic())
        return callback

    def value(self, topic):
        return self.inputs[topic][0]

    def tick(self):
        missing = [t for t in ('latitude', 'longitude', 'heading_direction', 'wind_direction',
                               'waypoint_latitude', 'waypoint_longitude') if t not in self.inputs]
        if missing or self.wind.value is None:
            self.say('waiting for ' + (', '.join(missing) or 'the wind'))
            return
        now = time.monotonic()
        if now - self.inputs['latitude'][1] > STALE_FIX_S:
            self.say('waiting for a fresh position')
            self.get_logger().warn('No position for over %.0f s; holding the last heading target.'
                                   % STALE_FIX_S, throttle_duration_sec=5.0)
            return

        # The leg starts at the previous waypoint; with none yet, it's a point at the waypoint.
        start = 'previous_waypoint' if 'previous_waypoint_latitude' in self.inputs else 'waypoint'
        lat0, lon0 = self.value(start + '_latitude'), self.value(start + '_longitude')
        a = (0.0, 0.0)
        b = to_local(self.value('waypoint_latitude'), self.value('waypoint_longitude'), lat0, lon0)
        boat = to_local(self.value('latitude'), self.value('longitude'), lat0, lon0)
        heading = self.value('heading_direction') % 360.0
        g = guide(self.config, self.state, now, boat, heading, self.wind.value, a, b,
                  vane_cw=self.value('wind_direction'))
        self.last = (g, lat0, lon0, a, b)

        self.publish(self.targetHeading_publisher, g.heading)
        self.publish(self.bearingAngle_publisher, g.leg_bearing)
        array = Float32MultiArray()
        array.data = [float(lon0), float(lat0), float(self.value('waypoint_longitude')),
                      float(self.value('waypoint_latitude'))]
        self.bearing_publisher.publish(array)
        if g.mode == 'reaching':
            self.say('reaching')
        else:
            self.say(('tacking onto the %s' if self.state.tacking_since is not None
                      else 'beating (%s)') % TACK_NAMES[g.tack])
        if g.reason:
            self.get_logger().info('%s: on the %s, %+.0f m off the leg, %.0f m to go' % (
                g.reason, TACK_NAMES.get(g.tack, 'reach'), g.cross_track_m, g.distance_m))
        self.get_logger().debug('heading %.0f -> %.0f (%s), wind from %.0f, %.0f m to go' % (
            heading, g.heading, g.mode, self.wind.value, g.distance_m))

    def publish_corridor(self):
        """The corridor's corners as lat/lon, for displays (once a second)."""
        if self.last is None:
            return
        g, lat0, lon0, a, b = self.last
        half = self.config.corridor_half_width_m
        nx, ny = -math.sin(math.radians(g.leg_bearing)), math.cos(math.radians(g.leg_bearing))
        corners = {'APlus': (a[0] + nx * half, a[1] + ny * half),
                   'AMinus': (a[0] - nx * half, a[1] - ny * half),
                   'BPlus': (b[0] + nx * half, b[1] + ny * half),
                   'BMinus': (b[0] - nx * half, b[1] - ny * half)}
        text = String()
        text.data = ''.join('\n%s: (%.6f, %.6f)' % (name, *to_latlon(x, y, lat0, lon0))
                            for name, (x, y) in corners.items())
        self.bb_coords.publish(text)

    def say(self, state):
        msg = String()
        msg.data = state
        self.nav_state.publish(msg)

    @staticmethod
    def publish(publisher, value):
        msg = Float32()
        msg.data = float(value)
        publisher.publish(msg)


def main():
    rclpy.init()
    node = navigationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
