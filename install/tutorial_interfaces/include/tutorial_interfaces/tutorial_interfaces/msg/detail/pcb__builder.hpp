// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/pcb.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__PCB__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__PCB__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/pcb__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_PCB_rudder_angle
{
public:
  explicit Init_PCB_rudder_angle(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::PCB rudder_angle(::tutorial_interfaces::msg::PCB::_rudder_angle_type arg)
  {
    msg_.rudder_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_backflap_angle
{
public:
  explicit Init_PCB_backflap_angle(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_rudder_angle backflap_angle(::tutorial_interfaces::msg::PCB::_backflap_angle_type arg)
  {
    msg_.backflap_angle = std::move(arg);
    return Init_PCB_rudder_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_sailflap_angle
{
public:
  explicit Init_PCB_sailflap_angle(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_backflap_angle sailflap_angle(::tutorial_interfaces::msg::PCB::_sailflap_angle_type arg)
  {
    msg_.sailflap_angle = std::move(arg);
    return Init_PCB_backflap_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_sail_angle
{
public:
  explicit Init_PCB_sail_angle(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_sailflap_angle sail_angle(::tutorial_interfaces::msg::PCB::_sail_angle_type arg)
  {
    msg_.sail_angle = std::move(arg);
    return Init_PCB_sailflap_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_heading
{
public:
  explicit Init_PCB_heading(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_sail_angle heading(::tutorial_interfaces::msg::PCB::_heading_type arg)
  {
    msg_.heading = std::move(arg);
    return Init_PCB_sail_angle(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_longitude
{
public:
  explicit Init_PCB_longitude(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_heading longitude(::tutorial_interfaces::msg::PCB::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_PCB_heading(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_latitude
{
public:
  explicit Init_PCB_latitude(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_longitude latitude(::tutorial_interfaces::msg::PCB::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_PCB_longitude(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_yaw
{
public:
  explicit Init_PCB_yaw(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_latitude yaw(::tutorial_interfaces::msg::PCB::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_PCB_latitude(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_pitch
{
public:
  explicit Init_PCB_pitch(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_yaw pitch(::tutorial_interfaces::msg::PCB::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_PCB_yaw(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_roll
{
public:
  explicit Init_PCB_roll(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_pitch roll(::tutorial_interfaces::msg::PCB::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_PCB_pitch(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_wind_direction
{
public:
  explicit Init_PCB_wind_direction(::tutorial_interfaces::msg::PCB & msg)
  : msg_(msg)
  {}
  Init_PCB_roll wind_direction(::tutorial_interfaces::msg::PCB::_wind_direction_type arg)
  {
    msg_.wind_direction = std::move(arg);
    return Init_PCB_roll(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

class Init_PCB_wind_speed
{
public:
  Init_PCB_wind_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PCB_wind_direction wind_speed(::tutorial_interfaces::msg::PCB::_wind_speed_type arg)
  {
    msg_.wind_speed = std::move(arg);
    return Init_PCB_wind_direction(msg_);
  }

private:
  ::tutorial_interfaces::msg::PCB msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::PCB>()
{
  return tutorial_interfaces::msg::builder::Init_PCB_wind_speed();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__PCB__BUILDER_HPP_
