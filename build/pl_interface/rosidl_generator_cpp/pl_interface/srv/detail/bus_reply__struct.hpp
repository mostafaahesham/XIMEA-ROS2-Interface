// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pl_interface:srv/BusReply.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_HPP_
#define PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__pl_interface__srv__BusReply_Request __attribute__((deprecated))
#else
# define DEPRECATED__pl_interface__srv__BusReply_Request __declspec(deprecated)
#endif

namespace pl_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BusReply_Request_
{
  using Type = BusReply_Request_<ContainerAllocator>;

  explicit BusReply_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0;
      this->data_len = 0;
      this->err = 0;
    }
  }

  explicit BusReply_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0;
      this->data_len = 0;
      this->err = 0;
    }
  }

  // field types and members
  using _cmd_type =
    uint8_t;
  _cmd_type cmd;
  using _data_len_type =
    uint8_t;
  _data_len_type data_len;
  using _data_type =
    std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>>;
  _data_type data;
  using _err_type =
    uint8_t;
  _err_type err;

  // setters for named parameter idiom
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
  Type & set__err(
    const uint8_t & _arg)
  {
    this->err = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pl_interface::srv::BusReply_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const pl_interface::srv::BusReply_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pl_interface::srv::BusReply_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pl_interface::srv::BusReply_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pl_interface__srv__BusReply_Request
    std::shared_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pl_interface__srv__BusReply_Request
    std::shared_ptr<pl_interface::srv::BusReply_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BusReply_Request_ & other) const
  {
    if (this->cmd != other.cmd) {
      return false;
    }
    if (this->data_len != other.data_len) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    if (this->err != other.err) {
      return false;
    }
    return true;
  }
  bool operator!=(const BusReply_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BusReply_Request_

// alias to use template instance with default allocator
using BusReply_Request =
  pl_interface::srv::BusReply_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pl_interface


#ifndef _WIN32
# define DEPRECATED__pl_interface__srv__BusReply_Response __attribute__((deprecated))
#else
# define DEPRECATED__pl_interface__srv__BusReply_Response __declspec(deprecated)
#endif

namespace pl_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BusReply_Response_
{
  using Type = BusReply_Response_<ContainerAllocator>;

  explicit BusReply_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0;
      this->data_len = 0;
      this->err = 0;
    }
  }

  explicit BusReply_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd = 0;
      this->data_len = 0;
      this->err = 0;
    }
  }

  // field types and members
  using _cmd_type =
    uint8_t;
  _cmd_type cmd;
  using _data_len_type =
    uint8_t;
  _data_len_type data_len;
  using _data_type =
    std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>>;
  _data_type data;
  using _err_type =
    uint8_t;
  _err_type err;

  // setters for named parameter idiom
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
  Type & set__err(
    const uint8_t & _arg)
  {
    this->err = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pl_interface::srv::BusReply_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const pl_interface::srv::BusReply_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pl_interface::srv::BusReply_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pl_interface::srv::BusReply_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pl_interface__srv__BusReply_Response
    std::shared_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pl_interface__srv__BusReply_Response
    std::shared_ptr<pl_interface::srv::BusReply_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BusReply_Response_ & other) const
  {
    if (this->cmd != other.cmd) {
      return false;
    }
    if (this->data_len != other.data_len) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    if (this->err != other.err) {
      return false;
    }
    return true;
  }
  bool operator!=(const BusReply_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BusReply_Response_

// alias to use template instance with default allocator
using BusReply_Response =
  pl_interface::srv::BusReply_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pl_interface

namespace pl_interface
{

namespace srv
{

struct BusReply
{
  using Request = pl_interface::srv::BusReply_Request;
  using Response = pl_interface::srv::BusReply_Response;
};

}  // namespace srv

}  // namespace pl_interface

#endif  // PL_INTERFACE__SRV__DETAIL__BUS_REPLY__STRUCT_HPP_
