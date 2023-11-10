// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pl_interface:msg/BusCmd.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_H_
#define PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_H_

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

/// Struct defined in msg/BusCmd in the package pl_interface.
typedef struct pl_interface__msg__BusCmd
{
  uint8_t src;
  uint8_t cmd;
  uint8_t data_len;
  rosidl_runtime_c__uint8__Sequence data;
} pl_interface__msg__BusCmd;

// Struct for a sequence of pl_interface__msg__BusCmd.
typedef struct pl_interface__msg__BusCmd__Sequence
{
  pl_interface__msg__BusCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pl_interface__msg__BusCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_H_
