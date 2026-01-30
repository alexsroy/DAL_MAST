# generated from rosidl_generator_py/resource/_idl.py.em
# with input from tutorial_interfaces:msg/Navigation.idl
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


class Metaclass_Navigation(type):
    """Metaclass of message 'Navigation'."""

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
                'tutorial_interfaces.msg.Navigation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__navigation
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__navigation
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__navigation
            cls._TYPE_SUPPORT = module.type_support_msg__msg__navigation
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__navigation

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Navigation(metaclass=Metaclass_Navigation):
    """Message class 'Navigation'."""

    __slots__ = [
        '_waypoint_latitude',
        '_waypoint_longitude',
        '_tacking_waypoint_latitude',
        '_tacking_waypoint_longitude',
        '_target_heading',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'waypoint_latitude': 'double',
        'waypoint_longitude': 'double',
        'tacking_waypoint_latitude': 'double',
        'tacking_waypoint_longitude': 'double',
        'target_heading': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
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
        self.waypoint_latitude = kwargs.get('waypoint_latitude', float())
        self.waypoint_longitude = kwargs.get('waypoint_longitude', float())
        self.tacking_waypoint_latitude = kwargs.get('tacking_waypoint_latitude', float())
        self.tacking_waypoint_longitude = kwargs.get('tacking_waypoint_longitude', float())
        self.target_heading = kwargs.get('target_heading', float())

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
        if self.waypoint_latitude != other.waypoint_latitude:
            return False
        if self.waypoint_longitude != other.waypoint_longitude:
            return False
        if self.tacking_waypoint_latitude != other.tacking_waypoint_latitude:
            return False
        if self.tacking_waypoint_longitude != other.tacking_waypoint_longitude:
            return False
        if self.target_heading != other.target_heading:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def waypoint_latitude(self):
        """Message field 'waypoint_latitude'."""
        return self._waypoint_latitude

    @waypoint_latitude.setter
    def waypoint_latitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'waypoint_latitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'waypoint_latitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._waypoint_latitude = value

    @builtins.property
    def waypoint_longitude(self):
        """Message field 'waypoint_longitude'."""
        return self._waypoint_longitude

    @waypoint_longitude.setter
    def waypoint_longitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'waypoint_longitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'waypoint_longitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._waypoint_longitude = value

    @builtins.property
    def tacking_waypoint_latitude(self):
        """Message field 'tacking_waypoint_latitude'."""
        return self._tacking_waypoint_latitude

    @tacking_waypoint_latitude.setter
    def tacking_waypoint_latitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'tacking_waypoint_latitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tacking_waypoint_latitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tacking_waypoint_latitude = value

    @builtins.property
    def tacking_waypoint_longitude(self):
        """Message field 'tacking_waypoint_longitude'."""
        return self._tacking_waypoint_longitude

    @tacking_waypoint_longitude.setter
    def tacking_waypoint_longitude(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'tacking_waypoint_longitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tacking_waypoint_longitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tacking_waypoint_longitude = value

    @builtins.property
    def target_heading(self):
        """Message field 'target_heading'."""
        return self._target_heading

    @target_heading.setter
    def target_heading(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'target_heading' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'target_heading' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._target_heading = value
