# waypointControl Class Written by: Alex Roy
# Used to create the racecourse by passing commands through PCBComm,
# update the objective waypoint when you reach the end of the current leg,
# and tracking the start / end of the race

import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Bool
import json


GATE_WIDTH_METERS = 10


class waypointControl(Node):
    def __init__(self, waypoints):
        super().__init__('waypointControl')

        self.waypoints = waypoints  # list of (lat, lon)
        #if there are waypoints set, then create the waypoints from the starting waypoint
        if len(self.waypoints) > 0:
            self.origin = self.waypoints[0]
            self.meter_waypoints = [
                self._latlon_to_xy(wp) for wp in self.waypoints
            ]
        else:
            self.origin = None
            self.meter_waypoints = []
        
        self.gate_width = GATE_WIDTH_METERS
        self.latitude = 0
        self.longitude = 0
        self.wpTracker = 0
        
        
        #The current leg is the waypoint you are sailing to (0 = going to the start mark)
        self.max_laps = 1
        self.current_leg = 0
        self.lap_count = 0
        self.following_enabled = False
        self.race_started = False
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

        self.waypointCmd_subscriber = self.create_subscription(String, 'waypoint_command', self.command_callback, 10)
        self.navigationTimer = self.create_timer(0.1, self.waypoint_radius_callback)
        
        # Following waypoint command
        self.following_enabled_publisher = self.create_publisher(Bool, 'following', 10)

        self.bearingAngle = 0


    #recieve a String with JSON, convert it to a dictionary
    def command_callback(self, msg):

        try:
            DICT = json.loads(msg.data)
        except json.JSONDecodeError:
            print("Invalid waypoint command JSON")
            return
        print('this is the DICT')
        print(DICT)
        cmd = next(iter(DICT))          # get command name
        payload = DICT[cmd]

        if not isinstance(payload, list) or len(payload) == 0:
            payload = [{}]

        data = payload[0]

        if cmd == "add":
            lat = data["latitude"]
            lon = data["longitude"]
            order = data.get("order")

            if isinstance(order, int) and 0 <= order <= len(self.waypoints):
                self.waypoints.insert(order, (lat, lon))
            else:
                self.waypoints.append((lat, lon))

            if self.origin is None:
                self.origin = (lat, lon)

            self.meter_waypoints = [
                self._latlon_to_xy(wp) for wp in self.waypoints
            ]

            print(f"Waypoint added: {lat}, {lon}")


        elif cmd == "remove":

            if not self.waypoints:
                print("No waypoints to remove")
                return

            order = data.get("order")

            if isinstance(order, int) and 0 <= order < len(self.waypoints):
                removed = self.waypoints.pop(order)
            else:
                removed = self.waypoints.pop()

            print(f"Removed waypoint: {removed}")
            if self.waypoints:
                self.current_leg = min(self.current_leg, len(self.waypoints) - 1)
            else:
                self.current_leg = 0

            self.meter_waypoints = [
                self._latlon_to_xy(wp) for wp in self.waypoints
            ]
            


        elif cmd == "startFollowing":

            if not self.waypoints:
                print("No waypoints to follow")
                return
            
            self.following_enabled = True
            self.lap_count = 0
            self.race_started = False
            self.race_complete = False
            self._was_inside_gate = False
            msg = Bool()
            msg.data = True
            self.following_enabled_publisher.publish(msg)
            print("Following enabled")


        elif cmd == "stopFollowing":
            self.following_enabled = False
            msg = Bool()
            msg.data = True
            self.following_enabled_publisher.publish(msg)
            print("Following disabled")
        
        elif cmd == "setCurrentWaypoint":
            order = data.get("order")

            if isinstance(order, int) and 0 <= order < len(self.waypoints):
                self.current_leg = order
                self._was_inside_gate = False  # reset gate tracking
                print(f"Current waypoint manually set to {self.current_leg}")
            else:
                print(f"Invalid waypoint index: {order}")

        else:
            print(f"Unknown waypoint command: {cmd}")
    

    def longitude_callback(self, msg):
        self.longitude = msg.data

    def latitude_callback(self, msg):
        self.latitude = msg.data

    # Updates the WP tracker
    def waypoint_radius_callback(self):
        if not self.following_enabled:
            return

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


    # Update race state
    def update(self, boat_pos):

        if self.race_complete or len(self.waypoints) == 0:
            return False

        inside, distance = self.point_in_gate(boat_pos)
        print(f"Leg {self.current_leg} | Distance: {distance:.2f} m | Inside: {inside}")
        print("Waypoints")
        print(self.waypoints)

        if inside and not self._was_inside_gate:
            # PRE-START
            if not self.race_started and self.current_leg == 0:
                self.race_started = True
                self._advance_leg()
                print("Race started")

            # NORMAL RACING
            else:
                # If we ENTER waypoint 0 during racing,
                # that means we finished a lap.
                if self.race_started and self.current_leg == 0:

                    self.lap_count += 1
                    print(f"Lap {self.lap_count} complete")

                    if self.max_laps is not None and self.lap_count >= self.max_laps:
                        self.race_complete = True
                        print("Race complete")
                        self._was_inside_gate = True
                        return True

                self._advance_leg()
                print(f"Advanced to leg {self.current_leg}")

            self._was_inside_gate = True
            return True

        # Reset once outside gate
        if not inside:
            self._was_inside_gate = False

        return False


    def _advance_leg(self):
        self.current_leg += 1
        if self.current_leg >= len(self.waypoints):
            self.current_leg = 0


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

    #Test racecourse
    A = (44.616314, -63.549043)
    B = (44.619957, -63.548778)
    C = (44.619894, -63.557008)
    D = (44.615673, -63.557152)


    waypoints = []

    rclpy.init(args=args)

    handler = waypointControl(waypoints)

    print("Waypoint Control Runner")

    rclpy.spin(handler)

    rclpy.shutdown()


if __name__ == '__main__':
    main()


