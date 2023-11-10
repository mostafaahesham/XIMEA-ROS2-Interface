// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from pl_interface:srv/BusReply.idl
// generated code does not contain a copyright notice
#include "pl_interface/srv/detail/bus_reply__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "pl_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "pl_interface/srv/detail/bus_reply__struct.h"
#include "pl_interface/srv/detail/bus_reply__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // data
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // data

// forward declare type support functions


using _BusReply_Request__ros_msg_type = pl_interface__srv__BusReply_Request;

static bool _BusReply_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _BusReply_Request__ros_msg_type * ros_message = static_cast<const _BusReply_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd
  {
    cdr << ros_message->cmd;
  }

  // Field name: data_len
  {
    cdr << ros_message->data_len;
  }

  // Field name: data
  {
    size_t size = ros_message->data.size;
    auto array_ptr = ros_message->data.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: err
  {
    cdr << ros_message->err;
  }

  return true;
}

static bool _BusReply_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _BusReply_Request__ros_msg_type * ros_message = static_cast<_BusReply_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd
  {
    cdr >> ros_message->cmd;
  }

  // Field name: data_len
  {
    cdr >> ros_message->data_len;
  }

  // Field name: data
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->data.data) {
      rosidl_runtime_c__uint8__Sequence__fini(&ros_message->data);
    }
    if (!rosidl_runtime_c__uint8__Sequence__init(&ros_message->data, size)) {
      fprintf(stderr, "failed to create array for field 'data'");
      return false;
    }
    auto array_ptr = ros_message->data.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: err
  {
    cdr >> ros_message->err;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pl_interface
size_t get_serialized_size_pl_interface__srv__BusReply_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _BusReply_Request__ros_msg_type * ros_message = static_cast<const _BusReply_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name cmd
  {
    size_t item_size = sizeof(ros_message->cmd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name data_len
  {
    size_t item_size = sizeof(ros_message->data_len);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name data
  {
    size_t array_size = ros_message->data.size;
    auto array_ptr = ros_message->data.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name err
  {
    size_t item_size = sizeof(ros_message->err);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _BusReply_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_pl_interface__srv__BusReply_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pl_interface
size_t max_serialized_size_pl_interface__srv__BusReply_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: cmd
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: data_len
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: data
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: err
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _BusReply_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_pl_interface__srv__BusReply_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_BusReply_Request = {
  "pl_interface::srv",
  "BusReply_Request",
  _BusReply_Request__cdr_serialize,
  _BusReply_Request__cdr_deserialize,
  _BusReply_Request__get_serialized_size,
  _BusReply_Request__max_serialized_size
};

static rosidl_message_type_support_t _BusReply_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_BusReply_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pl_interface, srv, BusReply_Request)() {
  return &_BusReply_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "pl_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "pl_interface/srv/detail/bus_reply__struct.h"
// already included above
// #include "pl_interface/srv/detail/bus_reply__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"  // data
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"  // data

// forward declare type support functions


using _BusReply_Response__ros_msg_type = pl_interface__srv__BusReply_Response;

static bool _BusReply_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _BusReply_Response__ros_msg_type * ros_message = static_cast<const _BusReply_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd
  {
    cdr << ros_message->cmd;
  }

  // Field name: data_len
  {
    cdr << ros_message->data_len;
  }

  // Field name: data
  {
    size_t size = ros_message->data.size;
    auto array_ptr = ros_message->data.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: err
  {
    cdr << ros_message->err;
  }

  return true;
}

static bool _BusReply_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _BusReply_Response__ros_msg_type * ros_message = static_cast<_BusReply_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd
  {
    cdr >> ros_message->cmd;
  }

  // Field name: data_len
  {
    cdr >> ros_message->data_len;
  }

  // Field name: data
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->data.data) {
      rosidl_runtime_c__uint8__Sequence__fini(&ros_message->data);
    }
    if (!rosidl_runtime_c__uint8__Sequence__init(&ros_message->data, size)) {
      fprintf(stderr, "failed to create array for field 'data'");
      return false;
    }
    auto array_ptr = ros_message->data.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: err
  {
    cdr >> ros_message->err;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pl_interface
size_t get_serialized_size_pl_interface__srv__BusReply_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _BusReply_Response__ros_msg_type * ros_message = static_cast<const _BusReply_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name cmd
  {
    size_t item_size = sizeof(ros_message->cmd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name data_len
  {
    size_t item_size = sizeof(ros_message->data_len);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name data
  {
    size_t array_size = ros_message->data.size;
    auto array_ptr = ros_message->data.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name err
  {
    size_t item_size = sizeof(ros_message->err);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _BusReply_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_pl_interface__srv__BusReply_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pl_interface
size_t max_serialized_size_pl_interface__srv__BusReply_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: cmd
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: data_len
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: data
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: err
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _BusReply_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_pl_interface__srv__BusReply_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_BusReply_Response = {
  "pl_interface::srv",
  "BusReply_Response",
  _BusReply_Response__cdr_serialize,
  _BusReply_Response__cdr_deserialize,
  _BusReply_Response__get_serialized_size,
  _BusReply_Response__max_serialized_size
};

static rosidl_message_type_support_t _BusReply_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_BusReply_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pl_interface, srv, BusReply_Response)() {
  return &_BusReply_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "pl_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "pl_interface/srv/bus_reply.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t BusReply__callbacks = {
  "pl_interface::srv",
  "BusReply",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pl_interface, srv, BusReply_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pl_interface, srv, BusReply_Response)(),
};

static rosidl_service_type_support_t BusReply__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &BusReply__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pl_interface, srv, BusReply)() {
  return &BusReply__handle;
}

#if defined(__cplusplus)
}
#endif
