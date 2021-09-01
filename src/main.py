#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from asilo import Asilo



if __name__ == '__main__':

    mi_Asilo = Asilo()

    print("xddxdxdx")
    rospy.loginfo("Iniciando nodo del robot...")
    rospy.init_node('nodo_robot')

    clienteAccionBase = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    rospy.loginfo("Esperando al action server move_base...")
    clienteAccionBase.wait_for_server()
    rospy.loginfo("Action server move_base identificado y listo.")

    goal = MoveBaseGoal()

    #set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/
    goal.target_pose.pose.position =  Point(mi_Asilo.xCafe, mi_Asilo.yCafe, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("")
    clienteAccionBase.send_goal(goal)

    clienteAccionBase.wait_for_result(rospy.Duration(60))

    if(clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
    else:
        rospy.loginfo("The robot failed to reach the destination")

