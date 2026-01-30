import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alexroy/Documents/DalMAST/ROS2-Luca/ros2_py_tut/install/py_tut'
