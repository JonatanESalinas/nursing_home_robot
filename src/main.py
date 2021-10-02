#!/usr/bin/env python
'''
    Este main no es el principal. Este codigo solo es de prueba para la navegacion y los hilos.
    El main principal es el MainPastillero.py

   Para correr la simulacion:
        Terminal 1:
            roslaunch nursing_home_robot nursing_robot_simulation.launch
        Terminal 2 (correr en el folder nursing_home_robot/src/ )!!!!!!!!!!!!:
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
from recorrido import Recorrido
import threading

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


def funcion_nuevo_recorrido(unRecorrido, nombre_recorrido):
    hilo_pendiente_de_la_hora = threading.Thread(target= mi_Robot.checa_la_hora, args=(unRecorrido,), name=nombre_recorrido)
    hilo_pendiente_de_la_hora.start()

if __name__ == '__main__':

    rospy.loginfo("Iniciando nodo main...")
    rospy.init_node('nodo_main')

    mi_Asilo = Asilo()
    mi_Robot = Robot()

    while 1:

        print("Ajusta recorrido 1:")

        hora_elegida = int(input())
        minutos_elegidos = int(input())
        nombreTemp = raw_input()

        print("Creando nuevo recorrido 1...")

        nuevoRecorrido1 = Recorrido(mi_Asilo.xRoom1, mi_Asilo.yRoom1, hora_elegida, minutos_elegidos)

        funcion_nuevo_recorrido(nuevoRecorrido1, nombreTemp)

        print("aca ando")

