// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/navigation.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/navigation__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Navigation & msg,
  std::ostream & out)
{
  out << "{";
  // member: waypoint_latitude
  {
    out << "waypoint_latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_latitude, out);
    out << ", ";
  }

  // member: waypoint_longitude
  {
    out << "waypoint_longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_longitude, out);
    out << ", ";
  }

  // member: tacking_waypoint_latitude
  {
    out << "tacking_waypoint_latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.tacking_waypoint_latitude, out);
    out << ", ";
  }

  // member: tacking_waypoint_longitude
  {
    out << "tacking_waypoint_longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.tacking_waypoint_longitude, out);
    out << ", ";
  }

  // member: target_heading
  {
    out << "target_heading: ";
    rosidl_generator_traits::value_to_yaml(msg.target_heading, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Navigation & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: waypoint_latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_latitude, out);
    out << "\n";
  }

  // member: waypoint_longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_longitude, out);
    out << "\n";
  }

  // member: tacking_waypoint_latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tacking_waypoint_latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.tacking_waypoint_latitude, out);
    out << "\n";
  }

  // member: tacking_waypoint_longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tacking_waypoint_longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.tacking_waypoint_longitude, out);
    out << "\n";
  }

  // member: target_heading
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_heading: ";
    rosidl_generator_traits::value_to_yaml(msg.target_heading, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Navigation & msg, bool use_flow_style = false)
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
  const tutorial_interfaces::msg::Navigation & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::Navigation & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::Navigation>()
{
  return "tutorial_interfaces::msg::Navigation";
}

template<>
inline const char * name<tutorial_interfaces::msg::Navigation>()
{
  return "tutorial_interfaces/msg/Navigation";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::Navigation>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::Navigation>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<tutorial_interfaces::msg::Navigation>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__TRAITS_HPP_
