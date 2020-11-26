#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Pose

path = Path()

def odom_cb(data):
    global path
    path.header = data.header
    ps = PoseStamped()
    ps.header = data.header
    ps.pose = data.pose.pose
    path.poses.append(ps)
    path_pub.publish(path)

rospy.init_node('path_node')
odomometry_sub = rospy.Subscriber('/RosAria/pose', Odometry, odom_cb)
path_pub = rospy.Publisher('/path', Path, queue_size=10)

if __name__ == '__main__':
    rospy.spin()
