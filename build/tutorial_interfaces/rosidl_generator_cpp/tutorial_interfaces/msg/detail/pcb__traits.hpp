// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/pcb.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__PCB__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__PCB__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/pcb__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const PCB & msg,
  std::ostream & out)
{
  out << "{";
  // member: wind_speed
  {
    out << "wind_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.wind_speed, out);
    out << ", ";
  }

  // member: wind_direction
  {
    out << "wind_direction: ";
    rosidl_generator_traits::value_to_yaml(msg.wind_direction, out);
    out << ", ";
  }

  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << ", ";
  }

  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << ", ";
  }

  // member: heading
  {
    out << "heading: ";
    rosidl_generator_traits::value_to_yaml(msg.heading, out);
    out << ", ";
  }

  // member: sail_angle
  {
    out << "sail_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.sail_angle, out);
    out << ", ";
  }

  // member: sailflap_angle
  {
    out << "sailflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.sailflap_angle, out);
    out << ", ";
  }

  // member: backflap_angle
  {
    out << "backflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.backflap_angle, out);
    out << ", ";
  }

  // member: rudder_angle
  {
    out << "rudder_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rudder_angle, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PCB & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: wind_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wind_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.wind_speed, out);
    out << "\n";
  }

  // member: wind_direction
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wind_direction: ";
    rosidl_generator_traits::value_to_yaml(msg.wind_direction, out);
    out << "\n";
  }

  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
  }

  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }

  // member: heading
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "heading: ";
    rosidl_generator_traits::value_to_yaml(msg.heading, out);
    out << "\n";
  }

  // member: sail_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sail_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.sail_angle, out);
    out << "\n";
  }

  // member: sailflap_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sailflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.sailflap_angle, out);
    out << "\n";
  }

  // member: backflap_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "backflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.backflap_angle, out);
    out << "\n";
  }

  // member: rudder_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rudder_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.rudder_angle, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PCB & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::msg::PCB & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::PCB & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::PCB>()
{
  return "tutorial_interfaces::msg::PCB";
}

template<>
inline const char * name<tutorial_interfaces::msg::PCB>()
{
  return "tutorial_interfaces/msg/PCB";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::PCB>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::PCB>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<tutorial_interfaces::msg::PCB>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__PCB__TRAITS_HPP_
