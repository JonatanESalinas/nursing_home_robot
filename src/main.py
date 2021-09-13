#!/usr/bin/env python
'''
   Para correr la simulacion:
        Terminal 1:
            roslaunch nursing_home_robot nursing_home_simulation.launch
        Terminal 2 (correr en el folder nursing_home_robot/src/ ):
            rosrun nursing_home_robot main.py
        Terminal 3:
            roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
            (Acomodar el TurtleBot y cerrar este nodo).
'''

import rospy
import actionlib
from actionlib_msgs.msg import *
from asilo import Asilo
from robot import Robot

def imprimir_menu_temporal():
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

if __name__ == '__main__':

    rospy.loginfo("Iniciando nodo main...")
    rospy.init_node('nodo_main')

    mi_Asilo = Asilo()
    mi_Robot = Robot()

    while 1:

        choice='q'
        imprimir_menu_temporal()
        choice = (input())
        print(choice)

        proximoObjetivo_x = 0
        proximoObjetivo_y = 0

        if (choice==1):
            proximoObjetivo_x = mi_Asilo.xRespawn
            proximoObjetivo_y = mi_Asilo.yRespawn
        elif (choice==2):
            proximoObjetivo_x = mi_Asilo.xRoom1
            proximoObjetivo_y = mi_Asilo.yRoom1
        elif (choice==3):
            proximoObjetivo_x = mi_Asilo.xRoom2
            proximoObjetivo_y = mi_Asilo.yRoom2
        elif (choice==4):
            proximoObjetivo_x = mi_Asilo.xRoom3
            proximoObjetivo_y = mi_Asilo.yRoom3
        elif (choice==5):
            proximoObjetivo_x = mi_Asilo.xRoom4
            proximoObjetivo_y = mi_Asilo.yRoom4
        elif (choice==6):
            proximoObjetivo_x = mi_Asilo.xGarden
            proximoObjetivo_y = mi_Asilo.yGarden
        elif (choice==7):
            proximoObjetivo_x = mi_Asilo.xDinRoom
            proximoObjetivo_y = mi_Asilo.yDinRoom
        elif (choice==8):
            sys.exit()

        mi_Robot.ve_a_habitacion(proximoObjetivo_x, proximoObjetivo_y)

        mi_Robot.clienteAccionBase.wait_for_result(rospy.Duration(60))

        if(mi_Robot.clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
            rospy.loginfo("You have reached the destination")
            mi_Robot.decir_hola_hora_medicina()
        else:
            rospy.loginfo("The robot failed to reach the destination")


