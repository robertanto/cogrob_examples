#!/usr/bin/python
import rospy
from std_msgs.msg import Float32MultiArray
from robot_arm_simulator import draw

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' - I heard %s', str(data.data) )
    draw(data.data)

def listener():

    rospy.init_node('robot_simulator')

    rospy.Subscriber('ctrl', Float32MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
