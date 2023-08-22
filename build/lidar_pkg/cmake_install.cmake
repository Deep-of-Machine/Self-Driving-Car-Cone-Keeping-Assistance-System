# Install script for directory: /home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/lidar_pkg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_pkg/msg" TYPE FILE FILES
    "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/lidar_pkg/msg/lidar_lavacon.msg"
    "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/lidar_pkg/msg/lavacon.msg"
    "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/lidar_pkg/msg/yolo_lavacon.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_pkg/cmake" TYPE FILE FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/lidar_pkg-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/include/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/share/roseus/ros/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/share/common-lisp/ros/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/share/gennodejs/ros/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/local/bin/python3" -m compileall "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/lib/python3/dist-packages/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/devel/lib/python3/dist-packages/lidar_pkg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/lidar_pkg.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_pkg/cmake" TYPE FILE FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/lidar_pkg-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_pkg/cmake" TYPE FILE FILES
    "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/lidar_pkgConfig.cmake"
    "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/lidar_pkgConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_pkg" TYPE FILE FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/src/lidar_pkg/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/lidar_pkg" TYPE PROGRAM FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/pcd_downsampling.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/lidar_pkg" TYPE PROGRAM FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/pcd_clustering.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/lidar_pkg" TYPE PROGRAM FILES "/home/baqu/Self-Driving-Car-Cone-Keeping-Assistance-System/build/lidar_pkg/catkin_generated/installspace/pcd_path_planning.py")
endif()

