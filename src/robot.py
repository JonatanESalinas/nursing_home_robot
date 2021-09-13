#!/usr/bin/env python
import os
import rospy
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point

class Robot:
    
    def __init__(self):     
        self.clienteAccionBase = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        rospy.loginfo("Esperando al action server move_base...")
        self.clienteAccionBase.wait_for_server()
        rospy.loginfo("Action server move_base identificado y listo.")

    def ve_a_habitacion(self, coordenada_x, coordenada_y):
        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position =  Point(coordenada_x, coordenada_y, 0)

        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

        rospy.loginfo("")
        self.clienteAccionBase.send_goal(goal)

    def decir_hola_hora_medicina(self):
        os.system("mpg321 ../voice/medicina_only.mp3")

    def decir_tenga_buen_dia(self):
        os.system("mpg321 ../voice/tenga_buen_dia.mp3")

    def decir_gracias_hasta_luego(self):
        os.system("mpg321 ../voice/gracias_hasta_luego.mp3")

if __name__ == '__main__':
    robot_prueba = Robot()

    robot_prueba.decir_gracias_hasta_luego()