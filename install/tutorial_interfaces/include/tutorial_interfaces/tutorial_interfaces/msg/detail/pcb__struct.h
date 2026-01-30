// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/pcb.h"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/PCB in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__PCB
{
  double wind_speed;
  double wind_direction;
  double roll;
  double pitch;
  double yaw;
  double latitude;
  double longitude;
  double heading;
  double sail_angle;
  double sailflap_angle;
  double backflap_angle;
  double rudder_angle;
} tutorial_interfaces__msg__PCB;

// Struct for a sequence of tutorial_interfaces__msg__PCB.
typedef struct tutorial_interfaces__msg__PCB__Sequence
{
  tutorial_interfaces__msg__PCB * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__PCB__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_H_
