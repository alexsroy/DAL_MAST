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
# D is the bounding box FULL width in meters (half on each side of the bearing line)
D = 100  # metres — was wrongly set to 1000 "pixels" but nav operates in GPS→metres space

BBReverseSpace = 30  # metres behind the previous WP that the corridor starts


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

        # --- Convert all GPS inputs to a flat-earth metre coordinate system ---
        # Use the previous waypoint as the local origin so numbers stay small and
        # the geometry is identical to what the sim does in boatClasses.py.
        R = 6371000.0  # Earth radius in metres
        ref_lat = self.prevWaypointLatitude if self.prevWaypointLatitude != 0 else self.waypointLatitude
        ref_lon = self.prevWaypointLongitude if self.prevWaypointLongitude != 0 else self.waypointLongitude
        ref_lat_rad = math.radians(ref_lat)

        def gps_to_m(lat, lon):
            """Flat-earth GPS → local metres, origin = prev waypoint."""
            x =  math.radians(lon - ref_lon) * R * math.cos(ref_lat_rad)
            y = -math.radians(lat - ref_lat) * R   # negate: north = -y in pygame screen space
            return x, y

        # All positions in metres relative to prev waypoint origin
        boat_x,    boat_y    = gps_to_m(self.latitude,           self.longitude)
        wp_x,      wp_y      = gps_to_m(self.waypointLatitude,   self.waypointLongitude)
        prev_wp_x, prev_wp_y = gps_to_m(self.prevWaypointLatitude, self.prevWaypointLongitude)

        # Guard: if waypoints are the same point (startup / not yet received) do nothing
        dx = wp_x - prev_wp_x
        dy = wp_y - prev_wp_y
        if abs(dx) < 0.01 and abs(dy) < 0.01:
            self.get_logger().warn("Waypoint and previous waypoint are the same — waiting for valid waypoints")
            return

        # --- Bearing angle in the metre coordinate system ---
        self.bearingAngle = math.degrees(math.atan2(dy, dx))

        # Corridor start: slightly behind the previous waypoint along the bearing
        b0x = prev_wp_x - BBReverseSpace * math.cos(math.radians(self.bearingAngle))
        b0y = prev_wp_y - BBReverseSpace * math.sin(math.radians(self.bearingAngle))
        b1x = wp_x
        b1y = wp_y

        # Store in the old format for any subscribers that still use it (GPS space)
        self.bearing = [
            (self.prevWaypointLongitude, self.prevWaypointLatitude),
            (self.waypointLongitude,     self.waypointLatitude)
        ]

        f = Float32()
        f.data = float(self.bearingAngle)
        self.bearingAngle_publisher.publish(f)

        f = Float32MultiArray()
        f.data = [self.bearing[0][0], self.bearing[0][1], self.bearing[1][0], self.bearing[1][1]]
        self.bearing_publisher.publish(f)

        # --- Bounding box corners in metre space ---
        ang_rad = math.radians(self.bearingAngle)
        cos90 =  math.cos(ang_rad + math.radians(90))
        sin90 =  math.sin(ang_rad + math.radians(90))
        half = D / 2.0

        APlus  = [b0x + half * cos90, b0y + half * sin90]
        AMinus = [b0x - half * cos90, b0y - half * sin90]
        BPlus  = [b1x + half * cos90, b1y + half * sin90]
        BMinus = [b1x - half * cos90, b1y - half * sin90]

        boundingBox = [APlus, AMinus, BMinus, BPlus]  # same winding as before

        # Debug publish (now in metres relative to prev WP origin — label it clearly)
        bbcoords = String()
        bbcoords.data = (f"[metres from prev WP]\n"
                         f"APlus:  ({APlus[0]:.1f}, {APlus[1]:.1f})\n"
                         f"AMinus: ({AMinus[0]:.1f}, {AMinus[1]:.1f})\n"
                         f"BPlus:  ({BPlus[0]:.1f}, {BPlus[1]:.1f})\n"
                         f"BMinus: ({BMinus[0]:.1f}, {BMinus[1]:.1f})\n"
                         f"boat:   ({boat_x:.1f}, {boat_y:.1f})\n"
                         f"bearingAngle: {self.bearingAngle:.1f} deg")
        print(bbcoords.data)

        print(
            f"wind={self.windAngle:.1f} heading={self.heading:.1f} "
            f"boat=({boat_x:.1f},{boat_y:.1f}) wp=({wp_x:.1f},{wp_y:.1f}) "
            f"bearing={self.bearingAngle:.1f}"
        )

        # --- In-BB check (all in metre space now — D is meaningful) ---
        in_bb = self.pointInRect((boat_x, boat_y), boundingBox)
        wind_to_bearing = abs(self.shortestAngle(self.windAngle, self.bearingAngle))

        self.get_logger().info(f"in_BB={in_bb}  wind_to_bearing={wind_to_bearing:.1f}  heading={self.heading:.1f}  target={self.headingTarget:.1f}")

        if in_bb:
            if abs(self.shortestAngle(self.windAngle, self.bearingAngle)) < self.TACKING_ANGLE:
                # If tacking
                vector1 = [math.cos(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle + self.TACKING_ANGLE))), math.sin(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle + self.TACKING_ANGLE)))]
                vector2 = [math.cos(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle - self.TACKING_ANGLE))), math.sin(math.radians(self.shortestAngle(self.bearingAngle, self.windAngle - self.TACKING_ANGLE)))]

                # publish the fact that we're tacking
                navstate = String()
                navstate.data = "tacking"
                self.nav_state.publish(navstate)

                # c = sqrt a squared + b squared
                BBLen = math.sqrt((b1x - b0x)**2 + (b1y - b0y)**2)
                upperBnd = D / 2
                lowerBnd = -D / 2

                # Rotate the coordinate grid to align with the bearing axis (metre space)
                # Translate relative to b0 (corridor start), then rotate by -bearingAngle
                rx = boat_x - b0x
                ry = boat_y - b0y
                cos_b = math.cos(math.radians(-self.bearingAngle))
                sin_b = math.sin(math.radians(-self.bearingAngle))
                boatPosition = [rx * cos_b - ry * sin_b, rx * sin_b + ry * cos_b]

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

            # y = mx + b through the bearing line (metre space)
            # Check which side of the bearing line the boat is on
            slope = math.tan(math.radians(self.bearingAngle))
            intercept = b0y - slope * b0x  # line passes through b0

            targetY = slope * boat_x + intercept

            BBReturnHeading = 0
            if boat_y >= targetY:
                BBReturnHeading = ((self.bearingAngle >= 90 and self.bearingAngle <= 270) * (self.bearingAngle + 45) + (self.bearingAngle < 90 or self.bearingAngle > 270) * (self.bearingAngle - 45)) % 360
            else:
                BBReturnHeading = ((self.bearingAngle >= 90 and self.bearingAngle <= 270) * (self.bearingAngle - 45) + (self.bearingAngle < 90 or self.bearingAngle > 270) * (self.bearingAngle + 45)) % 360


            # Now w need to do a check against the wind direction.
            # If the wind is against the return heading, we want to take the leg closest to the return heading. At worst it will be 45 degrees off
            # which will either turn the boat directly into the BB, or sail it alongside the BB.
            # The two legs of the tack can be described as (windAngle +/- tacking_angle) % 360
            if abs(self.shortestAngle(self.windAngle, BBReturnHeading)) < self.TACKING_ANGLE:
                print("BB: ", BBReturnHeading, "\n", "LHS: ", self.shortestAngle(self.windAngle + self.TACKING_ANGLE, self.bearingAngle), "\n", "RHS", self.shortestAngle(self.windAngle - self.TACKING_ANGLE, self.bearingAngle))
                print("WIND:", self.windAngle, "\n", "BEARING: ", self.bearingAngle, "\n", "TACKING DIST: ", self.TACKING_ANGLE)
                if abs(self.shortestAngle(self.windAngle + self.TACKING_ANGLE, BBReturnHeading)) < abs(self.shortestAngle(self.windAngle - self.TACKING_ANGLE, BBReturnHeading)):
                    BBReturnHeading = (self.windAngle + self.TACKING_ANGLE) % 360

                else:
                    BBReturnHeading = (self.windAngle - self.TACKING_ANGLE) % 360

            self.headingTarget = BBReturnHeading


        # Finally make sure to publish the target heading lolololol
        f = Float32()
        #print(type(f.data), "    tt    ", type(self.headingTarget))
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

    def pointInRect(self, point, BB):
        # Sum of the 4 triangles formed with the point should equal the rectangle area if inside.
        # All coordinates are now in metres so the comparison is valid.
        # https://stackoverflow.com/questions/17136084/checking-if-a-point-is-inside-a-rotated-rectangle
        rect_area = (self.calcTriArea(BB[0], BB[1], BB[2]) + self.calcTriArea(BB[0], BB[2], BB[3]))
        tri_sum = (self.calcTriArea(BB[0], point, BB[3]) +
                   self.calcTriArea(BB[3], point, BB[2]) +
                   self.calcTriArea(BB[2], point, BB[1]) +
                   self.calcTriArea(BB[0], point, BB[1]))
        return tri_sum <= rect_area + 0.01  # small epsilon for floating point


def main():
    rclpy.init()

    control_service = navigationNode()

    rclpy.spin(control_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

