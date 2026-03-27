# This is to run effectively the sailboat simulation through nodes
# Most of the sailboat sim is physics and rendering, so I want to
# detach the physics and rendering from controls and actuation.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray

import pygame
from pygame.locals import *
import numpy as np
import math
import time
import random as rnd

import os
from ament_index_python.packages import get_package_share_directory



# If enabled, can control the sailboat with the keyboard
KEYBOARD_CONTROLS = True
NAV_ALGORITHM = True
CREATE_POLAR_PLOT = False
DRAW_THRUST_VECTOR = True
WAYPOINT_HUD_ENABLE = True
PUBLISH_VALUES = True
RUN_PHYSICS = True

# use share dir to get assets
pkg_share_dir = get_package_share_directory('py_tut')
images_dir = os.path.join(pkg_share_dir, 'assets')

# get image paths
ocean_path = os.path.join(images_dir, '/workspace/src/py_tut/assets/ocean.jpg')
wind_path = os.path.join(images_dir, '/workspace/src/py_tut/assets/arrow.png')
hull_path = os.path.join(images_dir, '/workspace/src/py_tut/assets/hull.png')
sail_path = os.path.join(images_dir, '/workspace/src/py_tut/assets/sail.png')
flap_path = os.path.join(images_dir, '/workspace/src/py_tut/assets/flap.png')

# Load image files
oceanTile = pygame.image.load(ocean_path)
windVane = pygame.image.load(wind_path)
hullImg = pygame.image.load(hull_path)
sailImg = pygame.image.load(sail_path)
flapImg = pygame.image.load(flap_path)

# These are variables used for scaling
# Below has units of pixels
TILE_SIZE = 100
windVaneSize = 50

# Take the original image, and divide by the shrink factor
shrinkHull = 3 # This scales it to 0.333 or 1 / 3
shrinkSail = 1.5 # This scales to 0.666 or 1 / 1.5
shrinkFlap = 1

# Scale the images to the size used in the simulation
oceanTile = pygame.transform.scale(oceanTile, (TILE_SIZE, TILE_SIZE))
windVane = pygame.transform.scale(windVane, (windVaneSize, windVaneSize))
hullImg = pygame.transform.scale(hullImg, (hullImg.get_width() / shrinkHull, hullImg.get_height() / shrinkHull))
sailImg = pygame.transform.scale(sailImg, (sailImg.get_width() / shrinkSail, sailImg.get_height() / shrinkSail))

D = 1000

# Pygame constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)

# This is the window that we will render to
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sailboat Sail Visualization")

getCourse = 1
didInit = 0

counter = 0

class waypoint:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.rad = radius

wp = waypoint(3500, 2000, 200)



