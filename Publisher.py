#! /usr/bin/env python

import rospy
from p_s_Person import Person

if __name__ == "__main":
    rospy.init_node("name")
    pub = rospy.Publisher("topic",Person,seque_size=10)
    rate = rospy.Rate(3)
    p = Person()
    p.name = "xiaowang"
    p.age = 21
    p.height = 1.71
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("%s,%s,%s",p.name,p.age,p.height)
        rate.sleep()