from pathlib import Path
import sys
import time
import os

# for resolving file paths in ros2
from ament_index_python.packages import get_package_share_directory

import rclpy
from rclpy.node import Node
import math

from std_msgs.msg import Float32, Float32MultiArray, String

maxFlapDeflection = 45

# If you change this variable, change the one in waypoint control.py
# Set to 100 pixels for simulator, change to 0.0005 for real GPS coordinates
D = 2000 # Tacking box width in pixel space

BBReverseSpace = 2 # Behind the previous WP distance of BB


def convToHudCords(num, isX):
    return num / 10 + isX * 150 + (1 - isX) * 50

class navigationNode(Node):

    def __init__(self):
        super().__init__('control_configuration_node')
        self.windVane_subscription = self.create_subscription(Float32, 'wind_direction', self.wind_callback, 10)
        self.compass_subscription = self.create_subscription(Float32, 'heading_direction', self.compass_callback, 10)
        self.longitude_subscription = self.create_subscription(Float32, 'longitude', self.longitude_callback, 10)
        self.latitude_subscription = self.create_subscription(Float32, 'latitude', self.latitude_callback, 10)
        self.waypoint_longitude_subscription = self.create_subscription(Float32, 'waypoint_longitude', self.waypoint_longitude_callback, 10)
        self.waypoint_latitude_subscription = self.create_subscription(Float32, 'waypoint_latitude', self.waypoint_latitude_callback, 10)
        self.prevWaypoint_longitude_subscription = self.create_subscription(Float32, 'previous_waypoint_longitude', self.previous_waypoint_longitude_callback, 10)
        self.prevWaypoint_latitude_subscription = self.create_subscription(Float32, 'previous_waypoint_latitude', self.previous_waypoint_latitude_callback, 10)

        # The inputs and outputs for this node
        self.targetHeading_publisher = self.create_publisher(Float32, 'heading_target_direction', 10)
        self.bearing_publisher = self.create_publisher(Float32MultiArray, 'bearing', 10)
        self.bearingAngle_publisher = self.create_publisher(Float32, 'bearing_angle', 10)
        self.nav_state = self.create_publisher(String, 'nav_state', 10)
        self.bb_coords = self.create_publisher(String, 'bb_coords', 10)

        # Calculated variables
        self.counter = 0
        self.bearingAngle = 0
        self.bearing = ((0, 0), (0, 0))
        self.TACKING_ANGLE = 40
        self.HEADING_TOLERANCE = 5
        #self.BBReverseSpace = 2
        self.heading = 0
        self.headingTarget = 0
        self.tacking = 0
        self.changingTack = 0

        # Variables to store inputs for navigation
        self.longitude = 0
        self.latitude = 0
        self.waypointLongitude = 0
        self.waypointLatitude = 0

        self.prevWaypointLongitude = 0
        self.prevWaypointLatitude = 0

        # Variables to store inputs COPY FROM CONTROLS
        self.windAngle = 0


        self.sailAngle = 0
        self.flapAngle = 0
        self.rudderAngle = 0


        # Publication rates
        #self.target_heading_pub_callback()
        #self.bearing_to_waypoint_callback()

        self.navigationTimer = self.create_timer(0.1, self.bearing_to_waypoint_callback)


    def longitude_callback(self, msg):
        self.longitude = msg.data

    def latitude_callback(self, msg):
        self.latitude = msg.data

    def waypoint_longitude_callback(self, msg):
        self.waypointLongitude = msg.data

    def waypoint_latitude_callback(self, msg):
        self.waypointLatitude = msg.data

    def previous_waypoint_longitude_callback(self, msg):
        self.prevWaypointLongitude = msg.data

    def previous_waypoint_latitude_callback(self, msg):
        self.prevWaypointLatitude = msg.data

    def wind_callback(self, msg):
        self.windAngle = msg.data

    def compass_callback(self, msg):
        self.heading = msg.data

    def bearing_to_waypoint_callback(self):
        # Get bearing
        self.bearingAngle = math.degrees(math.atan2(self.waypointLatitude - self.prevWaypointLatitude, self.waypointLongitude - self.prevWaypointLongitude))
        self.bearing = [(self.prevWaypointLongitude - BBReverseSpace * math.cos(math.radians(self.bearingAngle)), self.prevWaypointLatitude - BBReverseSpace * math.sin(math.radians(self.bearingAngle))), (self.waypointLongitude, self.waypointLatitude)]

        f = Float32()
        f.data = float(self.bearingAngle)
        self.bearingAngle_publisher.publish(f)

        f = Float32MultiArray()
        f.data = [self.bearing[0][0], self.bearing[0][1], self.bearing[1][0], self.bearing[1][1]]
        self.bearing_publisher.publish(f)

        # By this point the bearing between previous and target waypoint is calculated

        APlus = [D / 2 * math.cos(math.radians(self.bearingAngle + 90)) + self.bearing[0][0], D / 2 * math.sin(math.radians(self.bearingAngle + 90)) + self.bearing[0][1]]
        AMinus = [D / 2 * math.cos(math.radians(self.bearingAngle - 90)) + self.bearing[0][0], D / 2 * math.sin(math.radians(self.bearingAngle - 90)) + self.bearing[0][1]]
        BPlus = [D / 2 * math.cos(math.radians(self.bearingAngle + 90)) + self.waypointLongitude, D / 2 * math.sin(math.radians(self.bearingAngle + 90)) + self.waypointLatitude]
        BMinus = [D / 2 * math.cos(math.radians(self.bearingAngle - 90)) + self.waypointLongitude, D / 2 * math.sin(math.radians(self.bearingAngle - 90)) + self.waypointLatitude]

        boundingBox = [APlus, AMinus, BMinus, BPlus]

        # publishing the bb coords for debug
        bbcoords = String()
        bbcoords.data = (f"\nAPlus:  ({APlus[0]:.2f}, {APlus[1]:.2f})\n"
                        f"AMinus: ({AMinus[0]:.2f}, {AMinus[1]:.2f})\n"
                        f"BPlus:  ({BPlus[0]:.2f}, {BPlus[1]:.2f})\n"
                        f"BMinus: ({BMinus[0]:.2f}, {BMinus[1]:.2f})")
        self.bb_coords.publish(bbcoords)

        # Check if boat is in BB
        if self.pointInRect((self.longitude, self.latitude), boundingBox):
            if abs(self.shortestAngle(self.windAngle, self.bearingAngle)) < self.TACKING_ANGLE:
                # If tacking
                vector1 = [math.cos(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle + self.TACKING_ANGLE))), math.sin(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle + self.TACKING_ANGLE)))]
                vector2 = [math.cos(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle - self.TACKING_ANGLE))), math.sin(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle - self.TACKING_ANGLE)))]

                # publish the fact that we're tacking
                navstate = String()
                navstate.data = "tacking"
                self.nav_state.publish(navstate)

                # c = sqrt a squared + b squared
                BBLen = ((self.bearing[1][0] - self.bearing[0][0]) ** 2 + (self.bearing[1][1] - self.bearing[0][1]) ** 2) ** 0.5
                upperBnd = D / 2
                lowerBnd = - D / 2

                # Rotate the co-ordinate grid to align with the bearing's point away from the WP
                # https://en.wikipedia.org/wiki/Rotation_matrix

                # Start by translating then rotating, where x and y are the variables to feed the LP
                # https://academo.org/demos/rotation-about-point/
                x = self.longitude - self.bearing[0][0]
                y = self.latitude - self.bearing[0][1]
                boatPosition = [x * math.cos(math.radians(-self.bearingAngle)) - y * math.sin(math.radians(-self.bearingAngle)), x * math.sin(math.radians(-self.bearingAngle)) + y * math.cos(math.radians(-self.bearingAngle))]

                replacements = {
                    "~" : upperBnd,
                    "@" : BBLen,
                    "^" : boatPosition[0],
                    "&" : boatPosition[1],
                    "!" : vector1[0], # NOTE in the LP it's organized by X components as one parameter, and Y components as another
                    "?" : vector1[1], # Read the LP carefully
                    "$" : vector2[0],
                    "%" : vector2[1]
                }

                # getting the nav template path properly for ros2
                package_share_directory = get_package_share_directory('py_tut')
                nav_template_path = os.path.join(package_share_directory, 'navigationTemplate.mod')

                # Take the template, and replace our special characters with the values stored in the dict above
                template = Path(nav_template_path).read_text()
                for character in replacements:
                    template = template.replace(character, str(replacements[character]))

                # Write to a .mod file and then run using GLPK, and output result to output.txt
                with open("temp.mod", "w") as text_file:
                    text_file.write(template)
                os.system('glpsol --math temp.mod > output.txt') # Removed comment that Andrew found scary, it's just bash


                # Once operating system returns value, read output file to a variable
                results = Path('output.txt').read_text()

                if "PROBLEM HAS NO PRIMAL FEASIBLE SOLUTION" in results: # Pick a direction (changes every minutes) to tack to if the LP fails
                    self.headingTarget = self.windAngle + (45 * (time.time() // 60 % 2) - 45 * (1 - time.time() // 60 % 2))

                else:
                    # Parsing the output to see which direction has a non-zero value first
                    temp = results.split("magDir1")[1:-1]
                    counter1 = 0
                    for entry in temp:
                        if entry.split(" ")[-1][0] != '0':
                            break
                        else:
                            counter1 += 1

                    temp = results.split("magDir2")[1:-1]
                    counter2 = 0
                    for entry in temp:
                        if entry.split(" ")[-1][0] != '0':
                            break
                        else:
                            counter2 += 1

                    if counter1 < counter2:
                        self.headingTarget = (self.windAngle + self.TACKING_ANGLE) % 360
                    else:
                        self.headingTarget = (self.windAngle - self.TACKING_ANGLE) % 360

            else:
                # Straight sailing (very mathematically complex)
                # update: changed to bearing angle

                # publish the fact that we're straight sailing
                navstate = String()
                navstate.data = "straight sailing"
                self.nav_state.publish(navstate)

                self.headingTarget = self.bearingAngle

        # If boat is out of the BB
        else:

            # publish the fact that we're out of the bounding box
            navstate = String()
            navstate.data = "out of BB"
            self.nav_state.publish(navstate)

            slope = math.tan(math.radians(self.bearingAngle))
            intercept = self.bearing[0][1]

            # y = mx + b, and we check whether the boat is above or below it.
            # If we are greater than y, we want to set course for bearing - 45 and if we're above it we want to set heading for bearing + 45
            # this will give us the heading to intercept the bounding box again
            # The quadrent inverter flips the direction of the return BB heading based upon the direction we're trying to sail in.
            # Quadrents 2 and 3 need to reverse the direction we're trying to get do dependant on if we're above or below the line
            targetLatitude = slope * self.longitude + intercept

            BBReturnHeading = 0
            if self.latitude >= targetLatitude: # Basically to sail back to the BB, we need to sail back to it at a 45 degree angle.
                #                                 If we are above the line, we need to take the bearing and add 45 degrees, only in quadrents 2 and 3
                #                                 in quadrents 1 and 4, we subtract 45 degrees
                BBReturnHeading = ((self.bearingAngle >= 90 and self.bearingAngle <= 270) * (self.bearingAngle + 45) + (self.bearingAngle < 90 or self.bearingAngle > 270) * (self.bearingAngle - 45)) % 360
            else:                               # If we are below, we reverse the logic and subtract 45 in quadrents 2 and 3
                BBReturnHeading = ((self.bearingAngle >= 90 and self.bearingAngle <= 270) * (self.bearingAngle - 45) + (self.bearingAngle < 90 or self.bearingAngle > 270) * (self.bearingAngle + 45)) % 360
                

            # Now w need to do a check against the wind direction.
            # If the wind is against the return heading, we want to take the leg closest to the return heading. At worst it will be 45 degrees off
            # which will either turn the boat directly into the BB, or sail it alongside the BB.
            # The two legs of the tack can be described as (windAngle +/- tacking_angle) % 360
            if abs(self.shortestAngle(self.windAngle, BBReturnHeading)) < self.TACKING_ANGLE:
                BBReturnHeading = min(abs(self.shortestAngle(BBReturnHeading, (self.windAngle + self.TACKING_ANGLE) % 360)),
                abs(self.shortestAngle(BBReturnHeading, (self.windAngle - self.TACKING_ANGLE) % 360)))

            self.headingTarget = BBReturnHeading

        # Finally make sure to publish the target heading lolololol
        f = Float32()
        print(type(f.data), "    tt    ", type(self.headingTarget))
        f.data = float(self.headingTarget)
        self.targetHeading_publisher.publish(f)


    # This returns the shortest angle between two directions, where positive indicates the target is counter clockwise of the reference angle.
    # This also accounts for crossing the positive x axis
    def shortestAngle(self, referenceAngle, targetAngle):
        returnAngle = referenceAngle - targetAngle

        if returnAngle < -180:
            returnAngle = 360 - (targetAngle - referenceAngle)

        if returnAngle > 180:
            returnAngle = (360 - (referenceAngle - targetAngle)) * -1

        return returnAngle

    def voidCallback(self):
        pass

    # If you change either of these functions, make sure to change the one in waypointCtrl.py
    def calcTriArea(self, A, B, C):
        return abs((B[0] * A[1] - A[0] * B[1]) + (C[0] * B[1] - C[1] * B[0]) + (A[0] * C[1] - A[1] * C[0])) / 2

    # This line of code may need a magic number tbh to make sure that we are certain the boat is out of the the BB
    def pointInRect(self, point, BB): # https://stackoverflow.com/questions/17136084/checking-if-a-point-is-inside-a-rotated-rectangle
        return self.calcTriArea(BB[0], point, BB[3]) + self.calcTriArea(BB[3], point, BB[2]) + self.calcTriArea(BB[2], point, BB[1]) + self.calcTriArea(BB[0], point, BB[1]) <= D * (abs(BB[0][0] - BB[3][0]) / (math.cos(math.radians(self.bearingAngle)) + 0.000000000000000001))


def main():
    rclpy.init()

    control_service = navigationNode()

    rclpy.spin(control_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

