# generated from rosidl_generator_py/resource/_idl.py.em
# with input from tutorial_interfaces:msg/PCB.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PCB(type):
    """Metaclass of message 'PCB'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('tutorial_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'tutorial_interfaces.msg.PCB')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__pcb
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__pcb
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__pcb
            cls._TYPE_SUPPORT = module.type_support_msg__msg__pcb
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__pcb

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class PCB(metaclass=Metaclass_PCB):
    """Message class 'PCB'."""

    __slots__ = [
        '_wind_speed',
        '_wind_direction',
        '_roll',
        '_pitch',
        '_yaw',
        '_latitude',
        '_longitude',
        '_heading',
        '_sail_angle',
        '_sailflap_angle',
        '_backflap_angle',
        '_rudder_angle',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'wind_speed': 'double',
        'wind_direction': 'double',
        'roll': 'double',
        'pitch': 'double',
        'yaw': 'double',
        'latitude': 'double',
        'longitude': 'double',
        'heading': 'double',
        'sail_angle': 'double',
        'sailflap_angle': 'double',
        'backflap_angle': 'double',
        'rudder_angle': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.wind_speed = kwargs.get('wind_speed', float())
        self.wind_direction = kwargs.get('wind_direction', float())
        self.roll = kwargs.get('roll', float())
        self.pitch = kwargs.get('pitch', float())
        self.yaw = kwargs.get('yaw', float())
        self.latitude = kwargs.get('latitude', float())
        self.longitude = kwargs.get('longitude', float())
        self.heading = kwargs.get('heading', float())
        self.sail_angle = kwargs.get('sail_angle', float())
        self.sailflap_angle = kwargs.get('sailflap_angle', float())
        self.backflap_angle = kwargs.get('backflap_angle', float())
        self.rudder_angle = kwargs.get('rudder_angle', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.wind_speed != other.wind_speed:
            return False
        if self.wind_direction != other.wind_direction:
            return False
        if self.roll != other.roll:
            return False
        if self.pitch != other.pitch:
            return False
        if self.yaw != other.yaw:
            return False
        if self.latitude != other.latitude:
            return False
        if self.longitude != other.longitude:
            return False
        if self.heading != other.heading:
            return False
        if self.sail_angle != other.sail_angle:
            return False
        if self.sailflap_angle != other.sailflap_angle:
            return False
        if self.backflap_angle != other.backflap_angle:
            return False
        if self.rudder_angle != other.rudder_angle:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def wind_speed(self):
        """Message field 'wind_speed'."""
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'wind_speed' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'wind_speed' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._wind_speed = value

    @builtins.property
    def wind_direction(self):
        """Message field 'wind_direction'."""
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'wind_direction' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'wind_direction' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._wind_direction = value

    @builtins.property
    def roll(self):
        """Message field 'roll'."""
        return self._roll

    @roll.setter
    def roll(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'roll' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'roll' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._roll = value

    @builtins.property
    def pitch(self):
        """Message field 'pitch'."""
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'pitch' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'pitch' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._pitch = value

    @builtins.property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'yaw' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._yaw = value

    @builtins.property
    def latitude(self):
        """Message field 'latitude'."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'latitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'latitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._latitude = value

    @builtins.property
    def longitude(self):
        """Message field 'longitude'."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'longitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'longitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._longitude = value

    @builtins.property
    def heading(self):
        """Message field 'heading'."""
        return self._heading

    @heading.setter
    def heading(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'heading' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'heading' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._heading = value

    @builtins.property
    def sail_angle(self):
        """Message field 'sail_angle'."""
        return self._sail_angle

    @sail_angle.setter
    def sail_angle(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'sail_angle' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sail_angle' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sail_angle = value

    @builtins.property
    def sailflap_angle(self):
        """Message field 'sailflap_angle'."""
        return self._sailflap_angle

    @sailflap_angle.setter
    def sailflap_angle(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'sailflap_angle' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sailflap_angle' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sailflap_angle = value

    @builtins.property
    def backflap_angle(self):
        """Message field 'backflap_angle'."""
        return self._backflap_angle

    @backflap_angle.setter
    def backflap_angle(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'backflap_angle' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'backflap_angle' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._backflap_angle = value

    @builtins.property
    def rudder_angle(self):
        """Message field 'rudder_angle'."""
        return self._rudder_angle

    @rudder_angle.setter
    def rudder_angle(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'rudder_angle' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'rudder_angle' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._rudder_angle = value
