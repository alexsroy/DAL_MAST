
# change ROS
#removefminm
import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32
import json



GATE_WIDTH_METERS = 10



class waypointControl(Node):
    def __init__(self, waypoints):
        super().__init__('waypointControl')

        # Changed waypoint list to actual list instead of dictionary
        self.waypoints = waypoints  # list of (lat, lon)
        self.meter_waypoints = []
        self.origin = None
        self.race_started = False

        self.current_leg = 0

        # This is
        self.max_laps = 1
        self.lap_count = 0

        self.latitude = 0
        self.longitude = 0
        self.wpTracker = 0
        self.gate_width = GATE_WIDTH_METERS
        self.race_complete = False
        self._was_inside_gate = False
        
        

        #Next waypoint coords
        self.waypoint_latitude_publisher = self.create_publisher(Float32, 'waypoint_latitude', 10)
        self.waypoint_longitude_publisher = self.create_publisher(Float32, 'waypoint_longitude', 10)
        #Previous waypoint coords
        self.prevWaypoint_latitude_publisher = self.create_publisher(Float32, 'previous_waypoint_latitude', 10)
        self.prevWaypoint_longitude_publisher = self.create_publisher(Float32, 'previous_waypoint_longitude', 10)

        self.longitude_subscription = self.create_subscription(Float32, 'longitude', self.longitude_callback, 10)
        self.latitude_subscription = self.create_subscription(Float32, 'latitude', self.latitude_callback, 10)

        self.waypointCMD_subscriber = self.create_subscription(String, 'waypoint_command', self.command_callback, 10)
        self.navigationTimer = self.create_timer(1.0, self.waypoint_radius_callback)

        self.bearingAngle = 0
        print("yooooooo")


    def command_callback(self, msg):
        DICT = json.loads(msg.data)

        if DICT["WPcmd"] == "add":
            lat = DICT["latitude"]
            lon = DICT["longitude"]

            self.waypoints.append((lat, lon))

            if self.origin is None:
                self.origin = (lat, lon)

            self.meter_waypoints = [
                self._latlon_to_xy(wp) for wp in self.waypoints
            ]

            print(f"Waypoint added: {lat}, {lon}")

        elif DICT["WPcmd"] == "clear":
            self.waypoints = []
            self.meter_waypoints = []
            self.origin = None
            self.current_leg = 0
            self.race_started = False

    def longitude_callback(self, msg):
        self.longitude = msg.data

    def latitude_callback(self, msg):
        self.latitude = msg.data

    # Updates the WP tracker
    def waypoint_radius_callback(self):

        if len(self.waypoints) == 0:
            return

        boat_pos = (self.latitude, self.longitude)

        triggered = self.update(boat_pos)

        if triggered:
            print("Entered waypoint gate")

        if self.race_complete:
            return

        # Publish current and previous waypoint
        target = self.waypoints[self.current_leg]
        prev_index = (self.current_leg - 1) % len(self.waypoints)
        prev_wp = self.waypoints[prev_index]

        msg = Float32()

        msg.data = float(target[0])
        self.waypoint_latitude_publisher.publish(msg)

        msg.data = float(target[1])
        self.waypoint_longitude_publisher.publish(msg)

        msg.data = float(prev_wp[0])
        self.prevWaypoint_latitude_publisher.publish(msg)

        msg.data = float(prev_wp[1])
        self.prevWaypoint_longitude_publisher.publish(msg)


    def _latlon_to_xy(self, wp):
        lat, lon = wp
        ref_lat, ref_lon = self.origin

        R = 6371008  # Earth radius (m)

        dlat = math.radians(lat - ref_lat)
        dlon = math.radians(lon - ref_lon)

        x = dlon * R * math.cos(math.radians(ref_lat))
        y = dlat * R

        return (x, y)

    def point_in_gate(self, boat_pos):

        if len(self.meter_waypoints) == 0:
            return False, 0.0

        boat_xy = self._latlon_to_xy(boat_pos)

        B = self.meter_waypoints[self.current_leg]

        dx = boat_xy[0] - B[0]
        dy = boat_xy[1] - B[1]

        distance = math.hypot(dx, dy)

        inside = distance <= (self.gate_width / 2.0)

        return inside, distance

    # -------------------------
    # Update race state
    # -------------------------

    def update(self, boat_pos):
        print('in update function')
        print(f'here is the latitude, longitude {self.latitude}, {self.longitude}')
        print(f'boat pos: {boat_pos}')
        if self.race_complete or len(self.waypoints) == 0:
            return False

        inside, distance = self.point_in_gate(boat_pos)

        if inside and not self._was_inside_gate:

            if not self.race_started:
                self._advance_leg()
                self.race_started = True
                print('race started')

            else:
                self._advance_leg()
                print(f"Advanced to leg {self.current_leg}")

            self._was_inside_gate = True
            return True

        if not inside:
            self._was_inside_gate = False

        return False


    def _advance_leg(self):
        self.current_leg += 1

        if self.current_leg >= len(self.waypoints):
            self.current_leg = 0
            self.lap_count += 1

            print(f"Lap {self.lap_count} complete")

            if self.max_laps is not None and self.lap_count >= self.max_laps:
                self.race_complete = True
                print("Race complete")

    # -------------------------
    # Info helpers
    # -------------------------

    def current_leg_info(self, boat_pos=None):
        if self.race_complete:
            return None

        # PRE-START
        if not self.race_started:
            start_wp = self.waypoints[0]

            return "PRESTART", boat_pos, start_wp

        # NORMAL RACING
        target = self.waypoints[self.current_leg]
        prev_index = (self.current_leg - 1) % len(self.waypoints)
        prev_wp = self.waypoints[prev_index]

        return self.current_leg, prev_wp, target
    
    def current_target(self):
        if self.race_complete:
            return None
        return self.waypoints[self.current_leg]



def main(args=None):
    # Main loop

    #racecourse
    A = (44.616314, -63.549043)
    B = (44.619957, -63.548778)
    C = (44.619894, -63.557008)
    D = (44.615673, -63.557152)


    waypoints = [A, B, C, D]

    rclpy.init(args=args)

    handler = waypointControl(waypoints)

    print("Waypoint Control Test Runner")

    rclpy.spin(handler)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


