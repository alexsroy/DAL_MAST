// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "tutorial_interfaces/msg/detail/controls__rosidl_typesupport_introspection_c.h"
#include "tutorial_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "tutorial_interfaces/msg/detail/controls__functions.h"
#include "tutorial_interfaces/msg/detail/controls__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  tutorial_interfaces__msg__Controls__init(message_memory);
}

void tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_fini_function(void * message_memory)
{
  tutorial_interfaces__msg__Controls__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_member_array[4] = {
  {
    "target_sail_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(tutorial_interfaces__msg__Controls, target_sail_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "target_sailflap_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(tutorial_interfaces__msg__Controls, target_sailflap_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "target_backflap_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(tutorial_interfaces__msg__Controls, target_backflap_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "target_rudder_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(tutorial_interfaces__msg__Controls, target_rudder_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_members = {
  "tutorial_interfaces__msg",  // message namespace
  "Controls",  // message name
  4,  // number of fields
  sizeof(tutorial_interfaces__msg__Controls),
  false,  // has_any_key_member_
  tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_member_array,  // message members
  tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_init_function,  // function to initialize message memory (memory has to be allocated)
  tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_type_support_handle = {
  0,
  &tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_members,
  get_message_typesupport_handle_function,
  &tutorial_interfaces__msg__Controls__get_type_hash,
  &tutorial_interfaces__msg__Controls__get_type_description,
  &tutorial_interfaces__msg__Controls__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_tutorial_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, tutorial_interfaces, msg, Controls)() {
  if (!tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_type_support_handle.typesupport_identifier) {
    tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &tutorial_interfaces__msg__Controls__rosidl_typesupport_introspection_c__Controls_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
