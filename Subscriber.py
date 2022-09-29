#! /usr/bin/env python

import rospy
from p_s_Person import Person

def doPerson(p):
    rospy.loginfo("%s,%s,%s",p.name,p.age,p.height)

if __name__ == "__main__":
    rospy.init_node("name")
    sub = rospy.Subscriber("",Person,doPerson,seque_size=10)
    rospy.spin()