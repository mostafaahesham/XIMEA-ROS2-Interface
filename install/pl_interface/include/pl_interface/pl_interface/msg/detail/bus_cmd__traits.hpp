// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pl_interface:msg/BusCmd.idl
// generated code does not contain a copyright notice

#ifndef PL_INTERFACE__MSG__DETAIL__BUS_CMD__TRAITS_HPP_
#define PL_INTERFACE__MSG__DETAIL__BUS_CMD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pl_interface/msg/detail/bus_cmd__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pl_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const BusCmd & msg,
  std::ostream & out)
{
  out << "{";
  // member: src
  {
    out << "src: ";
    rosidl_generator_traits::value_to_yaml(msg.src, out);
    out << ", ";
  }

  // member: cmd
  {
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << ", ";
  }

  // member: data_len
  {
    out << "data_len: ";
    rosidl_generator_traits::value_to_yaml(msg.data_len, out);
    out << ", ";
  }

  // member: data
  {
    if (msg.data.size() == 0) {
      out << "data: []";
    } else {
      out << "data: [";
      size_t pending_items = msg.data.size();
      for (auto item : msg.data) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BusCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: src
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "src: ";
    rosidl_generator_traits::value_to_yaml(msg.src, out);
    out << "\n";
  }

  // member: cmd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << "\n";
  }

  // member: data_len
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data_len: ";
    rosidl_generator_traits::value_to_yaml(msg.data_len, out);
    out << "\n";
  }

  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data.size() == 0) {
      out << "data: []\n";
    } else {
      out << "data:\n";
      for (auto item : msg.data) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BusCmd & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace pl_interface

namespace rosidl_generator_traits
{

[[deprecated("use pl_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pl_interface::msg::BusCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  pl_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pl_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const pl_interface::msg::BusCmd & msg)
{
  return pl_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<pl_interface::msg::BusCmd>()
{
  return "pl_interface::msg::BusCmd";
}

template<>
inline const char * name<pl_interface::msg::BusCmd>()
{
  return "pl_interface/msg/BusCmd";
}

template<>
struct has_fixed_size<pl_interface::msg::BusCmd>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pl_interface::msg::BusCmd>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pl_interface::msg::BusCmd>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PL_INTERFACE__MSG__DETAIL__BUS_CMD__TRAITS_HPP_
