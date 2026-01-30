
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

maxFlapDeflection = 45

class controlConfigurationService(Node):

    def __init__(self):
        super().__init__('control_configuration_node')
        self.windVane_subscription = self.create_subscription(Float32, 'wind_direction', self.wind_callback, 10)
        self.compass_subscription = self.create_subscription(Float32, 'heading_direction', self.compass_callback, 10)
        self.targetHeading_subscription = self.create_subscription(Float32, 'heading_target_direction', self.heading_target_callback, 10)

        # The inputs and outputs for this node
        self.sailAngle_subscription = self.create_subscription(Float32, 'sail_angle', self.sail_callback, 10)
        self.flapAngle_subscription = self.create_subscription(Float32, 'flap_angle', self.flap_callback, 10)
        self.rudderAngle_subscription = self.create_subscription(Float32, 'rudder_angle', self.rudder_callback, 10)

        self.targetSailAngle_publisher = self.create_publisher(Float32, 'sail_angle_target', 10)
        self.targetFlapAngle_publisher = self.create_publisher(Float32, 'flap_angle_target', 10)
        self.targetRudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle_target', 10)

        # Variables to store inputs
        self.windAngle = float(0)
        self.heading = float(0)
        self.sailAngle = float(0)
        self.flapAngle = float(0)
        self.rudderAngle = float(0)
        self.targetHeading = float(0)

        # Publication rates
        rates = [0.1, 0.1, 0.2]

        self.sailTimer = self.create_timer(rates[0], self.sail_pub_callback)
        self.flapTimer = self.create_timer(rates[1], self.flap_pub_callback)
        self.rudderTimer = self.create_timer(rates[2], self.rudder_pub_callback)

    # Store topics to class members
    def wind_callback(self, msg):
        self.windAngle = msg.data

    def compass_callback(self, msg):
        self.heading = msg.data

    def heading_target_callback(self, msg):
        self.targetHeading = msg.data

    def sail_callback(self, msg):
        self.sailAngle = msg.data

    def flap_callback(self, msg):
        self.flapAngle = msg.data

    def rudder_callback(self, msg):
        self.rudderAngle = msg.data


    # These are the callbacks that run on a timer to update the published targets
    def sail_pub_callback(self): # This one needs to be decided on and tested on for the real boat
        msg = Float32()

        if self.windAngle > 180:
            msg.data = float((self.windAngle + 8) % 360)

        else:
            msg.data = float((self.windAngle - 8) % 360)

        self.targetSailAngle_publisher.publish(msg)

    def flap_pub_callback(self):
        msg = Float32()

        """
             * If the boat is sailing into the wind, we switch the angle of flap when heading - wind angle is at zero
             * Otherwise we switch the flap angle at +/- 180 degrees, the number being positive or negative dependant on if the boat is going
             *   or down

        """
        # Sailing into the wind
        if (self.windAngle >= 0 and self.windAngle >= 0) or (self.windAngle <= 0 and self.windAngle <= 0):
            if self.windAngle - self.heading > 20:
                flapTarget = maxFlapDeflection

            elif self.windAngle - self.heading < -20:
                flapTarget = -1 * maxFlapDeflection

            else: # If we're real close to the wind
                flapTarget = -1 * maxFlapDeflection # 0

        # Sailing away from the wind
        elif self.windAngle < 0 and self.heading > 0:
            if self.windAngle - self.heading < -200:
                flapTarget = maxFlapDeflection

            elif self.windAngle - self.heading > -160:
                flapTarget = -1 * maxFlapDeflection

            else: # Jibin time
                flapTarget = -1 * maxFlapDeflection # 0

        # Sailing away from the wind
        elif self.windAngle > 0 and self.heading < 0:
            if self.windAngle - self.heading > 200:
                flapTarget = -1 * maxFlapDeflection

            elif self.windAngle - self.heading < 160:
                flapTarget = maxFlapDeflection

            else: # Jibin time
                flapTarget = -1 * maxFlapDeflection # 0

        #global wp
        #if ((self.x - wp.x) ** 2 + (self.y - wp.y) ** 2) ** 0.5 < wp.rad:
        #    self.flapTarget = 0
        msg.data = float(flapTarget)
        self.targetFlapAngle_publisher.publish(msg)

    def rudder_pub_callback(self):
        msg = Float32()

        #print("heading: ", self.heading, "course: ", self.targetHeading)

        if self.heading - self.targetHeading > 0:
            rudderTarget = -1 * max(-0.5 * (self.heading - self.targetHeading), -45)
        else:
            rudderTarget = -1 * min(-0.5 * (self.heading - self.targetHeading), 45)

        msg.data = float(rudderTarget)
        self.targetRudderAngle_publisher.publish(msg)



    def voidCallback(self):
        pass

def main():
    rclpy.init()

    control_service = controlConfigurationService()

    rclpy.spin(control_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

