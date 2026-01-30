// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice

#include "tutorial_interfaces/msg/detail/navigation__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
const rosidl_type_hash_t *
tutorial_interfaces__msg__Navigation__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x88, 0x69, 0x29, 0x78, 0x26, 0x14, 0x0a, 0x8e,
      0x42, 0xd1, 0x92, 0x59, 0x12, 0x38, 0xae, 0xd6,
      0x1a, 0xfd, 0x1f, 0x0d, 0x4d, 0xae, 0xd7, 0x46,
      0x22, 0x18, 0x83, 0xa8, 0x66, 0xe7, 0xfb, 0x1a,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char tutorial_interfaces__msg__Navigation__TYPE_NAME[] = "tutorial_interfaces/msg/Navigation";

// Define type names, field names, and default values
static char tutorial_interfaces__msg__Navigation__FIELD_NAME__waypoint_latitude[] = "waypoint_latitude";
static char tutorial_interfaces__msg__Navigation__FIELD_NAME__waypoint_longitude[] = "waypoint_longitude";
static char tutorial_interfaces__msg__Navigation__FIELD_NAME__tacking_waypoint_latitude[] = "tacking_waypoint_latitude";
static char tutorial_interfaces__msg__Navigation__FIELD_NAME__tacking_waypoint_longitude[] = "tacking_waypoint_longitude";
static char tutorial_interfaces__msg__Navigation__FIELD_NAME__target_heading[] = "target_heading";

static rosidl_runtime_c__type_description__Field tutorial_interfaces__msg__Navigation__FIELDS[] = {
  {
    {tutorial_interfaces__msg__Navigation__FIELD_NAME__waypoint_latitude, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Navigation__FIELD_NAME__waypoint_longitude, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Navigation__FIELD_NAME__tacking_waypoint_latitude, 25, 25},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Navigation__FIELD_NAME__tacking_waypoint_longitude, 26, 26},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Navigation__FIELD_NAME__target_heading, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
tutorial_interfaces__msg__Navigation__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {tutorial_interfaces__msg__Navigation__TYPE_NAME, 34, 34},
      {tutorial_interfaces__msg__Navigation__FIELDS, 5, 5},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 waypoint_latitude\n"
  "float64 waypoint_longitude\n"
  "float64 tacking_waypoint_latitude\n"
  "float64 tacking_waypoint_longitude\n"
  "float64 target_heading";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
tutorial_interfaces__msg__Navigation__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {tutorial_interfaces__msg__Navigation__TYPE_NAME, 34, 34},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 145, 145},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
tutorial_interfaces__msg__Navigation__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *tutorial_interfaces__msg__Navigation__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
