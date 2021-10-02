#!/usr/bin/env python
import os
import threading
import rospy
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point
import datetime
#from ventanasExtra import Ui_ventanaYaEsHora

class Robot:    
    def __init__(self):     
        self.clienteAccionBase = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        rospy.loginfo("Esperando al action server move_base...")
        self.clienteAccionBase.wait_for_server()
        rospy.loginfo("Action server move_base identificado y listo.")

        self.xBase = -6.5530	
        self.yBase = 3.5
        self.my_rate = rospy.Rate(1)

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

    def checa_la_hora(self, mi_recorrido):
        es_la_hora = False

        print("Estoy en un nuevo hilo: " + threading.current_thread().getName())

        while(es_la_hora==False):
            tiempo_ahora = datetime.datetime.now()

            hora = tiempo_ahora.hour
            minuto = tiempo_ahora.minute
            
            if (hora==mi_recorrido.hora_medicina):
                if(minuto==mi_recorrido.minutos_medicina):
                    print(threading.current_thread().getName())
                    print("El robot debe ir a su destino ahora. X: " + str(mi_recorrido.habitacion_X) + " Y: " + str(mi_recorrido.habitacion_Y))

                    #es_la_hora = True       #esto parece que se tiene que borrar despues!!!

                    llegue_bien_a_habitacion = False

                    while(llegue_bien_a_habitacion == False):
                        self.ve_a_habitacion(mi_recorrido.habitacion_X, mi_recorrido.habitacion_Y)
                        
                        self.clienteAccionBase.wait_for_result(rospy.Duration(120))

                        if(self.clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
                            rospy.loginfo("You have reached the destination (room)")
                            llegue_bien_a_habitacion = True
                        else:
                            rospy.loginfo("The robot failed to reach the destination (room), trying again...")

                    self.decir_hola_hora_medicina()

                    rospy.loginfo("Hey Arduino! Ya llegue. [Aqui va el serial con el Arduino]")
                    #Le avisa al Arduino que ya llego. Aqui iria la comunicacion serial con el Arduino

                        #Se hace todo el proceso de autenticacion, entrega de medicina
                    rospy.sleep(5)
                    #Se avisa a la Rasp del turtlebot que ya acabo el proceso
                    rospy.loginfo("Termine. Voy a la base")  

                    self.decir_gracias_hasta_luego()
                    self.decir_tenga_buen_dia()

                    llegue_bien_a_base = False

                    while(llegue_bien_a_base == False):
                        self.ve_a_habitacion(self.xBase, self.yBase)
                        
                        self.clienteAccionBase.wait_for_result(rospy.Duration(120))

                        if(self.clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
                            rospy.loginfo("You have reached the destination (base)")
                            llegue_bien_a_base = True
                        else:
                            rospy.loginfo("The robot failed to reach the destination (base), trying again...")                                      

                        
            self.my_rate.sleep()        #Sleep for 1 sec


if __name__ == '__main__':
    robot_prueba = Robot()

    robot_prueba.decir_gracias_hasta_luego()