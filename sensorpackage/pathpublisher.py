#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs import PoseStamped
def callback(data):
	mypath = Path()
	mypath.header = data.header

	
	posestamped = PoseStamped()
	posestamped.header = data.header

	posestamped.pose.position = data.pose.postion
	posestamped.pose.orientation = data.pose.orientation 
	mypath.pose.position = posestamped.pose.position
	mypath.pose.orientation = posestamped.pose.orientation
	pub = rospy.Publisher('/append_plot', plot, queue_size=10)
	pub.publish(position)	
def listener():

    rospy.init_node('Pose_node', anonymous=False)

    rospy.Subscriber("/RosAria/pose", Odometry, callback)
    


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
