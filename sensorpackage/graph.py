#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
from geometry_msgs.msg import Point

def callback(data):
	global counter
	if counter % 5 == 0:
		plt.plot(data.x, data.y,'go--')
		print(data.x)
		plt.xlabel('x position')
		plt.ylabel('y position')
		plt.title('Robot position')
		plt.pause(0.0001)
	counter += 1

if __name__ == '__main__':
    counter = 0
    rospy.init_node('Graphing_node', anonymous=False)

    rospy.Subscriber("/Robot_position", Point, callback)
    plt.ion()
    plt.show()
    rospy.spin()
