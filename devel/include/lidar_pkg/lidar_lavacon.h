// Generated by gencpp from file lidar_pkg/lidar_lavacon.msg
// DO NOT EDIT!


#ifndef LIDAR_PKG_MESSAGE_LIDAR_LAVACON_H
#define LIDAR_PKG_MESSAGE_LIDAR_LAVACON_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace lidar_pkg
{
template <class ContainerAllocator>
struct lidar_lavacon_
{
  typedef lidar_lavacon_<ContainerAllocator> Type;

  lidar_lavacon_()
    : lidar_mid_X(0.0)
    , lidar_mid_y(0.0)
    , lidar_mid_z(0.0)
    , lidar_con_name()
    , lidar_con_color()  {
    }
  lidar_lavacon_(const ContainerAllocator& _alloc)
    : lidar_mid_X(0.0)
    , lidar_mid_y(0.0)
    , lidar_mid_z(0.0)
    , lidar_con_name(_alloc)
    , lidar_con_color(_alloc)  {
  (void)_alloc;
    }



   typedef double _lidar_mid_X_type;
  _lidar_mid_X_type lidar_mid_X;

   typedef double _lidar_mid_y_type;
  _lidar_mid_y_type lidar_mid_y;

   typedef double _lidar_mid_z_type;
  _lidar_mid_z_type lidar_mid_z;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _lidar_con_name_type;
  _lidar_con_name_type lidar_con_name;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _lidar_con_color_type;
  _lidar_con_color_type lidar_con_color;





  typedef boost::shared_ptr< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> const> ConstPtr;

}; // struct lidar_lavacon_

typedef ::lidar_pkg::lidar_lavacon_<std::allocator<void> > lidar_lavacon;

typedef boost::shared_ptr< ::lidar_pkg::lidar_lavacon > lidar_lavaconPtr;
typedef boost::shared_ptr< ::lidar_pkg::lidar_lavacon const> lidar_lavaconConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lidar_pkg::lidar_lavacon_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::lidar_pkg::lidar_lavacon_<ContainerAllocator1> & lhs, const ::lidar_pkg::lidar_lavacon_<ContainerAllocator2> & rhs)
{
  return lhs.lidar_mid_X == rhs.lidar_mid_X &&
    lhs.lidar_mid_y == rhs.lidar_mid_y &&
    lhs.lidar_mid_z == rhs.lidar_mid_z &&
    lhs.lidar_con_name == rhs.lidar_con_name &&
    lhs.lidar_con_color == rhs.lidar_con_color;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::lidar_pkg::lidar_lavacon_<ContainerAllocator1> & lhs, const ::lidar_pkg::lidar_lavacon_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace lidar_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8869dac3714f40275d5d1c09afbfd6f5";
  }

  static const char* value(const ::lidar_pkg::lidar_lavacon_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8869dac3714f4027ULL;
  static const uint64_t static_value2 = 0x5d5d1c09afbfd6f5ULL;
};

template<class ContainerAllocator>
struct DataType< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lidar_pkg/lidar_lavacon";
  }

  static const char* value(const ::lidar_pkg::lidar_lavacon_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 lidar_mid_X\n"
"float64 lidar_mid_y\n"
"float64 lidar_mid_z\n"
"string lidar_con_name\n"
"string lidar_con_color\n"
;
  }

  static const char* value(const ::lidar_pkg::lidar_lavacon_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.lidar_mid_X);
      stream.next(m.lidar_mid_y);
      stream.next(m.lidar_mid_z);
      stream.next(m.lidar_con_name);
      stream.next(m.lidar_con_color);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct lidar_lavacon_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lidar_pkg::lidar_lavacon_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lidar_pkg::lidar_lavacon_<ContainerAllocator>& v)
  {
    s << indent << "lidar_mid_X: ";
    Printer<double>::stream(s, indent + "  ", v.lidar_mid_X);
    s << indent << "lidar_mid_y: ";
    Printer<double>::stream(s, indent + "  ", v.lidar_mid_y);
    s << indent << "lidar_mid_z: ";
    Printer<double>::stream(s, indent + "  ", v.lidar_mid_z);
    s << indent << "lidar_con_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.lidar_con_name);
    s << indent << "lidar_con_color: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.lidar_con_color);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LIDAR_PKG_MESSAGE_LIDAR_LAVACON_H