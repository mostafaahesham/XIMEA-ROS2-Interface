// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pl_interface:srv/BusReply.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pl_interface/srv/detail/bus_reply__rosidl_typesupport_introspection_c.h"
#include "pl_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pl_interface/srv/detail/bus_reply__functions.h"
#include "pl_interface/srv/detail/bus_reply__struct.h"


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pl_interface__srv__BusReply_Request__init(message_memory);
}

void pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_fini_function(void * message_memory)
{
  pl_interface__srv__BusReply_Request__fini(message_memory);
}

size_t pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__size_function__BusReply_Request__data(
  const void * untyped_member)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return member->size;
}

const void * pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_const_function__BusReply_Request__data(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_function__BusReply_Request__data(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__fetch_function__BusReply_Request__data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_const_function__BusReply_Request__data(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__assign_function__BusReply_Request__data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_function__BusReply_Request__data(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

bool pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__resize_function__BusReply_Request__data(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  rosidl_runtime_c__uint8__Sequence__fini(member);
  return rosidl_runtime_c__uint8__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_member_array[4] = {
  {
    "cmd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Request, cmd),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data_len",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Request, data_len),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Request, data),  // bytes offset in struct
    NULL,  // default value
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__size_function__BusReply_Request__data,  // size() function pointer
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_const_function__BusReply_Request__data,  // get_const(index) function pointer
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__get_function__BusReply_Request__data,  // get(index) function pointer
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__fetch_function__BusReply_Request__data,  // fetch(index, &value) function pointer
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__assign_function__BusReply_Request__data,  // assign(index, value) function pointer
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__resize_function__BusReply_Request__data  // resize(index) function pointer
  },
  {
    "err",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Request, err),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_members = {
  "pl_interface__srv",  // message namespace
  "BusReply_Request",  // message name
  4,  // number of fields
  sizeof(pl_interface__srv__BusReply_Request),
  pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_member_array,  // message members
  pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_type_support_handle = {
  0,
  &pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pl_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Request)() {
  if (!pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_type_support_handle.typesupport_identifier) {
    pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pl_interface__srv__BusReply_Request__rosidl_typesupport_introspection_c__BusReply_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "pl_interface/srv/detail/bus_reply__rosidl_typesupport_introspection_c.h"
// already included above
// #include "pl_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "pl_interface/srv/detail/bus_reply__functions.h"
// already included above
// #include "pl_interface/srv/detail/bus_reply__struct.h"


// Include directives for member types
// Member `data`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pl_interface__srv__BusReply_Response__init(message_memory);
}

void pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_fini_function(void * message_memory)
{
  pl_interface__srv__BusReply_Response__fini(message_memory);
}

size_t pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__size_function__BusReply_Response__data(
  const void * untyped_member)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return member->size;
}

const void * pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_const_function__BusReply_Response__data(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_function__BusReply_Response__data(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__fetch_function__BusReply_Response__data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_const_function__BusReply_Response__data(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__assign_function__BusReply_Response__data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_function__BusReply_Response__data(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

bool pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__resize_function__BusReply_Response__data(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  rosidl_runtime_c__uint8__Sequence__fini(member);
  return rosidl_runtime_c__uint8__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_member_array[4] = {
  {
    "cmd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Response, cmd),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data_len",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Response, data_len),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Response, data),  // bytes offset in struct
    NULL,  // default value
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__size_function__BusReply_Response__data,  // size() function pointer
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_const_function__BusReply_Response__data,  // get_const(index) function pointer
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__get_function__BusReply_Response__data,  // get(index) function pointer
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__fetch_function__BusReply_Response__data,  // fetch(index, &value) function pointer
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__assign_function__BusReply_Response__data,  // assign(index, value) function pointer
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__resize_function__BusReply_Response__data  // resize(index) function pointer
  },
  {
    "err",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pl_interface__srv__BusReply_Response, err),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_members = {
  "pl_interface__srv",  // message namespace
  "BusReply_Response",  // message name
  4,  // number of fields
  sizeof(pl_interface__srv__BusReply_Response),
  pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_member_array,  // message members
  pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_type_support_handle = {
  0,
  &pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pl_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Response)() {
  if (!pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_type_support_handle.typesupport_identifier) {
    pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pl_interface__srv__BusReply_Response__rosidl_typesupport_introspection_c__BusReply_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "pl_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "pl_interface/srv/detail/bus_reply__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_members = {
  "pl_interface__srv",  // service namespace
  "BusReply",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_Request_message_type_support_handle,
  NULL  // response message
  // pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_Response_message_type_support_handle
};

static rosidl_service_type_support_t pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_type_support_handle = {
  0,
  &pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pl_interface
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply)() {
  if (!pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_type_support_handle.typesupport_identifier) {
    pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pl_interface, srv, BusReply_Response)()->data;
  }

  return &pl_interface__srv__detail__bus_reply__rosidl_typesupport_introspection_c__BusReply_service_type_support_handle;
}
