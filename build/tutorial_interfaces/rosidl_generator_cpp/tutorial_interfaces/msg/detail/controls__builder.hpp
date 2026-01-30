// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/controls.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/controls__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_Controls_target_rudder_angle
{
public:
  explicit Init_Controls_target_rudder_angle(::tutorial_interfaces::msg::Controls & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::Controls target_rudder_angle(::tutorial_interfaces::msg::Controls::_target_rudder_angle_type arg)
  {
    msg_.target_rudder_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::Controls msg_;
};

class Init_Controls_target_backflap_angle
{
public:
  explicit Init_Controls_target_backflap_angle(::tutorial_interfaces::msg::Controls & msg)
  : msg_(msg)
  {}
  Init_Controls_target_rudder_angle target_backflap_angle(::tutorial_interfaces::msg::Controls::_target_backflap_angle_type arg)
  {
    msg_.target_backflap_angle = std::move(arg);
    return Init_Controls_target_rudder_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::Controls msg_;
};

class Init_Controls_target_sailflap_angle
{
public:
  explicit Init_Controls_target_sailflap_angle(::tutorial_interfaces::msg::Controls & msg)
  : msg_(msg)
  {}
  Init_Controls_target_backflap_angle target_sailflap_angle(::tutorial_interfaces::msg::Controls::_target_sailflap_angle_type arg)
  {
    msg_.target_sailflap_angle = std::move(arg);
    return Init_Controls_target_backflap_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::Controls msg_;
};

class Init_Controls_target_sail_angle
{
public:
  Init_Controls_target_sail_angle()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Controls_target_sailflap_angle target_sail_angle(::tutorial_interfaces::msg::Controls::_target_sail_angle_type arg)
  {
    msg_.target_sail_angle = std::move(arg);
    return Init_Controls_target_sailflap_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::Controls msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::Controls>()
{
  return tutorial_interfaces::msg::builder::Init_Controls_target_sail_angle();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__BUILDER_HPP_
