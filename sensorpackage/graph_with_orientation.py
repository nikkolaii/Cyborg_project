#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
from sensorpackage.msg import PoseAngle
import math
def callback(data):
	global counter
	if counter % 5 == 0:
		x = data.positions.x
		y = data.positions.y
		robot_angle = data.angle

		plt.plot(x,y,marker=(3,0,robot_angle),markersize=10,linestyle='None')
		plt.xlabel('x position')
		plt.ylabel('y position')
		plt.title('Robot position')
		plt.pause(0.0001)
	counter += 1

if __name__ == '__main__':
    counter = 0
    rospy.init_node('Graphing_node', anonymous=False)

    rospy.Subscriber("/Robot_pose", PoseAngle, callback)
    plt.show()
    rospy.spin()
