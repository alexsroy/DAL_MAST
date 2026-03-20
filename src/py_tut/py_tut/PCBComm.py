import serial # https://github.com/AnrdyShmrdy/ros2_serial_interface/blob/main/ros2_serial_interface/serial_server.py
import json   # https://stackoverflow.com/questions/27858041/oserror-errno-13-permission-denied-dev-ttyacm0-using-pyserial-from-pyth
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32

MANUAL_INPUT_MODE = True

class PCBReadWrite(Node):
    def __init__(self):
        super().__init__('PCBComm')

        self.PCBStr = ""

        #COMMENT OUT these lines to run without the pcb
        #self.ser = serial.Serial("/dev/ttyS0", 115200, timeout = 0.1)
        #self.ser.reset_input_buffer()

        # OUTPUTS
        self.targetBearing = 0.0                # These are floats to be published for informative value
        self.waypointLat = 0.0
        self.waypointLon = 0.0
        self.prevWaypointLat = 0.0
        self.prevWaypointLon = 0.0

        # These are control surfaces the PCB needs to react to
        self.targetSailAngle = 0.0        # (0, 360)
        self.targetRudderAngle = 0.0      # (-45, 45)
        self.targetFlapAngle = 0.0        # (-45, 45)

        # INPUTS
        self.windAngle = 0.0 # (0, 360)
        self.sailAngle = 0.0 # (0, 360)
        self.flapAngle = 0.0
        self.rudderAngle = 0.0
        self.headingAngle = 0.0 # (0, 360)
        self.latitude = 0.0
        self.longitude = 0.0

        # These are subscriptions to store variables from the subscriptions
        self.targetSailAngle_subscriber = self.create_subscription(Float32, 'sail_angle_target', self.sail_target_callback, 10)
        self.targetFlapAngle_subscriber = self.create_subscription(Float32, 'flap_angle_target', self.flap_target_callback, 10)
        self.targetRudderAngle_subscriber = self.create_subscription(Float32, 'rudder_angle_target', self.rudder_target_callback, 10)
        self.targetHeading_subscriber = self.create_subscription(Float32, 'heading_target_direction', self.target_heading_callback, 10)
        self.waypoint_longitude_subscription = self.create_subscription(Float32, 'waypoint_longitude', self.waypoint_longitude_callback, 10)
        self.waypoint_latitude_subscription = self.create_subscription(Float32, 'waypoint_latitude', self.waypoint_latitude_callback, 10)
        self.previous_Waypoint_longitude_subscription = self.create_subscription(Float32, 'previous_waypoint_longitude', self.previous_Waypoint_longitude_callback, 10)
        self.previous_Waypoint_latitude_subscription = self.create_subscription(Float32, 'previous_waypoint_latitude', self.previous_Waypoint_latitude_callback, 10)

        # These are publishers that are sensor data from the PCB
        self.windVane_publisher = self.create_publisher(Float32, 'wind_direction', 10)
        self.compass_publisher = self.create_publisher(Float32, 'heading_direction', 10)
        self.latitude_publisher = self.create_publisher(Float32, 'latitude', 10)
        self.longitude_publisher = self.create_publisher(Float32, 'longitude', 10)
        self.sailAngle_publisher = self.create_publisher(Float32, 'sail_angle', 10)
        self.flapAngle_publisher = self.create_publisher(Float32, 'flap_angle', 10)
        self.rudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle', 10)

        self.waypointCmd_publisher = self.create_publisher(String, 'waypoint_command', 10)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.read_PCB)

        timer_period = 0.1737  # seconds

        #COMMENT OUT this line to run without the pcb
        #self.timer = self.create_timer(timer_period, self.writeToPCB)


    # The json should be in the form of: {"latitude": 53.54, "longitude": 45.23, "sail_angle": 2.2, "flap_angle": 30.2, "rudder_angle": 11.1, "heading_angle": 145, "wind_angle": 76.0}
    def read_PCB(self):

            if MANUAL_INPUT_MODE:
                self.PCBStr = input(">")
            else:
                # Read value from PCB
                self.PCBStr = self.ser.readline().decode('utf-8').rstrip()

            print("read from PCB: ", self.PCBStr)
            #self.PCBStr = "" # this is the str from the PCB

            DICT = json.loads(self.PCBStr)

            if "wind_angle" in DICT.keys():
                f = Float32()
                f.data = float(DICT["wind_angle"])
                self.windVane_publisher.publish(f)

                f.data = float(DICT["heading_angle"])
                self.compass_publisher.publish(f)

                f.data = float(DICT["rudder_angle"])
                self.rudderAngle_publisher.publish(f)

                f.data = float(DICT["flap_angle"])
                self.flapAngle_publisher.publish(f)

                f.data = float(DICT["sail_angle"])
                self.sailAngle_publisher.publish(f)

                f.data = float(DICT["longitude"])
                self.longitude_publisher.publish(f)

                f.data = float(DICT["latitude"])
                self.latitude_publisher.publish(f)

            waypoint_commands = ["add", "remove", "startFollowing", "stopFollowing", "setCurrentWaypoint", "refreshWaypoints"]
            if any(cmd in self.PCBStr for cmd in waypoint_commands):
                msg = String()
                msg.data = self.PCBStr
                self.waypointCmd_publisher.publish(msg)

    # Update the motors when we hear something from other ROS nodes
    def sail_target_callback(self, msg):
        self.targetSailAngle = msg.data

    def flap_target_callback(self, msg):
        self.targetFlapAngle = msg.data

    def rudder_target_callback(self, msg):
        self.targetRudderAngle = msg.data

    def target_heading_callback(self, msg):
        self.targetBearing = msg.data

    def waypoint_longitude_callback(self, msg):
        self.waypointLon = msg.data

    def waypoint_latitude_callback(self, msg):
        self.waypointLat = msg.data
        
    def previous_Waypoint_longitude_callback(self, msg):
        self.prevWaypointLon = msg.data

    def previous_Waypoint_latitude_callback(self, msg):
        self.prevWaypointLat = msg.data

    def writeToPCB(self):
        writeStr = self.PCBStr[:-1]
        variablesToWrite = [["sail_angle_target", self.targetSailAngle], ["flap_angle_target", self.targetFlapAngle], ["rudder_angle_target", self.targetRudderAngle], ["heading_target", self.targetBearing], ["waypoint_longitude", self.waypointLon], ["waypoint_latitude", self.waypointLat]]

        for var in variablesToWrite:
            writeStr += ', \"' + var[0] + '\": ' + str(var[1])

        writeStr += '}'

        self.ser.write(bytes(writeStr,'utf-8'))

def main(args=None):
    # Main loop
    #print(getCourse)

    rclpy.init(args=args)

    handler = PCBReadWrite()

    rclpy.spin(handler)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()