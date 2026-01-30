// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/pcb.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__PCB __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__PCB __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PCB_
{
  using Type = PCB_<ContainerAllocator>;

  explicit PCB_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->wind_speed = 0.0;
      this->wind_direction = 0.0;
      this->roll = 0.0;
      this->pitch = 0.0;
      this->yaw = 0.0;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->heading = 0.0;
      this->sail_angle = 0.0;
      this->sailflap_angle = 0.0;
      this->backflap_angle = 0.0;
      this->rudder_angle = 0.0;
    }
  }

  explicit PCB_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->wind_speed = 0.0;
      this->wind_direction = 0.0;
      this->roll = 0.0;
      this->pitch = 0.0;
      this->yaw = 0.0;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->heading = 0.0;
      this->sail_angle = 0.0;
      this->sailflap_angle = 0.0;
      this->backflap_angle = 0.0;
      this->rudder_angle = 0.0;
    }
  }

  // field types and members
  using _wind_speed_type =
    double;
  _wind_speed_type wind_speed;
  using _wind_direction_type =
    double;
  _wind_direction_type wind_direction;
  using _roll_type =
    double;
  _roll_type roll;
  using _pitch_type =
    double;
  _pitch_type pitch;
  using _yaw_type =
    double;
  _yaw_type yaw;
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _longitude_type =
    double;
  _longitude_type longitude;
  using _heading_type =
    double;
  _heading_type heading;
  using _sail_angle_type =
    double;
  _sail_angle_type sail_angle;
  using _sailflap_angle_type =
    double;
  _sailflap_angle_type sailflap_angle;
  using _backflap_angle_type =
    double;
  _backflap_angle_type backflap_angle;
  using _rudder_angle_type =
    double;
  _rudder_angle_type rudder_angle;

  // setters for named parameter idiom
  Type & set__wind_speed(
    const double & _arg)
  {
    this->wind_speed = _arg;
    return *this;
  }
  Type & set__wind_direction(
    const double & _arg)
  {
    this->wind_direction = _arg;
    return *this;
  }
  Type & set__roll(
    const double & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const double & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__yaw(
    const double & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__heading(
    const double & _arg)
  {
    this->heading = _arg;
    return *this;
  }
  Type & set__sail_angle(
    const double & _arg)
  {
    this->sail_angle = _arg;
    return *this;
  }
  Type & set__sailflap_angle(
    const double & _arg)
  {
    this->sailflap_angle = _arg;
    return *this;
  }
  Type & set__backflap_angle(
    const double & _arg)
  {
    this->backflap_angle = _arg;
    return *this;
  }
  Type & set__rudder_angle(
    const double & _arg)
  {
    this->rudder_angle = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::PCB_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::PCB_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::PCB_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::PCB_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__PCB
    std::shared_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__PCB
    std::shared_ptr<tutorial_interfaces::msg::PCB_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PCB_ & other) const
  {
    if (this->wind_speed != other.wind_speed) {
      return false;
    }
    if (this->wind_direction != other.wind_direction) {
      return false;
    }
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->heading != other.heading) {
      return false;
    }
    if (this->sail_angle != other.sail_angle) {
      return false;
    }
    if (this->sailflap_angle != other.sailflap_angle) {
      return false;
    }
    if (this->backflap_angle != other.backflap_angle) {
      return false;
    }
    if (this->rudder_angle != other.rudder_angle) {
      return false;
    }
    return true;
  }
  bool operator!=(const PCB_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PCB_

// alias to use template instance with default allocator
using PCB =
  tutorial_interfaces::msg::PCB_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__PCB__STRUCT_HPP_
