import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import threading
import json
from std_msgs.msg import String


class PCBReadWrite(Node):

    def __init__(self):
        super().__init__('PCBComm')
        
        #from original PCBComm file
        
        self.waypointCmd_publisher = self.create_publisher(String, 'waypoint_command', 10)


        # Boat state
        self.latitude = 44.696314
        self.longitude = -63.619043

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
        
    #Pretend PCBComm that is actually just reading from the command line
    def read_PCB(self):
            #this is a pretend string from PCBComm (it will actually be read over serial connection)
            lamePCBstr = input("Enter the command").strip()
            DICT = json.loads(lamePCBstr)

            if "WaypointCommand" in DICT:
                wp_cmd_block = DICT["WaypointCommand"]

                # There will only be one key inside
                command_type = list(wp_cmd_block.keys())[0]
                payload = wp_cmd_block[command_type]

                outgoing = {}
                if command_type == "add":
                    wp = payload[0]
                    outgoing = {
                        "cmd": "add",
                        "order": wp["order"],
                        "latitude": wp["latitude"],
                        "longitude": wp["longitude"]
                    }
                elif command_type == "remove":
                    wp = payload[0]
                    outgoing = {
                        "cmd": "remove",
                        "order": wp["order"]
                    }
                elif command_type == "startFollowing":
                    outgoing = {"cmd": "startFollowing"}

                elif command_type == "stopFollowing":
                    outgoing = {"cmd": "stopFollowing"}

                msg = String()
                msg.data = json.dumps(outgoing)

                self.waypointCmd_publisher.publish(msg)



def main(args=None):

    rclpy.init(args=args)
    node = PCBReadWrite()



    def input_loop():
        while rclpy.ok():
            coord_or_command = input("Enter 1 for lat, lon, 2 for command")
            if coord_or_command == "1":        
                user_input = input("Enter lat,lon: ")
                if user_input.strip() != "":
                    lat, lon = map(float, user_input.split(","))
                    node.latitude = lat
                    node.longitude = lon
            elif coord_or_command == "2":
                node.read_PCB()

    thread = threading.Thread(target=input_loop, daemon=True)
    thread.start()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()