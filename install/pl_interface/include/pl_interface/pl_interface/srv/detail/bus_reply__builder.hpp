// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pl_interface:srv/BusReply.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__SRV__DETAIL__BUS_REPLY__BUILDER_HPP_
#define PL_INTERFACE__SRV__DETAIL__BUS_REPLY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pl_interface/srv/detail/bus_reply__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pl_interface
{

namespace srv
{

namespace builder
{

class Init_BusReply_Request_err
{
public:
  explicit Init_BusReply_Request_err(::pl_interface::srv::BusReply_Request & msg)
  : msg_(msg)
  {}
  ::pl_interface::srv::BusReply_Request err(::pl_interface::srv::BusReply_Request::_err_type arg)
  {
    msg_.err = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Request msg_;
};

class Init_BusReply_Request_data
{
public:
  explicit Init_BusReply_Request_data(::pl_interface::srv::BusReply_Request & msg)
  : msg_(msg)
  {}
  Init_BusReply_Request_err data(::pl_interface::srv::BusReply_Request::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_BusReply_Request_err(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Request msg_;
};

class Init_BusReply_Request_data_len
{
public:
  explicit Init_BusReply_Request_data_len(::pl_interface::srv::BusReply_Request & msg)
  : msg_(msg)
  {}
  Init_BusReply_Request_data data_len(::pl_interface::srv::BusReply_Request::_data_len_type arg)
  {
    msg_.data_len = std::move(arg);
    return Init_BusReply_Request_data(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Request msg_;
};

class Init_BusReply_Request_cmd
{
public:
  Init_BusReply_Request_cmd()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BusReply_Request_data_len cmd(::pl_interface::srv::BusReply_Request::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return Init_BusReply_Request_data_len(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pl_interface::srv::BusReply_Request>()
{
  return pl_interface::srv::builder::Init_BusReply_Request_cmd();
}

}  // namespace pl_interface


namespace pl_interface
{

namespace srv
{

namespace builder
{

class Init_BusReply_Response_err
{
public:
  explicit Init_BusReply_Response_err(::pl_interface::srv::BusReply_Response & msg)
  : msg_(msg)
  {}
  ::pl_interface::srv::BusReply_Response err(::pl_interface::srv::BusReply_Response::_err_type arg)
  {
    msg_.err = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Response msg_;
};

class Init_BusReply_Response_data
{
public:
  explicit Init_BusReply_Response_data(::pl_interface::srv::BusReply_Response & msg)
  : msg_(msg)
  {}
  Init_BusReply_Response_err data(::pl_interface::srv::BusReply_Response::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_BusReply_Response_err(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Response msg_;
};

class Init_BusReply_Response_data_len
{
public:
  explicit Init_BusReply_Response_data_len(::pl_interface::srv::BusReply_Response & msg)
  : msg_(msg)
  {}
  Init_BusReply_Response_data data_len(::pl_interface::srv::BusReply_Response::_data_len_type arg)
  {
    msg_.data_len = std::move(arg);
    return Init_BusReply_Response_data(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Response msg_;
};

class Init_BusReply_Response_cmd
{
public:
  Init_BusReply_Response_cmd()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BusReply_Response_data_len cmd(::pl_interface::srv::BusReply_Response::_cmd_type arg)
  {
    msg_.cmd = std::move(arg);
    return Init_BusReply_Response_data_len(msg_);
  }

private:
  ::pl_interface::srv::BusReply_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pl_interface::srv::BusReply_Response>()
{
  return pl_interface::srv::builder::Init_BusReply_Response_cmd();
}

}  // namespace pl_interface

#endif  // PL_INTERFACE__SRV__DETAIL__BUS_REPLY__BUILDER_HPP_
