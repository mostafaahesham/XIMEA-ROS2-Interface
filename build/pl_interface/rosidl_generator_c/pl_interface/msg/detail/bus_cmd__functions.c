// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pl_interface:msg/BusCmd.idl
// generated code does not contain a copyright notice
#include "pl_interface/msg/detail/bus_cmd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
pl_interface__msg__BusCmd__init(pl_interface__msg__BusCmd * msg)
{
  if (!msg) {
    return false;
  }
  // src
  // cmd
  // data_len
  // data
  if (!rosidl_runtime_c__uint8__Sequence__init(&msg->data, 0)) {
    pl_interface__msg__BusCmd__fini(msg);
    return false;
  }
  return true;
}

void
pl_interface__msg__BusCmd__fini(pl_interface__msg__BusCmd * msg)
{
  if (!msg) {
    return;
  }
  // src
  // cmd
  // data_len
  // data
  rosidl_runtime_c__uint8__Sequence__fini(&msg->data);
}

bool
pl_interface__msg__BusCmd__are_equal(const pl_interface__msg__BusCmd * lhs, const pl_interface__msg__BusCmd * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // src
  if (lhs->src != rhs->src) {
    return false;
  }
  // cmd
  if (lhs->cmd != rhs->cmd) {
    return false;
  }
  // data_len
  if (lhs->data_len != rhs->data_len) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__uint8__Sequence__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  return true;
}

bool
pl_interface__msg__BusCmd__copy(
  const pl_interface__msg__BusCmd * input,
  pl_interface__msg__BusCmd * output)
{
  if (!input || !output) {
    return false;
  }
  // src
  output->src = input->src;
  // cmd
  output->cmd = input->cmd;
  // data_len
  output->data_len = input->data_len;
  // data
  if (!rosidl_runtime_c__uint8__Sequence__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  return true;
}

pl_interface__msg__BusCmd *
pl_interface__msg__BusCmd__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pl_interface__msg__BusCmd * msg = (pl_interface__msg__BusCmd *)allocator.allocate(sizeof(pl_interface__msg__BusCmd), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pl_interface__msg__BusCmd));
  bool success = pl_interface__msg__BusCmd__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pl_interface__msg__BusCmd__destroy(pl_interface__msg__BusCmd * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pl_interface__msg__BusCmd__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pl_interface__msg__BusCmd__Sequence__init(pl_interface__msg__BusCmd__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pl_interface__msg__BusCmd * data = NULL;

  if (size) {
    data = (pl_interface__msg__BusCmd *)allocator.zero_allocate(size, sizeof(pl_interface__msg__BusCmd), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pl_interface__msg__BusCmd__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pl_interface__msg__BusCmd__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pl_interface__msg__BusCmd__Sequence__fini(pl_interface__msg__BusCmd__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pl_interface__msg__BusCmd__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pl_interface__msg__BusCmd__Sequence *
pl_interface__msg__BusCmd__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pl_interface__msg__BusCmd__Sequence * array = (pl_interface__msg__BusCmd__Sequence *)allocator.allocate(sizeof(pl_interface__msg__BusCmd__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pl_interface__msg__BusCmd__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pl_interface__msg__BusCmd__Sequence__destroy(pl_interface__msg__BusCmd__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pl_interface__msg__BusCmd__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pl_interface__msg__BusCmd__Sequence__are_equal(const pl_interface__msg__BusCmd__Sequence * lhs, const pl_interface__msg__BusCmd__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pl_interface__msg__BusCmd__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pl_interface__msg__BusCmd__Sequence__copy(
  const pl_interface__msg__BusCmd__Sequence * input,
  pl_interface__msg__BusCmd__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pl_interface__msg__BusCmd);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pl_interface__msg__BusCmd * data =
      (pl_interface__msg__BusCmd *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pl_interface__msg__BusCmd__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pl_interface__msg__BusCmd__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pl_interface__msg__BusCmd__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
