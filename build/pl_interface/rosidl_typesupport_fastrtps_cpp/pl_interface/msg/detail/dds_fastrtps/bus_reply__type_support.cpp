// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from pl_interface:msg/BusReply.idl
// generated code does not contain a copyright notice
#include "pl_interface/msg/detail/bus_reply__rosidl_typesupport_fastrtps_cpp.hpp"
#include "pl_interface/msg/detail/bus_reply__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace pl_interface
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pl_interface
cdr_serialize(
  const pl_interface::msg::BusReply & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: dest
  cdr << ros_message.dest;
  // Member: cmd
  cdr << ros_message.cmd;
  // Member: data_len
  cdr << ros_message.data_len;
  // Member: data
  {
    cdr << ros_message.data;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pl_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  pl_interface::msg::BusReply & ros_message)
{
  // Member: dest
  cdr >> ros_message.dest;

  // Member: cmd
  cdr >> ros_message.cmd;

  // Member: data_len
  cdr >> ros_message.data_len;

  // Member: data
  {
    cdr >> ros_message.data;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pl_interface
get_serialized_size(
  const pl_interface::msg::BusReply & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: dest
  {
    size_t item_size = sizeof(ros_message.dest);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cmd
  {
    size_t item_size = sizeof(ros_message.cmd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: data_len
  {
    size_t item_size = sizeof(ros_message.data_len);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: data
  {
    size_t array_size = ros_message.data.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.data[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pl_interface
max_serialized_size_BusReply(
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


  // Member: dest
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: cmd
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: data_len
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: data
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _BusReply__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const pl_interface::msg::BusReply *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _BusReply__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<pl_interface::msg::BusReply *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _BusReply__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const pl_interface::msg::BusReply *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _BusReply__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_BusReply(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _BusReply__callbacks = {
  "pl_interface::msg",
  "BusReply",
  _BusReply__cdr_serialize,
  _BusReply__cdr_deserialize,
  _BusReply__get_serialized_size,
  _BusReply__max_serialized_size
};

static rosidl_message_type_support_t _BusReply__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_BusReply__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace pl_interface

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_pl_interface
const rosidl_message_type_support_t *
get_message_type_support_handle<pl_interface::msg::BusReply>()
{
  return &pl_interface::msg::typesupport_fastrtps_cpp::_BusReply__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pl_interface, msg, BusReply)() {
  return &pl_interface::msg::typesupport_fastrtps_cpp::_BusReply__handle;
}

#ifdef __cplusplus
}
#endif