class boat:
    # This sets all the variables related to the boat
    # If a variable has 'angle' in its name, it is the angle with respect to the screen, and is stored in radians
    # If a variable has 'deflection' in its name, it an angle with respect to another component of the boat, this can be stored in degrees
    # If a variable has 'length' in its name, IT IS NOT the graphical size of the boat, it is a dummy variable for calculation
    def __init__(self):
        # Hull parameters
        self.x = 400 # SCREEN_WIDTH // 2
        self.y = 2000 # SCREEN_HEIGHT // 2
        self.length = 40
        self.width = 20
        self.angle = 0  # (rads)

        # Sail parameters
        self.sailLen = 100
        self.sailAng = 0 # (rads)
        # The thrust vector's direction is a physical property of the sail, and is a constant
        self.angleOfThrustDEGS = 58 # Change this one please
        self.angleOfThrust = math.radians(180 - self.angleOfThrustDEGS)
        # The is the magnitude of the thrust vector and has arbitrary length
        self.maxThrust = 30
        self.thrust = 0
        # Angle of attack that creates the most lift
        self.angleOfAttack = 12 # (degs)

        # Flap parameters
        self.flapLen = 40
        self.flapAng = 0
        self.flapDeflection = 0

        # Rudder parameters
        self.rudderAng = 0
        self.rudderLen = 20
        self.rudderDeflection = 0

        # The maximum amount the rudder or flap can turn in one direction
        # If max deflection is 45 degrees, the rudder deflection can be from -45 to 45 degrees
        self.maxFlapDeflection = 45
        self.maxRudderDeflection = 45

        # When the physics engine runs, if the deflections are not equal to these targets, it will rotate the deflections towards the target
        self.rudderTarget = 0.0
        self.flapTarget = 0.0
        self.sailTarget = 0.0

        self.speed = 0

        # Nav algorithm stuff
        self.bearing = [[700, 100], [200, 0]]
        self.bearingAng = 0
        self.track = [[self.x, self.y]]
        self.TACKING_ANGLE = 40
        self.HEADING_TOLERANCE = 5
        self.BBReverseSpace = 200
        self.course = 0
        self.tacking = 0 # 1 if tacking, 0 otherwise
        self.changingTack = 0

    """These next few functions are used in the physics engine to rotate the components of the boat"""

    # Turn the sail X degrees
    def turnSail(self, degs):
        self.sailAng += degs
    # Turn the flap X degrees
    def turnFlap(self, degs):
        self.flapDeflection += degs
    # Turn the rudder X degrees
    def turnRudd(self, degs):
        self.rudderDeflection += degs


    # Rotate the boat and all parts attached
    def rotateBoat(self, degs):
        self.convertToDegs()
        self.angle += degs
        self.sailAng += degs
        self.flapAng += degs
        self.rudderAng += degs
        self.convertToRads()
    # Update the x and y pos of the hull
    def sailForwards(self, dist):
        self.x += dist * math.cos(math.radians(self.angle))
        self.y += dist * math.sin(math.radians(self.angle))


    """For calculations only use degrees, so use these are helper functions at the start and end of the physics frame to convert relevant variables"""
    def convertToRads(self):
        self.angle = math.radians(self.angle)
        self.sailAng = self.heading = math.radians(self.sailAng)
        self.flapAng = math.radians(self.flapAng)
        self.rudderAng = math.radians(self.rudderAng)
        self.angleOfThrust = math.radians(self.angleOfThrust)
    def convertToDegs(self):
        self.angle = math.degrees(self.angle)
        self.sailAng = math.degrees(self.sailAng)
        self.flapAng = math.degrees(self.flapAng)
        self.rudderAng = math.degrees(self.rudderAng)
        self.angleOfThrust = math.degrees(self.angleOfThrust)

    """This function handles flap and rudder actuation, rotation of the sail based on the wind and the flap, and movement of the hull through water"""
    def updatePhysics(self, windAng):
        # Convert everything to degrees
        self.convertToDegs()
        windAng = math.degrees(windAng)

        # print("(", self.x, ", ", self.y, ")", sep="")

        # This is the angle of attack the sail actually makes with the wind
        windSailAng = self.sailAng - windAng
        #print(windSailAng, ",", self.flapAng, ",", self.sailAng, ",", self.flapTarget)

        # The unit circle has been tricky, everything is working so far, so I won't change this part
        if self.sailAng < -180:
            self.sailAng = 180
        elif self.sailAng > 180:
            self.sailAng = -180

        if self.angle > 180:
            self.angle = (self.angle - 180) - 180
        if self.angle < -180:
            self.angle = (self.angle + 180) + 180


        # Actuate the flap
        if self.flapDeflection < self.flapTarget:
            self.turnFlap(1)
        elif self.flapDeflection > self.flapTarget:
            self.turnFlap(-1)

        # Actuate the rudder
        if self.rudderDeflection < self.rudderTarget:
            self.turnRudd(1)
        elif self.rudderDeflection > self.rudderTarget:
            self.turnRudd(-1)


        # Update the angles with respect to the screen, used in rendering
        self.flapAng = self.flapDeflection + self.sailAng
        self.rudderAng = self.rudderDeflection + self.angle

        # Turn sail based on the geometry of the sail + flap
        rotateFactor = 0.02 # Magic number
        # Eqn. 1
        """ THIS IS FOR A FREELY ROTATING SAIL, MOVE TO CONTROLS AND MAKE MOTORIZED  """
        self.turnSail(rotateFactor * (self.sailLen * math.sin(math.radians(windSailAng)) + self.flapLen * math.sin(math.radians(windSailAng + self.flapDeflection))))

        # The next section converts the thrust vector to forwards motion

        # Set the angle of thrust on the correct side of the sail according to how the wind meets the sail
        if windSailAng %  180 <= 90:
            self.angleOfThrust = 180 + self.angleOfThrustDEGS
        else:
            self.angleOfThrust = 180 - self.angleOfThrustDEGS

        # The thrust factor is similar to the thrust being generated by the wing
        # We approximate it as linear up to a maximum of 12 degrees, and a linear decrease going over 12 degrees
        if windSailAng % 180 <= 26: # if windSailAng is close to 12, that left term approaches 1
            thrustFactor = 0.05 * (1 - abs(windSailAng % 180 - 12) / 12) # original thrustfactor is 0.025

        elif windSailAng % 180 >= 156:
            thrustFactor = 0.05 * (1 - abs(windSailAng % 180 - 168) / 12)

        else:
            thrustFactor = 0


        # Self.thrust is the forwards component of the thrust vector
        self.thrust = thrustFactor * self.maxThrust * math.cos(math.radians(self.angleOfThrust + self.sailAng - self.angle))
        # Since when sailing around 25 degrees into the wind, the speed drops off to zero,
        # I'm making the assumption that aerodynamic drag is going to be a constant magnitude of 0.709T
        # Which acts in the direction of the wind, but needs to be projected onto the line of heading
        drag = 0.709 * thrustFactor * self.maxThrust * math.cos(math.radians(self.angle - windAng)) * min(abs(self.sailAng - windAng) / 12, 1)

        """ RAW VALUE FROM MOVELLA"""
        self.speed = self.thrust - drag

        self.sailForwards(self.speed)

        # Rotate boat based on the rudder angle
        manouveringFactor = 10
        # Eqn. 3
        self.rotateBoat(manouveringFactor * (-1 * self.thrust * self.rudderLen * math.sin(math.radians(self.rudderDeflection))))

        self.convertToRads()

    # Renders the boat to the window
    def renderBoat(self):
        global screen
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        global hullImg
        global sailImg
        global shrinkSail
        global flapImg
        global shrinkFlap

        # Draw hull
        blitRotate(screen, hullImg, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], [hullImg.get_width() / 2, hullImg.get_height() / 2], -1 * math.degrees(self.angle) + 90)
        # Draw the sail, saving the bounding rectangle to calculate the flap's position
        sailRect = blitRotate(screen, sailImg, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], [sailImg.get_width() / 2, sailImg.get_height() / 2 + 7], -1 * math.degrees(self.sailAng) - 90)
        # Draw the flap
        blitRotate(screen, flapImg, [SCREEN_WIDTH / 2 + math.cos(self.sailAng) * (sailImg.get_height() / 2 + 7), SCREEN_HEIGHT / 2 + math.sin(self.sailAng) * (sailImg.get_height() / 2 + 7)], [1, 1], -1 * math.degrees(self.flapAng) + 90)

        # This is a line representing the thrust vector, but the last line is commented out so it isn't drawn
        if DRAW_THRUST_VECTOR:
            thrustSurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            thrustStartX = SCREEN_WIDTH / 2 + self.sailLen * math.cos(self.sailAng) / 2
            thrustStartY = SCREEN_HEIGHT / 2 + self.sailLen * math.sin(self.sailAng) / 2
            thrustEndX = thrustStartX + self.maxThrust * math.cos(self.sailAng + self.angleOfThrust)
            thrustEndY = thrustStartY + self.maxThrust * math.sin(self.sailAng + self.angleOfThrust)
            pygame.draw.line(thrustSurf, BLACK, (thrustStartX, thrustStartY), (thrustEndX, thrustEndY), 2) ## Uncomment to draw
            screen.blit(thrustSurf, (0, 0))


    def addTrack(self): # THIS IS A DRAWING FUNCTION
        self.track.append([self.x, self.y])

    """
    def setRudder(self, course):
        if math.degrees(self.angle) - course > 0:
            self.rudderTarget = -1 * max(-0.5 * (math.degrees(self.angle) - course), -45)
        else:
            self.rudderTarget = -1 * min(-0.5 * (math.degrees(self.angle) - course), 45)
    """

