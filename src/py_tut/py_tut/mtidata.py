import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3Stamped
from rclpy.qos import qos_profile_sensor_data

class TopicRelayNode(Node):
    def __init__(self):
        super().__init__('topic_relay_node')

        # 1. Create the Publisher
        self.z_pub = self.create_publisher(Float64, '/heading_direction', 10)
        self.lat_pub = self.create_publisher(Float64, '/latitude', 10)
        self.lon_pub = self.create_publisher(Float64, '/longitude', 10)
        self.roll_pub = self.create_publisher(Float64, '/roll', 10)
        self.pitch_pub = self.create_publisher(Float64, 'pitch', 10)
        # 2. Create the Subscriber
        # It calls 'listener_callback' every time a message is received
        self.z_sub = self.create_subscription(
            Vector3Stamped,
            '/filter/euler',
            self.listener_callback_z,
            qos_profile_sensor_data)
        self.lat_sub = self.create_subscription(
            Vector3Stamped,
            '/filter/positionlla',
            self.listener_callback_lat,
            qos_profile_sensor_data)

        self.get_logger().info('Relay Node has started.')

    def listener_callback_z(self, msg):
        # 3. Parsing/Processing Logic
        parsed_data = msg.vector.z
        # 4. Publish the new message
        new_msg = Float64()
        new_msg.data = parsed_data
        self.z_pub.publish(new_msg)
        parsed_data = msg.vector.x
        new_msg = Float64()
        new_msg.data = parsed_data
        self.roll_pub.publish(new_msg)
        parsed_data = msg.vector.y
        new_msg = Float64()
        new_msg.data = parsed_data
        self.pitch_pub.publish(new_msg)

    def listener_callback_lat(self, msg):
        parsed_data = msg.vector.x
        new_msg = Float64()
        new_msg.data = parsed_data
        self.lat_pub.publish(new_msg)
        parsed_data = msg.vector.y
        new_msg = Float64()
        new_msg.data = parsed_data
        self.lon_pub.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TopicRelayNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
