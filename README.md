# RoombaROS_v1
Project 3 Submission. Sean Martin. ECE 4422

This project consists of a ROS package which communicates with
a iRobot Create2 Roomba over a serial port USB connection from a Raspberry Pi3.

A publisher publishs the 6 IR range sensors (0=no object, 1=object)
and a subscriber takes these values and writes a corresponding left
and right wheel velocity value to the Roomba,

Thanks to the MomsFriendlyRobotCompany for their pycreate2 Python 
library, whose functions are used to drive the Roomba's sensors.
```
https://github.com/MomsFriendlyRobotCompany/pycreate2
```

The following hardware is used: An iRobot Create2

A Raspberry Pi3 w/ Unbuntu 16.04 and ROS Kinetic installed.

To download to a Raspberry Pi follow the below command line
steps


To run the ROS package, three terminal windows are needed.
Run the commands shown for each 3 below.

Terminal 1 [run roscore]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
roscore
```

Terminal 2 [run publisher]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source develop/setup.bash
rosrun ca_driver  rangestate.py
```
