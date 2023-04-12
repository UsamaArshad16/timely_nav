#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from datetime import datetime, time

t1 = t2 = t3 = t4 = t5 = 0

def publish_goal():
    global t1, t2, t3, t4, t5
    rospy.init_node('publish_goal_node', anonymous=True)
    
    # Get ROS parameters
    goal_time_1 = rospy.get_param('goal_time_1')
    goal_time_2 = rospy.get_param('goal_time_2')
    goal_time_3 = rospy.get_param('goal_time_3')
    goal_time_4 = rospy.get_param('goal_time_4')
    goal_time_5 = rospy.get_param('goal_time_5')
    
    pub = rospy.Publisher("/gotogoal", String, queue_size=10)
    
    # Loop until goal time is reached
    while True:
        current_time = datetime.now().strftime('%H:%M')
        if current_time == goal_time_1 and t1 == 0:
            message = "loc,1"
            pub.publish(message)
            t1 = 1
            t2 = t3 = t4 = t5 = 0

        if current_time == goal_time_2 and t2 == 0:
            message = "loc,2"
            pub.publish(message)
            t2 = 1
            t1 = t3 = t4 = t5 = 0

        if current_time == goal_time_3 and t3 == 0:
            message = "loc,3"
            pub.publish(message)
            t3 = 1
            t1 = t2 = t4 = t5 = 0

        if current_time == goal_time_4 and t4 == 0:
            message = "loc,4"
            pub.publish(message)
            t4 = 1
            t1 = t2 = t3 = t5 = 0

        if current_time == goal_time_5 and t5 == 0:
            message = "loc,5"
            pub.publish(message)
            t5 = 1
            t1 = t2 = t3 = t4 = 0

        rospy.sleep(1) # wait 1 second before checking current time again


if __name__ == '__main__':
    try:
        publish_goal()
    except rospy.ROSInterruptException:
        pass
