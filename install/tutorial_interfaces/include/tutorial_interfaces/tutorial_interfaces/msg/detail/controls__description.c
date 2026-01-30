// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

#include "tutorial_interfaces/msg/detail/controls__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
const rosidl_type_hash_t *
tutorial_interfaces__msg__Controls__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x10, 0xbf, 0x02, 0xfe, 0xd7, 0xd6, 0xac, 0x68,
      0xb0, 0x0a, 0x08, 0xb9, 0xef, 0xf5, 0xd9, 0xc5,
      0xec, 0x01, 0x63, 0x6c, 0x96, 0x7f, 0xbc, 0x81,
      0x67, 0x04, 0x0a, 0x6c, 0xcf, 0x0e, 0xeb, 0x05,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char tutorial_interfaces__msg__Controls__TYPE_NAME[] = "tutorial_interfaces/msg/Controls";

// Define type names, field names, and default values
static char tutorial_interfaces__msg__Controls__FIELD_NAME__target_sail_angle[] = "target_sail_angle";
static char tutorial_interfaces__msg__Controls__FIELD_NAME__target_sailflap_angle[] = "target_sailflap_angle";
static char tutorial_interfaces__msg__Controls__FIELD_NAME__target_backflap_angle[] = "target_backflap_angle";
static char tutorial_interfaces__msg__Controls__FIELD_NAME__target_rudder_angle[] = "target_rudder_angle";

static rosidl_runtime_c__type_description__Field tutorial_interfaces__msg__Controls__FIELDS[] = {
  {
    {tutorial_interfaces__msg__Controls__FIELD_NAME__target_sail_angle, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Controls__FIELD_NAME__target_sailflap_angle, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Controls__FIELD_NAME__target_backflap_angle, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {tutorial_interfaces__msg__Controls__FIELD_NAME__target_rudder_angle, 19, 19},
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
tutorial_interfaces__msg__Controls__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {tutorial_interfaces__msg__Controls__TYPE_NAME, 32, 32},
      {tutorial_interfaces__msg__Controls__FIELDS, 4, 4},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 target_sail_angle\n"
  "float64 target_sailflap_angle\n"
  "float64 target_backflap_angle\n"
  "float64 target_rudder_angle\n"
  "";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
tutorial_interfaces__msg__Controls__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {tutorial_interfaces__msg__Controls__TYPE_NAME, 32, 32},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 115, 115},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
tutorial_interfaces__msg__Controls__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *tutorial_interfaces__msg__Controls__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
