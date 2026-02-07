# 90% sure this is untested code.

# change ROS
#removefminm
import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32
import json


# waht is D?
D = 0.0005

#BB = Bounding Box
BBReverseSpace = 2

def calcTriArea(A, B, C):
    return abs((B[0] * A[1] - A[0] * B[1]) + (C[0] * B[1] - C[1] * B[0]) + (A[0] * C[1] - A[1] * C[0])) / 2

# This line of code may need a magic number tbh to make sure that we are certain the boat is out of the the BB
def pointInRect(self, point, BB): # https://stackoverflow.com/questions/17136084/checking-if-a-point-is-inside-a-rotated-rectangle
    return calcTriArea(BB[0], point, BB[3]) + calcTriArea(BB[3], point, BB[2]) + calcTriArea(BB[2], point, BB[1]) + calcTriArea(BB[0], point, BB[1]) <= D * (abs(BB[0][0] - BB[3][0]) / (math.cos(math.radians(self.bearingAngle)) + 0.000000000000000001))


class waypointControl(Node):
    def __init__(self):
        super().__init__('WaypointCTRL')

        # Changed waypoint list to actual list instead of dictionary
        self.waypointList = []

        self.latitude = 0
        self.longitude = 0
        self.wpTracker = 0

        self.waypoint_latitude_publisher = self.create_publisher(Float32, 'waypoint_latitude', 10)
        self.waypoint_longitude_publisher = self.create_publisher(Float32, 'waypoint_longitude', 10)
        self.prevWaypoint_latitude_publisher = self.create_publisher(Float32, 'previous_waypoint_latitude', 10)
        self.prevWaypoint_longitude_publisher = self.create_publisher(Float32, 'previous_waypoint_longitude', 10)

        self.longitude_subscription = self.create_subscription(Float32, 'longitude', self.longitude_callback, 10)
        self.latitude_subscription = self.create_subscription(Float32, 'latitude', self.latitude_callback, 10)

        self.waypointCMD_subscriber = self.create_subscription(String, 'waypoint_command', self.command_callback, 10)

        self.navigationTimer = self.create_timer(0.1, self.waypoint_radius_callback)

        self.bearingAngle = 0


    def command_callback(self, msg):
        DICT = json.loads(msg.data)

        if DICT["WPcmd"] == "add":
            # If you mis-type a waypoint, say it's in the 4th position instead of the 3rd position, it will fill both the 3rd and 4th position
            # with the same waypoint
            self.waypointList[str(DICT["order"])] = [DICT["longitude"], DICT["latitude"]]

        if DICT["WPcmd"] == "remove":
            self.waypointList.pop(DICT["order"], None)

    def longitude_callback(self, msg):
        self.longitude = msg.data

    def latitude_callback(self, msg):
        self.latitude = msg.data

    # Updates the WP tracker
    def waypoint_radius_callback(self):
        nextWP = self.waypointList[(self.wpTracker + 1) % len(self.waypointList)] # These are the waypoints we care about in order, we need 2 of them
        currWP = self.waypointList[(self.wpTracker + 0) % len(self.waypointList)] # in order to make a BB, so by definition, we need at least 4 WPs
        prevWP = self.waypointList[(self.wpTracker - 1) % len(self.waypointList)]
        doublePrevWP = self.waypointList[(self.wpTracker - 2) % len(self.waypointList)]

        # If in the next BB
        if self.inBB(currWP, nextWP):
            self.wpTracker += 1

        # If in the BB we expect
        elif self.inBB(prevWP, currWP):
            pass

        # If in the previous BB
        if self.inBB(doublePrevWP, prevWP):
            self.wpTracker -= 1

        # Publish the lats and lons for the WP
        f = Float32()
        f.data = float(self.waypointList[(self.wpTracker + 0) % len(self.wpTracker)][0])
        self.waypoint_longitude_publisher.publish(f)

        f.data = float(self.waypointList[(self.wpTracker + 0) % len(self.wpTracker)][1])
        self.waypoint_latitude_publisher.publish(f)

        f.data = float(self.waypointList[(self.wpTracker - 1) % len(self.wpTracker)][0])
        self.prevWaypoint_longitude_publisher.publish(f)

        f.data = float(self.waypointList[(self.wpTracker - 1) % len(self.wpTracker)][1])
        self.prevWaypoint_latitude_publisher.publish(f)

    def inBB(self, prevWP, nextWP):
        bearingAngle = math.degrees(math.atan2(nextWP[1] - prevWP[1], nextWP[0] - prevWP[0]))
        bearing = [(prevWP[0] - BBReverseSpace * math.cos(math.radians(bearingAngle)), prevWP[1] - BBReverseSpace * math.sin(math.radians(bearingAngle))), (nextWP[0], nextWP[1])]

        APlus = [D / 2 * math.cos(math.radians(bearingAngle + 90)) + bearing[0][0], D / 2 * math.sin(math.radians(bearingAngle + 90)) + bearing[0][1]]
        AMinus = [D / 2 * math.cos(math.radians(bearingAngle - 90)) + bearing[0][0], D / 2 * math.sin(math.radians(bearingAngle - 90)) + bearing[0][1]]
        BPlus = [D / 2 * math.cos(math.radians(self.bearingAngle + 90)) + bearing[1][0], D / 2 * math.sin(math.radians(self.bearingAngle + 90)) + bearing[1][1]]
        BMinus = [D / 2 * math.cos(math.radians(self.bearingAngle - 90)) + bearing[1][0], D / 2 * math.sin(math.radians(self.bearingAngle - 90)) + bearing[1][1]]

        boundingBox = [APlus, AMinus, BMinus, BPlus]

        return self.pointInRect((self.longitude, self.latitude), boundingBox)

def main(args=None):
    # Main loop
    #print(getCourse)

    rclpy.init(args=args)

    handler = waypointControl()

    rclpy.spin(handler)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


