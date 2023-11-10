// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from pl_interface:msg/BusReply.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_REPLY__FUNCTIONS_H_
#define PL_INTERFACE__MSG__DETAIL__BUS_REPLY__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "pl_interface/msg/rosidl_generator_c__visibility_control.h"

#include "pl_interface/msg/detail/bus_reply__struct.h"

/// Initialize msg/BusReply message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pl_interface__msg__BusReply
 * )) before or use
 * pl_interface__msg__BusReply__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__init(pl_interface__msg__BusReply * msg);

/// Finalize msg/BusReply message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
void
pl_interface__msg__BusReply__fini(pl_interface__msg__BusReply * msg);

/// Create msg/BusReply message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pl_interface__msg__BusReply__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
pl_interface__msg__BusReply *
pl_interface__msg__BusReply__create();

/// Destroy msg/BusReply message.
/**
 * It calls
 * pl_interface__msg__BusReply__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
void
pl_interface__msg__BusReply__destroy(pl_interface__msg__BusReply * msg);

/// Check for msg/BusReply message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__are_equal(const pl_interface__msg__BusReply * lhs, const pl_interface__msg__BusReply * rhs);

/// Copy a msg/BusReply message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__copy(
  const pl_interface__msg__BusReply * input,
  pl_interface__msg__BusReply * output);

/// Initialize array of msg/BusReply messages.
/**
 * It allocates the memory for the number of elements and calls
 * pl_interface__msg__BusReply__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__Sequence__init(pl_interface__msg__BusReply__Sequence * array, size_t size);

/// Finalize array of msg/BusReply messages.
/**
 * It calls
 * pl_interface__msg__BusReply__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
void
pl_interface__msg__BusReply__Sequence__fini(pl_interface__msg__BusReply__Sequence * array);

/// Create array of msg/BusReply messages.
/**
 * It allocates the memory for the array and calls
 * pl_interface__msg__BusReply__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
pl_interface__msg__BusReply__Sequence *
pl_interface__msg__BusReply__Sequence__create(size_t size);

/// Destroy array of msg/BusReply messages.
/**
 * It calls
 * pl_interface__msg__BusReply__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
void
pl_interface__msg__BusReply__Sequence__destroy(pl_interface__msg__BusReply__Sequence * array);

/// Check for msg/BusReply message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__Sequence__are_equal(const pl_interface__msg__BusReply__Sequence * lhs, const pl_interface__msg__BusReply__Sequence * rhs);

/// Copy an array of msg/BusReply messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pl_interface
bool
pl_interface__msg__BusReply__Sequence__copy(
  const pl_interface__msg__BusReply__Sequence * input,
  pl_interface__msg__BusReply__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_REPLY__FUNCTIONS_H_
