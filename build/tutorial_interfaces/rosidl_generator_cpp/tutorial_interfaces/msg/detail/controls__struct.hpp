// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/controls.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__Controls __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__Controls __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Controls_
{
  using Type = Controls_<ContainerAllocator>;

  explicit Controls_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_sail_angle = 0.0;
      this->target_sailflap_angle = 0.0;
      this->target_backflap_angle = 0.0;
      this->target_rudder_angle = 0.0;
    }
  }

  explicit Controls_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_sail_angle = 0.0;
      this->target_sailflap_angle = 0.0;
      this->target_backflap_angle = 0.0;
      this->target_rudder_angle = 0.0;
    }
  }

  // field types and members
  using _target_sail_angle_type =
    double;
  _target_sail_angle_type target_sail_angle;
  using _target_sailflap_angle_type =
    double;
  _target_sailflap_angle_type target_sailflap_angle;
  using _target_backflap_angle_type =
    double;
  _target_backflap_angle_type target_backflap_angle;
  using _target_rudder_angle_type =
    double;
  _target_rudder_angle_type target_rudder_angle;

  // setters for named parameter idiom
  Type & set__target_sail_angle(
    const double & _arg)
  {
    this->target_sail_angle = _arg;
    return *this;
  }
  Type & set__target_sailflap_angle(
    const double & _arg)
  {
    this->target_sailflap_angle = _arg;
    return *this;
  }
  Type & set__target_backflap_angle(
    const double & _arg)
  {
    this->target_backflap_angle = _arg;
    return *this;
  }
  Type & set__target_rudder_angle(
    const double & _arg)
  {
    this->target_rudder_angle = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::Controls_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::Controls_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::Controls_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::Controls_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__Controls
    std::shared_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__Controls
    std::shared_ptr<tutorial_interfaces::msg::Controls_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Controls_ & other) const
  {
    if (this->target_sail_angle != other.target_sail_angle) {
      return false;
    }
    if (this->target_sailflap_angle != other.target_sailflap_angle) {
      return false;
    }
    if (this->target_backflap_angle != other.target_backflap_angle) {
      return false;
    }
    if (this->target_rudder_angle != other.target_rudder_angle) {
      return false;
    }
    return true;
  }
  bool operator!=(const Controls_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Controls_

// alias to use template instance with default allocator
using Controls =
  tutorial_interfaces::msg::Controls_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__CONTROLS__STRUCT_HPP_
