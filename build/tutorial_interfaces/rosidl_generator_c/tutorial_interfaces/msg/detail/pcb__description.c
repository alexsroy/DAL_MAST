// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice

#include "tutorial_interfaces/msg/detail/pcb__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
const rosidl_type_hash_t *
tutorial_interfaces__msg__PCB__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x70, 0x91, 0xfb, 0x30, 0x43, 0x50, 0x3f, 0x05,
      0xd3, 0xa4, 0xd3, 0x44, 0xaf, 0x76, 0xab, 0xbb,
      0x46, 0x58, 0x12, 0x40, 0x60, 0x33, 0x36, 0xfe,
      0x36, 0x2b, 0x9f, 0x71, 0x0c, 0xdf, 0x16, 0x90,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char tutorial_interfaces__msg__PCB__TYPE_NAME[] = "tutorial_interfaces/msg/PCB";

// Define type names, field names, and default values
static char tutorial_interfaces__msg__PCB__FIELD_NAME__wind_speed[] = "wind_speed";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__wind_direction[] = "wind_direction";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__roll[] = "roll";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__pitch[] = "pitch";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__yaw[] = "yaw";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__latitude[] = "latitude";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__longitude[] = "longitude";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__heading[] = "heading";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__sail_angle[] = "sail_angle";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__sailflap_angle[] = "sailflap_angle";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__backflap_angle[] = "backflap_angle";
static char tutorial_interfaces__msg__PCB__FIELD_NAME__rudder_angle[] = "rudder_angle";

static rosidl_runtime_c__type_description__Field tutorial_interfaces__msg__PCB__FIELDS[] = {
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__wind_speed, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__wind_direction, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__roll, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__pitch, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__yaw, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__latitude, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__longitude, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__heading, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__sail_angle, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__sailflap_angle, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__backflap_angle, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__PCB__FIELD_NAME__rudder_angle, 12, 12},
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
tutorial_interfaces__msg__PCB__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {tutorial_interfaces__msg__PCB__TYPE_NAME, 27, 27},
      {tutorial_interfaces__msg__PCB__FIELDS, 12, 12},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 wind_speed\n"
  "float64 wind_direction\n"
  "float64 roll\n"
  "float64 pitch\n"
  "float64 yaw\n"
  "float64 latitude\n"
  "float64 longitude\n"
  "float64 heading\n"
  "float64 sail_angle\n"
  "float64 sailflap_angle\n"
  "float64 backflap_angle\n"
  "float64 rudder_angle\n"
  "";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
tutorial_interfaces__msg__PCB__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {tutorial_interfaces__msg__PCB__TYPE_NAME, 27, 27},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 219, 219},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
tutorial_interfaces__msg__PCB__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *tutorial_interfaces__msg__PCB__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
