// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/navigation.h"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Navigation in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__Navigation
{
  double waypoint_latitude;
  double waypoint_longitude;
  double tacking_waypoint_latitude;
  double tacking_waypoint_longitude;
  double target_heading;
} tutorial_interfaces__msg__Navigation;

// Struct for a sequence of tutorial_interfaces__msg__Navigation.
typedef struct tutorial_interfaces__msg__Navigation__Sequence
{
  tutorial_interfaces__msg__Navigation * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__Navigation__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_H_
