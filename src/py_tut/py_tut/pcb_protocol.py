"""The serial protocol between the Raspberry Pi and the STM32 (its UART7).

No ROS in here, so it can be tested anywhere; PCBComm.py does the I/O.

Pi to STM32, every write period, one line:

    {"TargetsOutput":[{"targetBearing":123.4,"waypointLat":44.692500,...}]}

What the firmware needs from it (windbound-firmware, User/Src):
* app_comms.c ProcessRaspberryData collects from the first '{' to its
  matching '}' in a 256-byte buffer, so a packet must be 255 characters or
  fewer; a longer one is dropped without a word.
* app_protocol.c AppProtocol_ParseRpiSample needs all ten keys below.
* Its number parser reads plain decimals only, so a value written as
  "1e-05" would be read as 1. Every number here has fixed decimals.

STM32 to Pi, every 500 ms, one line:

    {"SensorInput":[{"windAngle":87}]}

windAngle is the windvane's apparent wind angle, degrees clockwise from the
bow. Newer firmware may add windSpeed (m/s) and windValid (0 or 1).
"""

import json
import math

MAX_PACKET_CHARS = 255
# The firmware's key, how many decimals to send (6 for lat/lon: 0.1 m), and
# the range a value is put into first. The ten keys alone take about 150 of
# the 255 characters, so every value is kept short: directions in [0, 360),
# flap and rudder within +/-45 degrees.
TARGET_FIELDS = (
    ('targetBearing', 1), ('waypointLat', 6), ('waypointLon', 6),
    ('targetSailAngle', 1), ('targetFlapAngle', 1), ('targetRudderAngle', 1),
    ('latitude', 6), ('longitude', 6), ('headingAngle', 1), ('windAngle', 1),
)
DIRECTIONS = ('targetBearing', 'targetSailAngle', 'headingAngle', 'windAngle')
DEFLECTIONS = ('targetFlapAngle', 'targetRudderAngle')
DEFLECTION_LIMIT_DEG = 45.0
WAYPOINT_COMMANDS = ('add', 'remove', 'startFollowing', 'stopFollowing', 'setCurrentWaypoint')


def format_targets(values):
    """The TargetsOutput line for a dict holding every key in TARGET_FIELDS."""
    parts = []
    for key, decimals in TARGET_FIELDS:
        value = float(values[key])
        if not math.isfinite(value):
            value = 0.0
        if key in DIRECTIONS:
            value = round(value, decimals) % 360.0       # 359.96 goes as 0.0, not 360.0
        elif key in DEFLECTIONS:
            value = max(-DEFLECTION_LIMIT_DEG, min(DEFLECTION_LIMIT_DEG, value))
        parts.append('"%s":%.*f' % (key, decimals, value))
    packet = '{"TargetsOutput":[{' + ','.join(parts) + '}]}'
    if len(packet) > MAX_PACKET_CHARS:
        raise ValueError('TargetsOutput is %d characters; the STM32 drops anything over %d'
                         % (len(packet), MAX_PACKET_CHARS))
    return packet + '\n'


class LineReader:
    """Splits whatever the serial port has delivered into complete lines,
    keeping a partial line until the rest of it arrives."""

    def __init__(self, limit=4096):
        self.pending = b''
        self.limit = limit

    def feed(self, data):
        self.pending += data
        *lines, self.pending = self.pending.split(b'\n')
        if len(self.pending) > self.limit:       # no newline for this long: noise, not a line
            self.pending = b''
        return [line.decode('utf-8', 'replace').strip() for line in lines if line.strip()]


def parse_line(line):
    """('sensor', {...}) for SensorInput, ('waypoint', line) for a waypoint
    command, or (None, line) for anything else."""
    try:
        packet = json.loads(line)
    except ValueError:
        return None, line
    if not isinstance(packet, dict):
        return None, line
    if 'SensorInput' in packet:
        try:
            data = packet['SensorInput'][0]
            sensor = {'windAngle': float(data['windAngle']),
                      'windValid': bool(int(data.get('windValid', 1)))}
            if 'windSpeed' in data:
                sensor['windSpeed'] = float(data['windSpeed'])
        except (KeyError, IndexError, TypeError, ValueError):
            return None, line
        return 'sensor', sensor
    if any(command in packet for command in WAYPOINT_COMMANDS):
        return 'waypoint', line
    return None, line
