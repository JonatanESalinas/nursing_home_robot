#!/usr/bin/env python
'''
    robot.py

    Carlos Mario Bielma Avendano        A01730645  
    Nashely Martinez Chan               A01329786
    Jonatan Emanuel Salinas Avila       A01731815
    Ximena Aaroni Salinas Molar         A01551723
    Martin Octavio Garcia Garcia        A01328971

    Courses:
        Robotics Project
        Embedded Systems laboratory
    
    November, 2021
'''
import os
import threading
import rospy
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point
import datetime
from std_srvs.srv import Trigger, TriggerRequest, TriggerResponse
from std_msgs.msg import String

class Robot:    
    def __init__(self):     
        self.clienteAccionBase = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        rospy.loginfo("Esperando al action server move_base...")
        self.clienteAccionBase.wait_for_server()
        rospy.loginfo("Action server move_base identificado y listo.")

        self.pub_pastillero = rospy.Publisher('/Pastillero', String, queue_size=1)
        self.myRatePastillero = rospy.Rate(2)

        #creation of the service client connection
        rospy.loginfo("Esperando al habitacion service server...")
        rospy.wait_for_service('/habitacion_service_server')
        rospy.loginfo("Habitacion service server hallado")
        self.conexionCliente_HabsServ = rospy.ServiceProxy('/habitacion_service_server', Trigger)

        #Coordinates of the base of the nursing home cardboard model that we used to test the application
        self.xBase = 1.27                   
        self.yBase = -0.731

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

    def publicaNumero_pastillero(self, num_pastillero):
        bandera = False

        while not bandera:
            connections = self.pub_pastillero.get_num_connections()
            if connections > 0:
                self.pub_pastillero.publish(num_pastillero)
                bandera = True
            else:
                self.myRatePastillero.sleep()

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

                    llegue_bien_a_habitacion = False

                    while(llegue_bien_a_habitacion == False):
                        self.ve_a_habitacion(mi_recorrido.habitacion_X, mi_recorrido.habitacion_Y)
                        
                        self.clienteAccionBase.wait_for_result(rospy.Duration(120))

                        if(self.clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
                            rospy.loginfo("You have reached the destination (room)")
                            
                        else:
                            rospy.loginfo("The robot failed to reach the destination (room), trying again...")
                        llegue_bien_a_habitacion = True
                    rospy.loginfo("Hey Arduino! Ya llegue. [Aqui va el serial con el Arduino]")
                    #Le avisa al Arduino que ya llego. Aqui iria la comunicacion serial con el Arduino

                    #Se crea el ROS msg de tipo String
                    myString_pastillero = String()
                    print("*****se supone que pastillero es: " + str(mi_recorrido.un_pastillero))
                    myString_pastillero.data = str(mi_recorrido.un_pastillero)

                    self.publicaNumero_pastillero(myString_pastillero)

                    #EL cliente llama al Servicio, para que se ejecute la rutina de la habitacion: voz + dispensacion de medicina.
                    resServidorHab = self.conexionCliente_HabsServ(TriggerRequest())
                    if resServidorHab.success== True:
                        rospy.loginfo("El servicio fue dado")
                    else:
                        rospy.loginfo("Problemas al concretar el servicio")

                    #Se avisa a la Rasp del turtlebot que ya acabo el proceso
                    rospy.loginfo("Termine. Voy a la base")  

                    llegue_bien_a_base = False

                    while(llegue_bien_a_base == False):
                        self.ve_a_habitacion(self.xBase, self.yBase)
                        
                        self.clienteAccionBase.wait_for_result(rospy.Duration(120))

                        if(self.clienteAccionBase.get_state() ==  GoalStatus.SUCCEEDED):
                            rospy.loginfo("You have reached the destination (base)")
                        
                        else:
                            rospy.loginfo("The robot failed to reach the destination (base), trying again...")        
                        llegue_bien_a_base = True                              

                        
            self.my_rate.sleep()        #Sleep for 1 sec


if __name__ == '__main__':
    robot_prueba = Robot()

    robot_prueba.decir_gracias_hasta_luego()