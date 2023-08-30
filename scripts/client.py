#!/usr/bin/env python3 


import rospy 
import sys 

from service_node.srv import * 

def ser_call(a,b):
    try:
        ser=rospy.ServiceProxy('add_two_int',AddTwoInt)
        ans=ser(int(a),int(b))
        return ans.sum

    except rospy.ServiceException as e:
        rospy.loginfo(e)
if __name__=='__main__':
    rospy.init_node('client_node')
    rospy.wait_for_service('add_two_int')
    
    rospy.loginfo(ser_call(sys.argv[1],sys.argv[2]))