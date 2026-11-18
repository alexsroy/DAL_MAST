"""Tests for pcb_protocol: plain pytest, no ROS or serial port needed.

    cd src/py_tut && python -m pytest test/test_pcb_protocol.py
"""

import json
import re

import pytest

from py_tut.pcb_protocol import (MAX_PACKET_CHARS, TARGET_FIELDS, LineReader, format_targets,
                                 parse_line)

TYPICAL = {'targetBearing': 123.456789, 'waypointLat': 44.69250106811523,
           'waypointLon': -63.5530014038086, 'targetSailAngle': 98.00000000000001,
           'targetFlapAngle': 0.0, 'targetRudderAngle': -12.5, 'latitude': 44.69251251220703,
           'longitude': -63.55301284790039, 'headingAngle': -171.23, 'windAngle': 87.0}


def test_packet_is_one_line_the_firmware_can_frame():
    packet = format_targets(TYPICAL)
    assert packet.endswith('\n') and packet.count('\n') == 1
    body = packet.strip()
    assert body.startswith('{"TargetsOutput":[{') and body.endswith('}]}')
    assert json.loads(body)['TargetsOutput'][0].keys() == {key for key, _ in TARGET_FIELDS}


def test_worst_case_packet_fits_the_firmware_buffer():
    for angle in (-359.99, -180.04, -45.06, 359.96, 1234.5):
        worst = {key: (-179.123456 if key in ('waypointLon', 'longitude') else -89.123456
                       if key in ('waypointLat', 'latitude') else angle) for key, _ in TARGET_FIELDS}
        assert len(format_targets(worst).strip()) <= MAX_PACKET_CHARS, angle


def test_directions_and_deflections_are_kept_in_range():
    data = json.loads(format_targets(dict(TYPICAL, targetBearing=-90, headingAngle=359.96,
                                          windAngle=725, targetRudderAngle=-60,
                                          targetFlapAngle=50)))['TargetsOutput'][0]
    assert (data['targetBearing'], data['headingAngle'], data['windAngle']) == (270.0, 0.0, 5.0)
    assert (data['targetRudderAngle'], data['targetFlapAngle']) == (-45.0, 45.0)


def test_numbers_are_plain_decimals():
    """The firmware's StringToFloat stops at an 'e': 1e-05 would become 1."""
    values = dict(TYPICAL, targetRudderAngle=1.2e-07, targetSailAngle=-3.4e-12)
    body = format_targets(values)
    numbers = re.findall(r'"[A-Za-z]+":([^,}\[{]+)', body)
    assert len(numbers) == len(TARGET_FIELDS)
    assert all(re.fullmatch(r'-?\d+\.\d+', number) for number in numbers), numbers
    assert json.loads(body)['TargetsOutput'][0]['targetRudderAngle'] == 0.0


def test_values_that_are_not_numbers_go_as_zero():
    body = format_targets(dict(TYPICAL, headingAngle=float('nan'), windAngle=float('inf')))
    data = json.loads(body)['TargetsOutput'][0]
    assert data['headingAngle'] == 0.0 and data['windAngle'] == 0.0


def test_lines_split_across_reads_are_joined():
    reader = LineReader()
    assert reader.feed(b'{"SensorInput":[{"wind') == []
    assert reader.feed(b'Angle":87}]}\r\n{"SensorInput":[{"windAngle":88}]}\r\n{"Sen') == [
        '{"SensorInput":[{"windAngle":87}]}', '{"SensorInput":[{"windAngle":88}]}']
    assert reader.feed(b'sorInput":[{"windAngle":89}]}\n') == ['{"SensorInput":[{"windAngle":89}]}']


def test_reads_the_firmwares_sensor_lines_old_and_new():
    assert parse_line('{"SensorInput":[{"windAngle":87}]}') == (
        'sensor', {'windAngle': 87.0, 'windValid': True})
    kind, sensor = parse_line('{"SensorInput":[{"windAngle":87.5,"windSpeed":4.2,"windRef":"R","windValid":0}]}')
    assert kind == 'sensor' and sensor == {'windAngle': 87.5, 'windSpeed': 4.2, 'windValid': False}


def test_passes_waypoint_commands_on_and_ignores_noise():
    command = '{"add":[{"latitude":44.69,"longitude":-63.55}]}'
    assert parse_line(command) == ('waypoint', command)
    for noise in ('', 'garbage', '{"SensorInput":[]}', '[1, 2]', '{"other":1}'):
        assert parse_line(noise)[0] is None
