#!/bin/bash

ros2 launch py_tut py_tut_prod.xml & ros2 launch xsens_mti_ros2_driver xsens_mti_node.launch.py port:=/dev/ttyUSB0