# Break the background into tiles, and reander until the whole screen is full of tiles
# Render a couple extra tiles on both the left and right side of the screen, since as the boat moves, the tiles move
def renderBackground(boatX, boatY):
    global screen
    global oceanTile
    global TILE_SIZE

    tileHeight = TILE_SIZE
    tileWidth = TILE_SIZE

    limX = SCREEN_WIDTH / tileWidth + 1
    limY = SCREEN_HEIGHT / tileHeight + 1
    i = -1
    while i <= limX:
        j = -1
        while j <= limY:
            screen.blit(oceanTile, (i * tileWidth - boatX % tileWidth, j * tileHeight - boatY % tileHeight))
            j += 1
        i += 1

    # Render the waypoint in the ocean
    waypointSurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(waypointSurf, (128, 0, 0), (wp.x - nautono.x + SCREEN_WIDTH // 2, wp.y - nautono.y + SCREEN_HEIGHT // 2), wp.rad)
    screen.blit(waypointSurf, (0, 0))

# This function is from: https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
# It rotates the image about originPos (a list with two elements describing point on the image), and draws it at location pos (another list)
def blitRotate(surf, image, pos, originPos, angle, renderRect = False):
    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # rotated image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    #if renderRect:
    #    pygame.draw.rect(screen, RED, rotated_image_rect.scale(1 / shrinkSail))

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
    return rotated_image_rect

# This renders an arrow in the corner of the screen to show which direction the wind is blowing
def renderWindVane(windAng):
    global screen
    global windVane
    blitRotate(screen, windVane, [windVaneSize / 2 + 10, windVaneSize / 2 + 10], [windVaneSize / 2, windVaneSize / 2], -1 * windAng - 45 + 180)

def runSimHeadless(boat, wind_direction, waypoint):
    # Run the sailing algorithm, then the physics engine based on the direction of the wind
    # getCourse = nautono.sailingAlgorithm(wind_direction, waypoint)
    nautono.updatePhysics(wind_direction)


def createPolarPlot(boat, waypoint):
    r = []
    i = 0
    with open('polar.csv', 'w') as f:
        f.write("Angle, Speed\n")
        for angle in list(range(-180, 190, 10)):
            timer = time.time() + 2
            while timer - time.time() > 0: # Run simulation for 5 seconds
                runSimHeadless(boat, 0, waypoint)
                # Render the tiles, wind vane, and boat to the screen
                renderBackground(nautono.x, nautono.y)
                renderWindVane(0)
                nautono.renderBoat()

                # Update the display
                pygame.display.flip()

            f.write(str(math.degrees(boat.angle)) + ", " + str(boat.speed) + "\n") # Print out the thrust and angle to the terminal
            print(str(math.degrees(nautono.angle - 0) % 360 - 180) + ", " + str(boat.speed))
            r.append(boat.speed)
            i += 1
            nautono.rotateBoat(10)

    fig = px.line_polar(r=r, theta = range(0,370,10), range_theta=[-180,180], start_angle=0, direction="clockwise")
    fig.show()

def convToHudCords(num, isX):
    return num / 10 + isX * 150 + (1 - isX) * 50

def renderHud(fadeVal):
    """ Render a minimap at 1/10th scale """
    global nautono
    global wp
    global wind_direction
    global screen
    hudSurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    HUDX = 150
    HUDY = 50

    # Render brown boarder 10px larger than the ocean inside
    boarder = Rect(HUDX - 10, HUDY - 10, 520, 520)
    pygame.draw.rect(hudSurf, (128, 66, 0, fadeVal), boarder)

    # Render blue rectangle at 150, 50 inside the boarder rect
    ocean = Rect(HUDX, HUDY, 500, 500)
    pygame.draw.rect(hudSurf, (0, 75, 150, fadeVal), ocean)

    # Draw manouving out of bounds
    # I might want to lock the bearing angle to 0 to +/- 90, and flip the APlus and AMinus calculations if bearingAng 180 < x < 90 or -180 < x < -90
    bearingAng = math.radians(nautono.bearingAng) #math.radians(90 - 180 - math.degrees(math.atan2(nautono.bearing[0][0] - nautono.bearing[1][0], nautono.bearing[0][1] - nautono.bearing[1][1])))

    UPlus = [D/15 * math.cos(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[0][0], 1), D/15 * math.sin(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[0][1], 0)]
    UMinus = [D/15 * math.cos(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[1][0], 1), D/15 * math.sin(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[1][1], 0)]
    VPlus = [D/15 * math.cos(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[0][0], 1), D/15 * math.sin(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[0][1], 0)]
    VMinus = [D/15 * math.cos(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[1][0], 1), D/15 * math.sin(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[1][1], 0)]
    RB = [UPlus, VPlus, VMinus, UMinus]
    pygame.draw.polygon(hudSurf, (200, 100, 150, fadeVal), RB)

    # These are the initial offsets from the bearing
    APlus = [D/20 * math.cos(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[0][0], 1), D/20 * math.sin(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[0][1], 0)]
    AMinus = [D/20 * math.cos(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[1][0], 1), D/20 * math.sin(bearingAng + math.radians(90)) + convToHudCords(nautono.bearing[1][1], 0)]
    BPlus = [D/20 * math.cos(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[0][0], 1), D/20 * math.sin(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[0][1], 0)]
    BMinus = [D/20 * math.cos(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[1][0], 1), D/20 * math.sin(bearingAng - math.radians(90)) + convToHudCords(nautono.bearing[1][1], 0)]

    BB = [APlus, BPlus, BMinus, AMinus]

    pygame.draw.polygon(hudSurf, (0, 100, 200, fadeVal), BB)

    # Draw the waypoint
    pygame.draw.circle(hudSurf, (128, 0, 0, fadeVal), (wp.x / 10 + 150, wp.y / 10 + 50), wp.rad / 10)

    # Draw the boat
    boat_length = 10
    boat_width = 5
    nose = (nautono.x / 10 + boat_length * math.cos(nautono.angle) + 150, nautono.y / 10 + boat_length * math.sin(nautono.angle) + 50),
    port = (nautono.x / 10 + (boat_width / 2) * math.cos(nautono.angle - math.radians(90)) + 150, 50 + nautono.y / 10 + (boat_width / 2) * math.sin(nautono.angle - math.radians(90))),
    starboard = (nautono.x / 10 + (boat_width / 2) * math.cos(nautono.angle + math.radians(90)) + 150, 50 + nautono.y / 10 + (boat_width / 2) * math.sin(nautono.angle + math.radians(90)))

    pygame.draw.polygon(hudSurf, (0, 0, 0, fadeVal), (nose, port, starboard))

    # Draw Bearing
    pygame.draw.line(hudSurf, (0, 0, 0, fadeVal), (nautono.bearing[0][0] / 10 + 150, nautono.bearing[0][1] / 10 + 50), (nautono.bearing[1][0] / 10 + 150, nautono.bearing[1][1] / 10 + 50), 1)

    for x in range(1, len(nautono.track)):
        if len(nautono.track) < 2:
            break
        pygame.draw.line(hudSurf, (255, 255, 0, fadeVal), (convToHudCords(nautono.track[x - 1][0], 1), convToHudCords(nautono.track[x - 1][1], 0)), (convToHudCords(nautono.track[x][0], 1), convToHudCords(nautono.track[x][1], 0)))

    screen.blit(hudSurf, (0, 0))

#def calcTriArea(A, B, C): # Input 3 lists of 2 points for each corner in format [x, y]
#    return abs((B[0] * A[1] - A[0] * B[1]) + (C[0] * B[1] - C[1] * B[0]) + (A[0] * C[1] - A[1] * C[0])) / 2

#def pointInRect(point, BB): # https://stackoverflow.com/questions/17136084/checking-if-a-point-is-inside-a-rotated-rectangle
#    #print(calcTriArea(BB[0], point, BB[3]) + calcTriArea(BB[3], point, BB[2]) + calcTriArea(BB[2], point, BB[1]) + calcTriArea(BB[0], point, BB[1]) , " <= ", abs((D/10) * abs(BB[0][0] - BB[3][0]) / (math.cos(nautono.bearingAng) + 0.000000000000000001)) + 10)
#    #print("RHS:", abs(BB[0][0] - BB[3][0]), " ang ", math.cos(nautono.bearingAng))
#    return calcTriArea(BB[0], point, BB[3]) + calcTriArea(BB[3], point, BB[2]) + calcTriArea(BB[2], point, BB[1]) + calcTriArea(BB[0], point, BB[1]) <= (abs(BB[0][1] - BB[1][1]) / (math.cos(nautono.bearingAng) + 0.000000000000000001)) * (abs(BB[0][0] - BB[3][0]) / (math.cos(nautono.bearingAng) + 0.000000000000000001)) + 10



nautono = boat()

counter = 0

if CREATE_POLAR_PLOT:
    createPolarPlot(nautono, wp)

running = not CREATE_POLAR_PLOT

# Initialize Pygame
pygame.init()

setting_desired_direction = False
# This is a timer to block inputs for the keys A and D so they rotate by 10 degs without pausing the rest of the simulation
ADBlockingTimer = time.time()
TabBlocker = time.time()
hudState = 0
opacity = 0
settingWP = False


class SIM_ROS_HANDLER(Node):


    def __init__(self):
        super().__init__('sailboat_sim')

        self.windVane_publisher = self.create_publisher(Float32, 'wind_direction', 10)
        self.compass_publisher = self.create_publisher(Float32, 'heading_direction', 10)

        self.latitude_publisher = self.create_publisher(Float32, 'latitude', 10)
        self.longitude_publisher = self.create_publisher(Float32, 'longitude', 10)
        self.waypoint_latitude_publisher = self.create_publisher(Float32, 'waypoint_latitude', 10)
        self.waypoint_longitude_publisher = self.create_publisher(Float32, 'waypoint_longitude', 10)

        self.sailAngle_publisher = self.create_publisher(Float32, 'sail_angle', 10)
        self.flapAngle_publisher = self.create_publisher(Float32, 'flap_angle', 10)
        self.rudderAngle_publisher = self.create_publisher(Float32, 'rudder_angle', 10)

        self.targetSailAngle_subscriber = self.create_subscription(Float32, 'sail_angle_target', self.sail_target_callback, 10)
        self.targetFlapAngle_subscriber = self.create_subscription(Float32, 'flap_angle_target', self.flap_target_callback, 10)
        self.targetRudderAngle_subscriber = self.create_subscription(Float32, 'rudder_angle_target', self.rudder_target_callback, 10)

        self.bearingAngle_subscriber = self.create_subscription(Float32, 'bearing_angle', self.bearing_angle_callback, 10)
        self.bearing_subscriber = self.create_subscription(Float32MultiArray, 'bearing', self.bearing_callback, 10)

        # debug subscriber to set the waypoint x and y in one command
        self.debug_wp_subscriber = self.create_subscription(Float32MultiArray, 'debug_wp', self.debug_wp_callback, 10)

        timer_period = 0.02  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def sail_target_callback(self, msg):
        global nautono
        nautono.sailTarget = msg.data

    def flap_target_callback(self, msg):
        global nautono
        nautono.flapTarget = msg.data
        print(nautono.flapTarget)

    def rudder_target_callback(self, msg):
        global nautono
        nautono.rudderTarget = msg.data

    def bearing_callback(self, msg):
        global nautono
        arr = msg.data
        nautono.bearing = [[msg.data[0], msg.data[1]], [msg.data[2], msg.data[3]]]

    def bearing_angle_callback(self, msg):
        global nautono
        nautono.bearingAng = msg.data

    # debug function to set the waypoint x and y from terminal
    # publish as: ros2 topic pub --once /debug_wp std_msgs/msg/Float32MultiArray 'data: [x, y]'
    def debug_wp_callback(self, msg):
        global wp
        wp.x = msg.data[0]
        wp.y = msg.data[1]

    def timer_callback(self):
        global counter
        global nautono
        global hudState
        global opacity

        global setting_desired_direction
        # This is a timer to block inputs for the keys A and D so they rotate by 10 degs without pausing the rest of the simulation
        global ADBlockingTimer
        global TabBlocker
        global settingWP

        # Get mouse position to set wind direction
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Wind comes from the mouse towards the centre of the screen, store it as an angle
        wind_direction = math.atan2(mouse_y - SCREEN_HEIGHT // 2, mouse_x - SCREEN_WIDTH // 2)

        # If the right mouse button is released, snap the boat to point to that direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hudState == 2:
                settingWP = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and settingWP:
                settingWP = False
                wp.x = (mouse_x - 150) * 10
                wp.y = (mouse_y - 50) * 10
                getCourse = 1

            # These two rotate the boat on mouse right click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
                setting_desired_direction = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and setting_desired_direction:
                setting_desired_direction = False
                # Set the boat's desired direction based on the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                nautono.rotateBoat(math.degrees(wind_direction - nautono.angle))

        # If left and write update the rudder target, up and down update the flap target
        if KEYBOARD_CONTROLS:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]: # Flap
                nautono.flapTarget += nautono.flapTarget < nautono.maxFlapDeflection
            elif keys[pygame.K_DOWN]:
                nautono.flapTarget -= nautono.flapTarget > -1 * nautono.maxFlapDeflection

            if keys[pygame.K_LEFT]: # Rudder
                nautono.rudderTarget += nautono.rudderTarget < nautono.maxRudderDeflection
            elif keys[pygame.K_RIGHT]:
                nautono.rudderTarget -= nautono.rudderTarget > -1 * nautono.maxRudderDeflection

            if keys[pygame.K_d] and time.time() - ADBlockingTimer > 0.15: # adjust angle by 10 degs
                nautono.rotateBoat(10)
                ADBlockingTimer = time.time()

            elif keys[pygame.K_a] and time.time() - ADBlockingTimer > 0.15:
                nautono.rotateBoat(-10)
                ADBlockingTimer = time.time()

            if keys[pygame.K_TAB] and time.time() - TabBlocker > 0.2:
                if hudState == 0: # If it is not on screen
                    hudState = 1 # Fade it in
                elif hudState == 2: # If it is fully faded in
                    hudState = -1 # Fade it out

                TabBlocker = time.time()

            if keys[pygame.K_SPACE]:
                pass
                #nautono.getBearing(wind_direction, wp)

            if keys[pygame.K_t]:
                nautono.addTrack()

        # wind_direction = math.radians(10)

        # Run all the physics
        #if not counter:
        #    nautono.getBearing(math.degrees(wind_direction), wp)
        #    nautono.sailingAlgorithm(math.degrees(wind_direction), wp)

        runSimHeadless(nautono, wind_direction, wp)

        # Render the tiles, wind vane, and boat to the screen
        renderBackground(nautono.x, nautono.y)
        renderWindVane(math.degrees(wind_direction))
        nautono.renderBoat()

        if WAYPOINT_HUD_ENABLE:
            if hudState == 1 and opacity < 255: # Isn't it funny that for an engineering demonstrater I added a fade effect to the hud?
                opacity += 1

            elif hudState == 1 and opacity == 255:
                hudState = 2

            elif hudState == -1 and opacity > 0:
                opacity -= 1

            elif hudState == -1 and opacity == 0:
                hudState = 0

            renderHud(opacity)

            if counter % 250 == 1:
                nautono.addTrack()

        # Publish sensor information
        f = Float32()

        if PUBLISH_VALUES:
            f.data = math.degrees(wind_direction)
            self.windVane_publisher.publish(f)
            f.data = math.degrees(nautono.angle)
            self.compass_publisher.publish(f)

            #print(type(nautono.flapDeflection))
            f.data = float(nautono.flapDeflection)
            self.flapAngle_publisher.publish(f)
            f.data = float(nautono.rudderDeflection)
            self.rudderAngle_publisher.publish(f)

            f.data = float(nautono.x)
            self.longitude_publisher.publish(f)
            f.data = float(nautono.y)
            self.latitude_publisher.publish(f)

            f.data = float(wp.x)
            self.waypoint_longitude_publisher.publish(f)
            f.data = float(wp.y)
            self.waypoint_latitude_publisher.publish(f)

        #f.data = float(math.degrees(nautono.course)) # This will have to remain in the nav algorithm
        #self.targetHeading_publisher.publish(f)

        print(nautono.rudderDeflection)

        # Update the display
        pygame.display.flip()
        counter += 1









def main(args=None):
    # Main loop
    #print(getCourse)

    rclpy.init(args=args)

    sailboat_sim = SIM_ROS_HANDLER()

    rclpy.spin(sailboat_sim)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()














