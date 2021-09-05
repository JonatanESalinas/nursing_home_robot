#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from asilo import Asilo



if __name__ == '__main__':
    while 1:

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
        choice='q'
        #rospy.loginfo(str(n))
        print(' ______________________________________________________')
        print('|                                                      |')
        print('|                Co-Assistant Robot                    |')
        print('|                NURSE TURTLE 2000                     |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        print('|                                                      |')
        print('|  Selecciona la habitacion a la cual va a dispensarse |')
        print('|  el medicamento :                                    |')
        print('|                                                      |')
        print("| 1.- Ir al centro de recarga.                         |")
        print('|                                                      |')
        print("| 2.- Cuarto de Carlos.                                |")
        print('|                                                      |')
        print("| 3.- Cuarto de Jonatan.                               |")
        print('|                                                      |')
        print("| 4.- Cuarto de Ximena.                                |")
        print('|                                                      |')
        print("| 5.- Cuarto de Nashely.                               |")
        print('|                                                      |')
        print("| 6.- Ir al jardin.                                    |")
        print('|                                                      |')
        print("| 7.- Comedor principal.                               |")
        print('|                                                      |')
        print("| 8.- Exit.                                            |")
        print('|                                                      |')
        print('|------------------------------------------------------|')
        choice = (input())
        print(choice)
        if (choice==1):
            goal.target_pose.pose.position =  Point(mi_Asilo.xRespawn, mi_Asilo.yRespawn, 0)
        elif (choice==2):
            goal.target_pose.pose.position =  Point(mi_Asilo.xRoom1, mi_Asilo.yRoom1, 0)
        elif (choice==3):
            goal.target_pose.pose.position =  Point(mi_Asilo.xRoom2, mi_Asilo.yRoom2, 0)
        elif (choice==4):
            goal.target_pose.pose.position =  Point(mi_Asilo.xRoom3, mi_Asilo.yRoom3, 0)
        elif (choice==5):
            goal.target_pose.pose.position =  Point(mi_Asilo.xRoom4, mi_Asilo.yRoom4, 0)
        elif (choice==6):
            goal.target_pose.pose.position =  Point(mi_Asilo.xGarden, mi_Asilo.yGarden, 0)
        elif (choice==7):
            goal.target_pose.pose.position =  Point(mi_Asilo.xDinRoom, mi_Asilo.yDinRoom, 0)
        elif (choice==8):
            sys.exit()
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

