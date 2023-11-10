// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pl_interface:srv/BusReply.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_H_
#define PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/BusReply in the package pl_interface.
typedef struct pl_interface__srv__BusReply_Request
{
  uint8_t cmd;
  uint8_t data_len;
  rosidl_runtime_c__uint8__Sequence data;
  uint8_t err;
} pl_interface__srv__BusReply_Request;

// Struct for a sequence of pl_interface__srv__BusReply_Request.
typedef struct pl_interface__srv__BusReply_Request__Sequence
{
  pl_interface__srv__BusReply_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pl_interface__srv__BusReply_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'data'
// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/BusReply in the package pl_interface.
typedef struct pl_interface__srv__BusReply_Response
{
  uint8_t cmd;
  uint8_t data_len;
  rosidl_runtime_c__uint8__Sequence data;
  uint8_t err;
} pl_interface__srv__BusReply_Response;

// Struct for a sequence of pl_interface__srv__BusReply_Response.
typedef struct pl_interface__srv__BusReply_Response__Sequence
{
  pl_interface__srv__BusReply_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pl_interface__srv__BusReply_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_H_
