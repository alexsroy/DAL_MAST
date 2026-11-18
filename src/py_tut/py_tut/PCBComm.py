"""The link to the STM32 over the Pi's serial port (the STM32's UART7).

Reads the windvane angle and waypoint commands the STM32 sends, and writes
the targets for the sail and rudder with the boat's position and heading.
The format, and what the firmware needs from it, is in pcb_protocol.py.

ROS parameters: port (default /dev/ttyS0), baud (9600, matching the STM32's
huart7), write_period_s (0.5).
"""

import serial  # https://github.com/AnrdyShmrdy/ros2_serial_interface/blob/main/ros2_serial_interface/serial_server.py
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32

from py_tut.pcb_protocol import LineReader, format_targets, parse_line

READ_PERIOD_S = 0.05      # drain the port often, so wind data never queues up


class PCBReadWrite(Node):
    def __init__(self):
        super().__init__('PCBComm')
        self.declare_parameter('port', '/dev/ttyS0')
        self.declare_parameter('baud', 9600)
        self.declare_parameter('write_period_s', 0.5)

        # timeout=0: reads return whatever has arrived, so the node never waits on the port.
        self.ser = serial.Serial(self.get_parameter('port').value, self.get_parameter('baud').value,
                                 timeout=0)
        self.ser.reset_input_buffer()
        self.lines = LineReader()

        # What goes to the STM32: TargetsOutput needs every one of these.
        self.targets = {key: 0.0 for key in ('targetBearing', 'waypointLat', 'waypointLon',
                                             'targetSailAngle', 'targetFlapAngle', 'targetRudderAngle',
                                             'latitude', 'longitude', 'headingAngle', 'windAngle')}
        for topic, key in (('sail_angle_target', 'targetSailAngle'), ('flap_angle_target', 'targetFlapAngle'),
                           ('rudder_angle_target', 'targetRudderAngle'),
                           ('heading_target_direction', 'targetBearing'),
                           ('waypoint_longitude', 'waypointLon'), ('waypoint_latitude', 'waypointLat'),
                           ('heading_direction', 'headingAngle'),
                           ('latitude', 'latitude'), ('longitude', 'longitude')):
            self.create_subscription(Float32, topic, self.store(key), 10)

        # Sensor data from the PCB
        self.windVane_publisher = self.create_publisher(Float32, 'wind_direction', 10)
        self.windSpeed_publisher = self.create_publisher(Float32, 'wind_speed', 10)
        self.waypointCmd_publisher = self.create_publisher(String, 'waypoint_command', 10)

        self.create_timer(READ_PERIOD_S, self.read_PCB)
        self.create_timer(self.get_parameter('write_period_s').value, self.writeToPCB)

    def store(self, key):
        def callback(msg):
            self.targets[key] = msg.data
        return callback

    def read_PCB(self):
        """Everything that has arrived since the last read, line by line."""
        try:
            data = self.ser.read(self.ser.in_waiting or 1)
        except serial.SerialException as error:
            self.get_logger().error(f'Serial read failed: {error}', throttle_duration_sec=5.0)
            return
        for line in self.lines.feed(data):
            kind, payload = parse_line(line)
            if kind == 'sensor':
                if not payload['windValid']:
                    self.get_logger().warn('The STM32 says the windvane reading is not valid.',
                                           throttle_duration_sec=10.0)
                    continue
                self.targets['windAngle'] = payload['windAngle']
                self.publish(self.windVane_publisher, payload['windAngle'])
                if 'windSpeed' in payload:
                    self.publish(self.windSpeed_publisher, payload['windSpeed'])
            elif kind == 'waypoint':
                msg = String()
                msg.data = payload
                self.waypointCmd_publisher.publish(msg)
            else:
                self.get_logger().debug(f'Ignored a line from the PCB: {line[:80]}')

    def writeToPCB(self):
        try:
            packet = format_targets(self.targets)
        except ValueError as error:          # too long for the STM32's buffer: say so, don't send it
            self.get_logger().error(str(error), throttle_duration_sec=5.0)
            return
        self.get_logger().debug(packet.strip())
        self.ser.write(packet.encode('ascii'))

    @staticmethod
    def publish(publisher, value):
        msg = Float32()
        msg.data = float(value)
        publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    handler = PCBReadWrite()
    try:
        rclpy.spin(handler)
    except KeyboardInterrupt:
        pass
    finally:
        handler.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
