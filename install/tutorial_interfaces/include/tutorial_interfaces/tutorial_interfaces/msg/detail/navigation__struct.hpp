// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/msg/navigation.hpp"


#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__Navigation __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__Navigation __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Navigation_
{
  using Type = Navigation_<ContainerAllocator>;

  explicit Navigation_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_latitude = 0.0;
      this->waypoint_longitude = 0.0;
      this->tacking_waypoint_latitude = 0.0;
      this->tacking_waypoint_longitude = 0.0;
      this->target_heading = 0.0;
    }
  }

  explicit Navigation_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_latitude = 0.0;
      this->waypoint_longitude = 0.0;
      this->tacking_waypoint_latitude = 0.0;
      this->tacking_waypoint_longitude = 0.0;
      this->target_heading = 0.0;
    }
  }

  // field types and members
  using _waypoint_latitude_type =
    double;
  _waypoint_latitude_type waypoint_latitude;
  using _waypoint_longitude_type =
    double;
  _waypoint_longitude_type waypoint_longitude;
  using _tacking_waypoint_latitude_type =
    double;
  _tacking_waypoint_latitude_type tacking_waypoint_latitude;
  using _tacking_waypoint_longitude_type =
    double;
  _tacking_waypoint_longitude_type tacking_waypoint_longitude;
  using _target_heading_type =
    double;
  _target_heading_type target_heading;

  // setters for named parameter idiom
  Type & set__waypoint_latitude(
    const double & _arg)
  {
    this->waypoint_latitude = _arg;
    return *this;
  }
  Type & set__waypoint_longitude(
    const double & _arg)
  {
    this->waypoint_longitude = _arg;
    return *this;
  }
  Type & set__tacking_waypoint_latitude(
    const double & _arg)
  {
    this->tacking_waypoint_latitude = _arg;
    return *this;
  }
  Type & set__tacking_waypoint_longitude(
    const double & _arg)
  {
    this->tacking_waypoint_longitude = _arg;
    return *this;
  }
  Type & set__target_heading(
    const double & _arg)
  {
    this->target_heading = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::Navigation_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::Navigation_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::Navigation_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::Navigation_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__Navigation
    std::shared_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__Navigation
    std::shared_ptr<tutorial_interfaces::msg::Navigation_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Navigation_ & other) const
  {
    if (this->waypoint_latitude != other.waypoint_latitude) {
      return false;
    }
    if (this->waypoint_longitude != other.waypoint_longitude) {
      return false;
    }
    if (this->tacking_waypoint_latitude != other.tacking_waypoint_latitude) {
      return false;
    }
    if (this->tacking_waypoint_longitude != other.tacking_waypoint_longitude) {
      return false;
    }
    if (this->target_heading != other.target_heading) {
      return false;
    }
    return true;
  }
  bool operator!=(const Navigation_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Navigation_

// alias to use template instance with default allocator
using Navigation =
  tutorial_interfaces::msg::Navigation_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__NAVIGATION__STRUCT_HPP_
