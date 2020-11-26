cmake_minimum_required(VERSION 3.0.2)
project(pkg_ros_basics)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  message_generation
)

add_message_files(
  FILES
  myMessage.msg
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES control_turtle
 CATKIN_DEPENDS geometry_msgs rospy message_runtime

)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)