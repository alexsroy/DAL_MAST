import serial # https://github.com/AnrdyShmrdy/ros2_serial_interface/blob/main/ros2_serial_interface/serial_server.py
import json   # https://stackoverflow.com/questions/27858041/oserror-errno-13-permission-denied-dev-ttyacm0-using-pyserial-from-pyth
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32

MANUAL_INPUT_MODE = False

class PCBReadWrite(Node):
    def __init__(self):
        super().__init__('PCBComm')

        self.PCBStr = ""

        self.ser = serial.Serial("/dev/ttyS0", 115200, timeout = 0.1) #change "ttyS0" to whatever port is being used.
        self.ser.reset_input_buffer()

        # INPUTS
        self.windAngle = 0.0 # (0, 360)

        # DEBUG OUTPUTS
        self.targetBearing = 0.0                # These are floats to be published for informative value
        self.waypointLat = 0.0                  # Could bring in more wayfinding info, like outputting the list and stuff
        self.waypointLon = 0.0

        self.headingAngle = 0.0 # (0, 360)      # Movella
        self.latitude = 0.0
        self.longitude = 0.0


        # CONTROL OUTPUTS
        self.targetSailAngle = 0.0        # (0, 360)
        self.targetRudderAngle = 0.0      # (-45, 45)
        self.targetFlapAngle = 0.0        # (-45, 45)

        # Deprecated and unused for the actual boat
        self.sailAngle = 0.0 # (0, 360)
        self.flapAngle = 0.0
        self.rudderAngle = 0.0
        # These are subscriptions to store variables from the subscriptions
        self.targetSailAngle_subscriber = self.create_subscription(Float32, 'sail_angle_target', self.sail_target_callback, 10)
        self.targetFlapAngle_subscriber = self.create_subscription(Float32, 'flap_angle_target', self.flap_target_callback, 10)
        self.targetRudderAngle_subscriber = self.create_subscription(Float32, 'rudder_angle_target', self.rudder_target_callback, 10)
        self.targetHeading_subscriber = self.create_subscription(Float32, 'heading_target_direction', self.target_heading_callback, 10)
        self.waypoint_longitude_subscription = self.create_subscription(Float32, 'waypoint_longitude', self.waypoint_longitude_callback, 10)
        self.waypoint_latitude_subscription = self.create_subscription(Float32, 'waypoint_latitude', self.waypoint_latitude_callback, 10)
        self.compass_subscription = self.create_subscription(Float32, 'heading_direction', self.heading_callback, 10)
        self.latitude_subscription = self.create_subscription(Float32, 'latitude', self.latitude_callback, 10)
        self.longitude_subscription = self.create_subscription(Float32, 'longitude', self.longitude_callback, 10)

        #self.intermediate_waypoint_longitude_subscription = self.create_subscription(Float32, 'intermediate_waypoint_longitude', self.inter_waypoint_longitude_callback, 10)
        #self.intermediate_waypoint_latitude_subscription = self.create_subscription(Float32, 'intermediate_waypoint_latitude', self.inter_waypoint_latitude_callback, 10)

        # These are publishers that are sensor data from the PCB
        self.windVane_publisher = self.create_publisher(Float32, 'wind_direction', 10)
        self.waypointCmd_publisher = self.create_publisher(String, 'waypoint_command', 10)


        # These come from the movella
        #self.compass_publisher = self.create_publisher(Float32, 'heading_direction', 10)
        #self.latitude_publisher = self.create_publisher(Float32, 'latitude', 10)
        #self.longitude_publisher = self.create_publisher(Float32, 'longitude', 10)

        # These are useless
        self.sailAngle_publisher = self.create_publisher(Float32, 'sail_angle', 10)
        self.flapAngle_publisher = self.create_publisher(Float32, 'flap_angle', 10)
        self.rudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle', 10)


        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.read_PCB)

        timer_period = 3  # seconds
        self.timer = self.create_timer(timer_period, self.writeToPCB)


    #OUTDATED: The json should be in the form of: {"latitude": 53.54, "longitude": 45.23, "sail_angle": 2.2, "flap_angle": 30.2, "rudder_angle": 11.1, "heading_angle": 145, "wind_angle": 76.0}
    # WP CMD msg should be in the form of: {"WPCmd": "add | remove", "order": "2", "latitude": 53.54, "longitude": 45.23}
    def read_PCB(self):

            if MANUAL_INPUT_MODE:
                self.PCBStr = input(">")
            else:
                # Read value from PCB

                try:
                    self.PCBStr = self.ser.readline().decode('utf-8').rstrip()
                    print(self.PCBStr)
                    #self.PCBStr = input(">")
                    DICT = json.loads(self.PCBStr)

                except Exception as err:
                    self.ser.write(bytes('{"ErrorMsg":[{"Description":"PCB String Failed to Read"}]}','utf-8'))
                else: #
                    print("read from PCB: ", self.PCBStr)
                    #self.PCBStr = "" # this is the str from the PCB

                    if "SensorInput" in DICT.keys():
                        data = DICT["SensorInput"][0]
                        print(DICT)
                        print(data["windAngle"])

                        f = Float32()
                        f.data = float(data["windAngle"])
                        self.windVane_publisher.publish(f)
                        self.windAngle = f.data

                    if "add" in DICT.keys() or "remove" in DICT.keys() or "startFollowing" in DICT.keys() or "stopFollowing" in DICT.keys():
                        s = String()
                        s.data = self.PCBStr
                        self.waypointCmd_publisher.publish(s)

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

    def latitude_callback(self, msg):
        self.latitude = msg.data

    def longitude_callback(self, msg):
        self.longitude = msg.data

    def heading_callback(self, msg):
        self.headingAngle = msg.data


    def writeToPCB(self):
        writeStr = ""
        variablesToWrite = [["targetSailAngle", self.targetSailAngle], ["targetFlapAngle", self.targetFlapAngle], ["targetRudderAngle", self.targetRudderAngle], ["targetBearing", self.targetBearing], ["waypointLon", self.waypointLon], ["waypointLat", self.waypointLat], ["headingAngle", self.headingAngle], ["latitude", self.latitude], ["longitude", self.longitude], ["windAngle", self.windAngle]]

        writeStr += '{\"TargetsOutput\":[{' + variablesToWrite[0][0] + '\": ' + str(variablesToWrite[0][1])



        for var in variablesToWrite:
            writeStr += ', \"' + var[0] + '\": ' + str(var[1])

        writeStr += '}]}'

        print(writeStr)
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


