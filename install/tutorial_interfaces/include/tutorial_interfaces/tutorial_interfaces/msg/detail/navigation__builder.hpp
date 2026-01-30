// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/navigation.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/navigation__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_Navigation_target_heading
{
public:
  explicit Init_Navigation_target_heading(::tutorial_interfaces::msg::Navigation & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::Navigation target_heading(::tutorial_interfaces::msg::Navigation::_target_heading_type arg)
  {
    msg_.target_heading = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::Navigation msg_;
};

class Init_Navigation_tacking_waypoint_longitude
{
public:
  explicit Init_Navigation_tacking_waypoint_longitude(::tutorial_interfaces::msg::Navigation & msg)
  : msg_(msg)
  {}
  Init_Navigation_target_heading tacking_waypoint_longitude(::tutorial_interfaces::msg::Navigation::_tacking_waypoint_longitude_type arg)
  {
    msg_.tacking_waypoint_longitude = std::move(arg);
    return Init_Navigation_target_heading(msg_);
  }

private:
  ::tutorial_interfaces::msg::Navigation msg_;
};

class Init_Navigation_tacking_waypoint_latitude
{
public:
  explicit Init_Navigation_tacking_waypoint_latitude(::tutorial_interfaces::msg::Navigation & msg)
  : msg_(msg)
  {}
  Init_Navigation_tacking_waypoint_longitude tacking_waypoint_latitude(::tutorial_interfaces::msg::Navigation::_tacking_waypoint_latitude_type arg)
  {
    msg_.tacking_waypoint_latitude = std::move(arg);
    return Init_Navigation_tacking_waypoint_longitude(msg_);
  }

private:
  ::tutorial_interfaces::msg::Navigation msg_;
};

class Init_Navigation_waypoint_longitude
{
public:
  explicit Init_Navigation_waypoint_longitude(::tutorial_interfaces::msg::Navigation & msg)
  : msg_(msg)
  {}
  Init_Navigation_tacking_waypoint_latitude waypoint_longitude(::tutorial_interfaces::msg::Navigation::_waypoint_longitude_type arg)
  {
    msg_.waypoint_longitude = std::move(arg);
    return Init_Navigation_tacking_waypoint_latitude(msg_);
  }

private:
  ::tutorial_interfaces::msg::Navigation msg_;
};

class Init_Navigation_waypoint_latitude
{
public:
  Init_Navigation_waypoint_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Navigation_waypoint_longitude waypoint_latitude(::tutorial_interfaces::msg::Navigation::_waypoint_latitude_type arg)
  {
    msg_.waypoint_latitude = std::move(arg);
    return Init_Navigation_waypoint_longitude(msg_);
  }

private:
  ::tutorial_interfaces::msg::Navigation msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::Navigation>()
{
  return tutorial_interfaces::msg::builder::Init_Navigation_waypoint_latitude();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__BUILDER_HPP_
