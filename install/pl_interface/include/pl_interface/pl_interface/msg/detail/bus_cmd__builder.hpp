// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pl_interface:msg/BusCmd.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_CMD__BUILDER_HPP_
#define PL_INTERFACE__MSG__DETAIL__BUS_CMD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pl_interface/msg/detail/bus_cmd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pl_interface
{

namespace msg
{

namespace builder
{

class Init_BusCmd_data
{
public:
  explicit Init_BusCmd_data(::pl_interface::msg::BusCmd & msg)
  : msg_(msg)
  {}
  ::pl_interface::msg::BusCmd data(::pl_interface::msg::BusCmd::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pl_interface::msg::BusCmd msg_;
};

class Init_BusCmd_data_len
{
public:
  explicit Init_BusCmd_data_len(::pl_interface::msg::BusCmd & msg)
  : msg_(msg)
  {}
  Init_BusCmd_data data_len(::pl_interface::msg::BusCmd::_data_len_type arg)
  {
    msg_.data_len = std::move(arg);
    return Init_BusCmd_data(msg_);
  }

private:
  ::pl_interface::msg::BusCmd msg_;
};

class Init_BusCmd_cmd
{
public:
  explicit Init_BusCmd_cmd(::pl_interface::msg::BusCmd & msg)
  : msg_(msg)
  {}
  Init_BusCmd_data_len cmd(::pl_interface::msg::BusCmd::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return Init_BusCmd_data_len(msg_);
  }

private:
  ::pl_interface::msg::BusCmd msg_;
};

class Init_BusCmd_src
{
public:
  Init_BusCmd_src()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BusCmd_cmd src(::pl_interface::msg::BusCmd::_src_type arg)
  {
    msg_.src = std::move(arg);
    return Init_BusCmd_cmd(msg_);
  }

private:
  ::pl_interface::msg::BusCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pl_interface::msg::BusCmd>()
{
  return pl_interface::msg::builder::Init_BusCmd_src();
}

}  // namespace pl_interface

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_CMD__BUILDER_HPP_
