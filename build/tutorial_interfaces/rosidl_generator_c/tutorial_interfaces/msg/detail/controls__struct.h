// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/controls.h"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Controls in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__Controls
{
  double target_sail_angle;
  double target_sailflap_angle;
  double target_backflap_angle;
  double target_rudder_angle;
} tutorial_interfaces__msg__Controls;

// Struct for a sequence of tutorial_interfaces__msg__Controls.
typedef struct tutorial_interfaces__msg__Controls__Sequence
{
  tutorial_interfaces__msg__Controls * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__Controls__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_H_
