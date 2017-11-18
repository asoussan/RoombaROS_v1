#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from pycreate2 import Create2
import time

def callback(data):
    v_top=50
    v_left=v_top
    v_right=v_top

    if any(t > 0 for t in data.data):
        if data.data[0] == 1 or data.data[1]==1 or data.data[2]==1:
            #right turn in place
            #
            v_left=-v_top
            v_right=v_top
        else:
            v_left=v_top
            v_right=-v_top

    bot.drive_direct(v_left,v_right)
    v=[v_left,v_right]
    rospy.loginfo(data.data)
    rospy.loginfo(v)
    time.sleep(0.01)

def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same node are launched, the previous
    # one is kicked off. The anonymous=True flag means that rospy will choose a unique name for our
    # 'listener' node so that multiple listeners can run simultaneously.

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("IRrange", Int32MultiArray, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200
    }

    bot = Create2(port=port, baud=baud['default'])
    listener()
