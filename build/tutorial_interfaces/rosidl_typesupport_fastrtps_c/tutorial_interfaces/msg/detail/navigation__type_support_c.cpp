// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/detail/navigation__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "tutorial_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "tutorial_interfaces/msg/detail/navigation__struct.h"
#include "tutorial_interfaces/msg/detail/navigation__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Navigation__ros_msg_type = tutorial_interfaces__msg__Navigation;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
bool cdr_serialize_tutorial_interfaces__msg__Navigation(
  const tutorial_interfaces__msg__Navigation * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: waypoint_latitude
  {
    cdr << ros_message->waypoint_latitude;
  }

  // Field name: waypoint_longitude
  {
    cdr << ros_message->waypoint_longitude;
  }

  // Field name: tacking_waypoint_latitude
  {
    cdr << ros_message->tacking_waypoint_latitude;
  }

  // Field name: tacking_waypoint_longitude
  {
    cdr << ros_message->tacking_waypoint_longitude;
  }

  // Field name: target_heading
  {
    cdr << ros_message->target_heading;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
bool cdr_deserialize_tutorial_interfaces__msg__Navigation(
  eprosima::fastcdr::Cdr & cdr,
  tutorial_interfaces__msg__Navigation * ros_message)
{
  // Field name: waypoint_latitude
  {
    cdr >> ros_message->waypoint_latitude;
  }

  // Field name: waypoint_longitude
  {
    cdr >> ros_message->waypoint_longitude;
  }

  // Field name: tacking_waypoint_latitude
  {
    cdr >> ros_message->tacking_waypoint_latitude;
  }

  // Field name: tacking_waypoint_longitude
  {
    cdr >> ros_message->tacking_waypoint_longitude;
  }

  // Field name: target_heading
  {
    cdr >> ros_message->target_heading;
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t get_serialized_size_tutorial_interfaces__msg__Navigation(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Navigation__ros_msg_type * ros_message = static_cast<const _Navigation__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: waypoint_latitude
  {
    size_t item_size = sizeof(ros_message->waypoint_latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: waypoint_longitude
  {
    size_t item_size = sizeof(ros_message->waypoint_longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: tacking_waypoint_latitude
  {
    size_t item_size = sizeof(ros_message->tacking_waypoint_latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: tacking_waypoint_longitude
  {
    size_t item_size = sizeof(ros_message->tacking_waypoint_longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: target_heading
  {
    size_t item_size = sizeof(ros_message->target_heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t max_serialized_size_tutorial_interfaces__msg__Navigation(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // Field name: waypoint_latitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: waypoint_longitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: tacking_waypoint_latitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: tacking_waypoint_longitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: target_heading
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }


  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = tutorial_interfaces__msg__Navigation;
    is_plain =
      (
      offsetof(DataType, target_heading) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
bool cdr_serialize_key_tutorial_interfaces__msg__Navigation(
  const tutorial_interfaces__msg__Navigation * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: waypoint_latitude
  {
    cdr << ros_message->waypoint_latitude;
  }

  // Field name: waypoint_longitude
  {
    cdr << ros_message->waypoint_longitude;
  }

  // Field name: tacking_waypoint_latitude
  {
    cdr << ros_message->tacking_waypoint_latitude;
  }

  // Field name: tacking_waypoint_longitude
  {
    cdr << ros_message->tacking_waypoint_longitude;
  }

  // Field name: target_heading
  {
    cdr << ros_message->target_heading;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t get_serialized_size_key_tutorial_interfaces__msg__Navigation(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Navigation__ros_msg_type * ros_message = static_cast<const _Navigation__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: waypoint_latitude
  {
    size_t item_size = sizeof(ros_message->waypoint_latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: waypoint_longitude
  {
    size_t item_size = sizeof(ros_message->waypoint_longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: tacking_waypoint_latitude
  {
    size_t item_size = sizeof(ros_message->tacking_waypoint_latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: tacking_waypoint_longitude
  {
    size_t item_size = sizeof(ros_message->tacking_waypoint_longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: target_heading
  {
    size_t item_size = sizeof(ros_message->target_heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t max_serialized_size_key_tutorial_interfaces__msg__Navigation(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;
  // Field name: waypoint_latitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: waypoint_longitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: tacking_waypoint_latitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: tacking_waypoint_longitude
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: target_heading
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = tutorial_interfaces__msg__Navigation;
    is_plain =
      (
      offsetof(DataType, target_heading) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _Navigation__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const tutorial_interfaces__msg__Navigation * ros_message = static_cast<const tutorial_interfaces__msg__Navigation *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_tutorial_interfaces__msg__Navigation(ros_message, cdr);
}

static bool _Navigation__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  tutorial_interfaces__msg__Navigation * ros_message = static_cast<tutorial_interfaces__msg__Navigation *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_tutorial_interfaces__msg__Navigation(cdr, ros_message);
}

static uint32_t _Navigation__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_tutorial_interfaces__msg__Navigation(
      untyped_ros_message, 0));
}

static size_t _Navigation__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_tutorial_interfaces__msg__Navigation(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Navigation = {
  "tutorial_interfaces::msg",
  "Navigation",
  _Navigation__cdr_serialize,
  _Navigation__cdr_deserialize,
  _Navigation__get_serialized_size,
  _Navigation__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _Navigation__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Navigation,
  get_message_typesupport_handle_function,
  &tutorial_interfaces__msg__Navigation__get_type_hash,
  &tutorial_interfaces__msg__Navigation__get_type_description,
  &tutorial_interfaces__msg__Navigation__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, tutorial_interfaces, msg, Navigation)() {
  return &_Navigation__type_support;
}

#if defined(__cplusplus)
}
#endif
