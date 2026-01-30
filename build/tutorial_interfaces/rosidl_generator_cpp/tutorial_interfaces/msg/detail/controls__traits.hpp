// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/controls.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/controls__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Controls & msg,
  std::ostream & out)
{
  out << "{";
  // member: target_sail_angle
  {
    out << "target_sail_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_sail_angle, out);
    out << ", ";
  }

  // member: target_sailflap_angle
  {
    out << "target_sailflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_sailflap_angle, out);
    out << ", ";
  }

  // member: target_backflap_angle
  {
    out << "target_backflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_backflap_angle, out);
    out << ", ";
  }

  // member: target_rudder_angle
  {
    out << "target_rudder_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_rudder_angle, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Controls & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target_sail_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_sail_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_sail_angle, out);
    out << "\n";
  }

  // member: target_sailflap_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_sailflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_sailflap_angle, out);
    out << "\n";
  }

  // member: target_backflap_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_backflap_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_backflap_angle, out);
    out << "\n";
  }

  // member: target_rudder_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_rudder_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.target_rudder_angle, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Controls & msg, bool use_flow_style = false)
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
  const tutorial_interfaces::msg::Controls & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::Controls & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::Controls>()
{
  return "tutorial_interfaces::msg::Controls";
}

template<>
inline const char * name<tutorial_interfaces::msg::Controls>()
{
  return "tutorial_interfaces/msg/Controls";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::Controls>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::Controls>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<tutorial_interfaces::msg::Controls>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__TRAITS_HPP_
