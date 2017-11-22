# RoombaROS_v1
Project 3 Submission. Sean Martin. ECE 4422
This project consists of a ROS package which communicates with
an iRobot Create2 over a serial port USB connection to a Raspberry Pi.

A publisher publishs the 6 IR range sensors (0=no object, 1=object)
and a subscriber takes these values and writes a corresponding left
and right wheel velocity value to the Roomba,

Thanks to the MomsFriendlyRobotCompany for their pycreate2 Python 
library, whose functions are used to drive the Roomba's sensors.
```
https://github.com/MomsFriendlyRobotCompany/pycreate2
```

