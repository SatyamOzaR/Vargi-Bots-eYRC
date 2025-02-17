// Generated by gencpp from file pkg_iot_ros_bridge/msgMqttSub.msg
// DO NOT EDIT!


#ifndef PKG_IOT_ROS_BRIDGE_MESSAGE_MSGMQTTSUB_H
#define PKG_IOT_ROS_BRIDGE_MESSAGE_MSGMQTTSUB_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pkg_iot_ros_bridge
{
template <class ContainerAllocator>
struct msgMqttSub_
{
  typedef msgMqttSub_<ContainerAllocator> Type;

  msgMqttSub_()
    : timestamp()
    , topic()
    , message()  {
    }
  msgMqttSub_(const ContainerAllocator& _alloc)
    : timestamp()
    , topic(_alloc)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef ros::Time _timestamp_type;
  _timestamp_type timestamp;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _topic_type;
  _topic_type topic;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> const> ConstPtr;

}; // struct msgMqttSub_

typedef ::pkg_iot_ros_bridge::msgMqttSub_<std::allocator<void> > msgMqttSub;

typedef boost::shared_ptr< ::pkg_iot_ros_bridge::msgMqttSub > msgMqttSubPtr;
typedef boost::shared_ptr< ::pkg_iot_ros_bridge::msgMqttSub const> msgMqttSubConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator1> & lhs, const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator2> & rhs)
{
  return lhs.timestamp == rhs.timestamp &&
    lhs.topic == rhs.topic &&
    lhs.message == rhs.message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator1> & lhs, const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pkg_iot_ros_bridge

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
{
  static const char* value()
  {
    return "76824121accacb087a76246dc01cbb0b";
  }

  static const char* value(const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x76824121accacb08ULL;
  static const uint64_t static_value2 = 0x7a76246dc01cbb0bULL;
};

template<class ContainerAllocator>
struct DataType< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pkg_iot_ros_bridge/msgMqttSub";
  }

  static const char* value(const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
{
  static const char* value()
  {
    return "time timestamp\n"
"string topic\n"
"string message\n"
;
  }

  static const char* value(const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.timestamp);
      stream.next(m.topic);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct msgMqttSub_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pkg_iot_ros_bridge::msgMqttSub_<ContainerAllocator>& v)
  {
    s << indent << "timestamp: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.timestamp);
    s << indent << "topic: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.topic);
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.message);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PKG_IOT_ROS_BRIDGE_MESSAGE_MSGMQTTSUB_H
