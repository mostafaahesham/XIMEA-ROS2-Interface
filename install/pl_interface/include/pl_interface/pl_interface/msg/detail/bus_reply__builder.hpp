// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pl_interface:msg/BusReply.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_REPLY__BUILDER_HPP_
#define PL_INTERFACE__MSG__DETAIL__BUS_REPLY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pl_interface/msg/detail/bus_reply__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pl_interface
{

namespace msg
{

namespace builder
{

class Init_BusReply_data
{
public:
  explicit Init_BusReply_data(::pl_interface::msg::BusReply & msg)
  : msg_(msg)
  {}
  ::pl_interface::msg::BusReply data(::pl_interface::msg::BusReply::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pl_interface::msg::BusReply msg_;
};

class Init_BusReply_data_len
{
public:
  explicit Init_BusReply_data_len(::pl_interface::msg::BusReply & msg)
  : msg_(msg)
  {}
  Init_BusReply_data data_len(::pl_interface::msg::BusReply::_data_len_type arg)
  {
    msg_.data_len = std::move(arg);
    return Init_BusReply_data(msg_);
  }

private:
  ::pl_interface::msg::BusReply msg_;
};

class Init_BusReply_cmd
{
public:
  explicit Init_BusReply_cmd(::pl_interface::msg::BusReply & msg)
  : msg_(msg)
  {}
  Init_BusReply_data_len cmd(::pl_interface::msg::BusReply::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return Init_BusReply_data_len(msg_);
  }

private:
  ::pl_interface::msg::BusReply msg_;
};

class Init_BusReply_dest
{
public:
  Init_BusReply_dest()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BusReply_cmd dest(::pl_interface::msg::BusReply::_dest_type arg)
  {
    msg_.dest = std::move(arg);
    return Init_BusReply_cmd(msg_);
  }

private:
  ::pl_interface::msg::BusReply msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pl_interface::msg::BusReply>()
{
  return pl_interface::msg::builder::Init_BusReply_dest();
}

}  // namespace pl_interface

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_REPLY__BUILDER_HPP_
