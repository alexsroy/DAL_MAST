import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3Stamped

class TopicRelayNode(Node):
    def __init__(self):
        super().__init__('topic_relay_node')

        # 1. Create the Publisher
        self.z_pub = self.create_publisher(Float32, '/heading_direction', 10)
        self.lat_pub = self.create_publisher(Float32, '/latitude', 10)
        self.lon_pub = self.create_publisher(Float32, '/longitude', 10)
        self.roll_pub = self.create_publisher(Float32, '/roll', 10)
        self.pitch_pub = self.create_publisher(Float32, '/pitch', 10)
        # 2. Create the Subscriber
        # It calls 'listener_callback' every time a message is received
        self.z_sub = self.create_subscription(
            Vector3Stamped,
            '/filter/euler',
            self.listener_callback_z,
            10)
        self.lat_sub = self.create_subscription(
            Vector3Stamped,
            '/filter/positionlla',
            self.listener_callback_lat,
            10)

        self.get_logger().info('Relay Node has started.')

    def listener_callback_z(self, msg):
        print("Entered listener callback Z")
        # 3. Parsing/Processing Logic
        parsed_data = msg.vector.z
        # 4. Publish the new message
        new_msg = Float32()
        new_msg.data = parsed_data
        # Normalizes the negative values
        if (new_msg.data < 0):
            new_msg.data += 180.0
        # Converts from movella unit convention (North = 0deg) to nav alg convention (East = 0deg)
        new_msg.data = (new_msg.data + 270)%360
        self.z_pub.publish(new_msg)
        parsed_data = msg.vector.x
        new_msg = Float32()
        new_msg.data = parsed_data
        self.roll_pub.publish(new_msg)
        parsed_data = msg.vector.y
        new_msg = Float32()
        new_msg.data = parsed_data
        self.pitch_pub.publish(new_msg)

    def listener_callback_lat(self, msg):
        print("Entered listener callback Lat")
        parsed_data = msg.vector.x
        new_msg = Float32()
        new_msg.data = parsed_data
        self.lat_pub.publish(new_msg)
        parsed_data = msg.vector.y
        new_msg = Float32()
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
