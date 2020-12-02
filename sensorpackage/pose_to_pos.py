#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry
from sensorpackage.msg import PoseAngle
import math

def callback(data):
	x_quat = data.pose.pose.orientation.x
	y_quat = data.pose.pose.orientation.y
	z_quat = data.pose.pose.orientation.z
	w_quat = data.pose.pose.orientation.w
	x = data.pose.pose.position.x
	y = data.pose.pose.position.y	
	pose_angle = PoseAngle()
	pose_angle.positions.x = x
	pose_angle.positions.y = y
	pose_angle.positions.z = 0
	robot_angle = math.atan2(2*(w_quat*z_quat + x_quat*y_quat), 1-2*(y_quat*y_quat+z_quat*z_quat))
	robot_angle = math.degrees(robot_angle)
	pose_angle.angle = robot_angle
	pub = rospy.Publisher('/Robot_pose', PoseAngle, queue_size=10)
	pub.publish(pose_angle)
def listener():
    rospy.init_node('Pose_to_position', anonymous=False)

    rospy.Subscriber("/RosAria/pose", Odometry, callback)
    
    rospy.spin()
if __name__ == '__main__':
    listener()
