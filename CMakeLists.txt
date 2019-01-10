cmake_minimum_required(VERSION 2.8.3)
project(tello_controller)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  sensor_msgs
  std_msgs
)

catkin_python_setup()


generate_messages(DEPENDENCIES geometry_msgs sensor_msgs std_msgs)

catkin_package(CATKIN_DEPENDS
  geometry_msgs
  message_runtime
  sensor_msgs 
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
