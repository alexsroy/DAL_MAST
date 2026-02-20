import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import threading


class PCBReadWrite(Node):

    def __init__(self):
        super().__init__('PCBComm')

        # Boat state
        self.latitude = 44.616314
        self.longitude = -63.549043

        # Publishers
        self.latitude_publisher = self.create_publisher(Float32, 'latitude', 10)
        self.longitude_publisher = self.create_publisher(Float32, 'longitude', 10)

        # Timer to publish repeatedly
        self.timer = self.create_timer(0.1, self.publish_position)

        self.get_logger().info("Manual GPS Node Started")

    def publish_position(self):

        lat_msg = Float32()
        lon_msg = Float32()

        lat_msg.data = float(self.latitude)
        lon_msg.data = float(self.longitude)

        self.latitude_publisher.publish(lat_msg)
        self.longitude_publisher.publish(lon_msg)

    # Call this manually from terminal if desired
    def set_position(self, lat, lon):
        self.latitude = lat
        self.longitude = lon
        self.get_logger().info(f"New Position Set: {lat}, {lon}")


def main(args=None):

    rclpy.init(args=args)
    node = PCBReadWrite()



    def input_loop():
        while rclpy.ok():
            user_input = input("Enter lat,lon: ")
            if user_input.strip() != "":
                lat, lon = map(float, user_input.split(","))
                node.latitude = lat
                node.longitude = lon

    thread = threading.Thread(target=input_loop, daemon=True)
    thread.start()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()