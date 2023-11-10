// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pl_interface:msg/BusCmd.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_HPP_
#define PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__pl_interface__msg__BusCmd __attribute__((deprecated))
#else
# define DEPRECATED__pl_interface__msg__BusCmd __declspec(deprecated)
#endif

namespace pl_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BusCmd_
{
  using Type = BusCmd_<ContainerAllocator>;

  explicit BusCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->src = 0;
      this->cmd = 0;
      this->data_len = 0;
    }
  }

  explicit BusCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->src = 0;
      this->cmd = 0;
      this->data_len = 0;
    }
  }

  // field types and members
  using _src_type =
    uint8_t;
  _src_type src;
  using _cmd_type =
    uint8_t;
  _cmd_type cmd;
  using _data_len_type =
    uint8_t;
  _data_len_type data_len;
  using _data_type =
    std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__src(
    const uint8_t & _arg)
  {
    this->src = _arg;
    return *this;
  }
  Type & set__cmd(
    const uint8_t & _arg)
  {
    this->cmd = _arg;
    return *this;
  }
  Type & set__data_len(
    const uint8_t & _arg)
  {
    this->data_len = _arg;
    return *this;
  }
  Type & set__data(
    const std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pl_interface::msg::BusCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const pl_interface::msg::BusCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pl_interface::msg::BusCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pl_interface::msg::BusCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pl_interface::msg::BusCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pl_interface::msg::BusCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pl_interface::msg::BusCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pl_interface::msg::BusCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pl_interface::msg::BusCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pl_interface::msg::BusCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pl_interface__msg__BusCmd
    std::shared_ptr<pl_interface::msg::BusCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pl_interface__msg__BusCmd
    std::shared_ptr<pl_interface::msg::BusCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BusCmd_ & other) const
  {
    if (this->src != other.src) {
      return false;
    }
    if (this->cmd != other.cmd) {
      return false;
    }
    if (this->data_len != other.data_len) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const BusCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BusCmd_

// alias to use template instance with default allocator
using BusCmd =
  pl_interface::msg::BusCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pl_interface

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_CMD__STRUCT_HPP_
