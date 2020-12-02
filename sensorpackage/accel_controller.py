#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from extract_sensor_data import extractData
def talker():
    values = extractData()
    translation = values.x
    rotation = values.rot
    pub = rospy.Publisher('/RosAria/cmd_vel', Twist, queue_size=10)
    rospy.init_node('sensor_node', anonymous=False)
    while not rospy.is_shutdown():
	for i in range(len(translation)):
	   com = Twist()
	   com.linear.x = float(translation[i])*0.3
	   com.linear.y = 0
	   com.linear.z = 0
	   com.angular.x = 0
	   com.angular.y = 0
	   com.angular.z = float(rotation[i])*0.3
	   rospy.sleep(0.1)	
	   pub.publish(com)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


