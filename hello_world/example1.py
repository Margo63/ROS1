#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist
rospy.init_node('splinter')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

msg=Twist()
msg.linear.x=1
msg.angular.z=0
while not rospy.is_shutdown():
    pub.publish(msg)
    msg.angular.z+=0.1
    time.sleep(10)

