#!/usr/bin/env python3 


import rospy 

from service_node.srv import AddTwoInt,AddTwoIntResponse
def call_me(data):
    
    return AddTwoIntResponse(data.a+data.b)

if __name__=='__main__':
    rospy.init_node('server_node')
    rospy.logerr("warn")
    ser=rospy.Service('add_two_int',AddTwoInt,call_me)

    rospy.spin()