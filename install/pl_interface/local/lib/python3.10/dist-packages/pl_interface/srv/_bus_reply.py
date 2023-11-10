# generated from rosidl_generator_py/resource/_idl.py.em
# with input from pl_interface:srv/BusReply.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'data'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BusReply_Request(type):
    """Metaclass of message 'BusReply_Request'."""

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
            module = import_type_support('pl_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pl_interface.srv.BusReply_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__bus_reply__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__bus_reply__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__bus_reply__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__bus_reply__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__bus_reply__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BusReply_Request(metaclass=Metaclass_BusReply_Request):
    """Message class 'BusReply_Request'."""

    __slots__ = [
        '_cmd',
        '_data_len',
        '_data',
        '_err',
    ]

    _fields_and_field_types = {
        'cmd': 'uint8',
        'data_len': 'uint8',
        'data': 'sequence<uint8>',
        'err': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint8')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd = kwargs.get('cmd', int())
        self.data_len = kwargs.get('data_len', int())
        self.data = array.array('B', kwargs.get('data', []))
        self.err = kwargs.get('err', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
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
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.cmd != other.cmd:
            return False
        if self.data_len != other.data_len:
            return False
        if self.data != other.data:
            return False
        if self.err != other.err:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd(self):
        """Message field 'cmd'."""
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cmd' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'cmd' field must be an unsigned integer in [0, 255]"
        self._cmd = value

    @builtins.property
    def data_len(self):
        """Message field 'data_len'."""
        return self._data_len

    @data_len.setter
    def data_len(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'data_len' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'data_len' field must be an unsigned integer in [0, 255]"
        self._data_len = value

    @builtins.property
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'B', \
                "The 'data' array.array() must have the type code of 'B'"
            self._data = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'data' field must be a set or sequence and each value of type 'int' and each unsigned integer in [0, 255]"
        self._data = array.array('B', value)

    @builtins.property
    def err(self):
        """Message field 'err'."""
        return self._err

    @err.setter
    def err(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'err' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'err' field must be an unsigned integer in [0, 255]"
        self._err = value


# Import statements for member types

# Member 'data'
# already imported above
# import array

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_BusReply_Response(type):
    """Metaclass of message 'BusReply_Response'."""

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
            module = import_type_support('pl_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pl_interface.srv.BusReply_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__bus_reply__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__bus_reply__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__bus_reply__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__bus_reply__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__bus_reply__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BusReply_Response(metaclass=Metaclass_BusReply_Response):
    """Message class 'BusReply_Response'."""

    __slots__ = [
        '_cmd',
        '_data_len',
        '_data',
        '_err',
    ]

    _fields_and_field_types = {
        'cmd': 'uint8',
        'data_len': 'uint8',
        'data': 'sequence<uint8>',
        'err': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint8')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd = kwargs.get('cmd', int())
        self.data_len = kwargs.get('data_len', int())
        self.data = array.array('B', kwargs.get('data', []))
        self.err = kwargs.get('err', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
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
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.cmd != other.cmd:
            return False
        if self.data_len != other.data_len:
            return False
        if self.data != other.data:
            return False
        if self.err != other.err:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd(self):
        """Message field 'cmd'."""
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cmd' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'cmd' field must be an unsigned integer in [0, 255]"
        self._cmd = value

    @builtins.property
    def data_len(self):
        """Message field 'data_len'."""
        return self._data_len

    @data_len.setter
    def data_len(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'data_len' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'data_len' field must be an unsigned integer in [0, 255]"
        self._data_len = value

    @builtins.property
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'B', \
                "The 'data' array.array() must have the type code of 'B'"
            self._data = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'data' field must be a set or sequence and each value of type 'int' and each unsigned integer in [0, 255]"
        self._data = array.array('B', value)

    @builtins.property
    def err(self):
        """Message field 'err'."""
        return self._err

    @err.setter
    def err(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'err' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'err' field must be an unsigned integer in [0, 255]"
        self._err = value


class Metaclass_BusReply(type):
    """Metaclass of service 'BusReply'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pl_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pl_interface.srv.BusReply')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__bus_reply

            from pl_interface.srv import _bus_reply
            if _bus_reply.Metaclass_BusReply_Request._TYPE_SUPPORT is None:
                _bus_reply.Metaclass_BusReply_Request.__import_type_support__()
            if _bus_reply.Metaclass_BusReply_Response._TYPE_SUPPORT is None:
                _bus_reply.Metaclass_BusReply_Response.__import_type_support__()


class BusReply(metaclass=Metaclass_BusReply):
    from pl_interface.srv._bus_reply import BusReply_Request as Request
    from pl_interface.srv._bus_reply import BusReply_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
