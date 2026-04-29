import rclpy

from rclpy.node import Node

from std_msgs.msg import Bool, Float32

maxFlapDeflection = 45
thrust_sail_offset = 57         #this
angle_of_attack = 8             #this

def shortestAngle(referenceAngle, targetAngle):
    returnAngle = referenceAngle - targetAngle

    if returnAngle < -180:
        returnAngle = 360 - (targetAngle - referenceAngle)

    if returnAngle > 180:
        returnAngle = (360 - (referenceAngle - targetAngle)) * -1

    return returnAngle



class controlConfigurationService(Node):

    def __init__(self):
        super().__init__('control_configuration_node')
        self.windVane_subscription = self.create_subscription(Float32, 'wind_direction', self.wind_callback, 10)
        self.compass_subscription = self.create_subscription(Float32, 'heading_direction', self.compass_callback, 10)
        self.targetHeading_subscription = self.create_subscription(Float32, 'heading_target_direction', self.heading_target_callback, 10)
        self.following_subscription = self.create_subscription(Bool, 'following', self.following_callback, 10)

        # The inputs and outputs for this node
        self.sailAngle_subscription = self.create_subscription(Float32, 'sail_angle', self.sail_callback, 10)
        self.flapAngle_subscription = self.create_subscription(Float32, 'flap_angle', self.flap_callback, 10)
        self.rudderAngle_subscription = self.create_subscription(Float32, 'rudder_angle', self.rudder_callback, 10)

        self.targetSailAngle_publisher = self.create_publisher(Float32, 'sail_angle_target', 10)
        self.targetFlapAngle_publisher = self.create_publisher(Float32, 'flap_angle_target', 10)
        self.targetRudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle_target', 10)         #this

        # Variables to store inputs
        self.windAngle = float(0)
        self.heading = float(0)
        self.sailAngle = float(0)
        self.flapAngle = float(0)
        self.rudderAngle = float(0)
        self.targetHeading = float(0)
        self.following = False

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

    def following_callback(self, msg):                    #this
        self.following = msg.data
    


    # These are the callbacks that run on a timer to update the published targets
    def sail_pub_callback(self): 
        msg = Float32()

# possible thrust vectors
        t1 = (self.windAngle + angle_of_attack + thrust_sail_offset) % 360
        Heading_to_t1 = shortestAngle(t1, self.targetHeading)

        t2 = (self.windAngle - angle_of_attack - thrust_sail_offset) % 360
        Heading_to_t2 = shortestAngle(t2, self.targetHeading)

#logic using existing shortest angle function
        if self.following:
            if abs(Heading_to_t1) <= abs(Heading_to_t2):
                msg.data = float((self.windAngle + angle_of_attack) % 360)
            else:
                msg.data = float((self.windAngle - angle_of_attack) % 360)

        self.targetSailAngle_publisher.publish(msg) #publish 

    def flap_pub_callback(self):
        msg = Float32()

        """
             * If the boat is sailing into the wind, we switch the angle of flap when heading - wind angle is at zero
             * Otherwise we switch the flap angle at +/- 180 degrees, the number being positive or negative dependant on if the boat is going
             *   or down

        """
        # Sailing into the wind
        if (self.windAngle >= 0 and self.heading >= 0) or (self.windAngle <= 0 and self.heading <= 0):
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

        #NOTE: TEMPORARILY DISABLED
        #self.targetFlapAngle_publisher.publish(msg)

    def rudder_pub_callback(self):
        msg = Float32()

        #print("heading: ", self.heading, "target heading: ", self.targetHeading)

        print(shortestAngle(self.heading, self.targetHeading))

        if shortestAngle(self.heading, self.targetHeading) < 0:
            rudderTarget = max(shortestAngle(self.heading, self.targetHeading), -45)


        else:
            rudderTarget = min(shortestAngle(self.heading, self.targetHeading) / 2, 45)


        print(rudderTarget, " rrR")

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
