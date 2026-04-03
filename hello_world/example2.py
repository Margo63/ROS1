#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
def callback(msg):
    rospy.loginfo(msg)

rospy.init_node('commend_listner')
rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
rospy.spin()
