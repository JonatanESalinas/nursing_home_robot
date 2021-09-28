#!/usr/bin/env python
'''
   Para correr la simulacion:
        Terminal 1:
            roslaunch nursing_home_robot nursing_robot_simulation.launch
        Terminal 2:
            roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

            (Acomodar el TurtleBot y cerrar este nodo)., luego Ctrl-C y ejecutar:
        Terminal 2 (CORRER EN EL FOLDER nursing_home_robot/src/ )!!!!!!!!!!!!:
            rosrun nursing_home_robot MainPastillero.py

    Para cambiar de .ui a .py:
        pyuic5 Pastillero.ui -o Pastillero.py
    Para generar el archivo Imag_rc.py:
        pyrcc5 Imag.qrc -o Imag_rc.py
'''

#import os
#import datetime
#import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#import numpy as np
#import requests
from Pastillero import *

import rospy
#import actionlib
from actionlib_msgs.msg import *
from asilo import Asilo
from robot import Robot
from recorrido import Recorrido
import threading

myAPI = ""#MATLAB
Usuario='A01329786'
Contra='Password'

class Ui_InterfazViva(QtWidgets.QDialog,Ui_InterfazViva):
    def __init__(self, *args, **kwargs):
        QtWidgets.QApplication.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #------------------------------------------------------------------------
        #Disable Tab
        self.Vistas.setTabEnabled(1, True)     ##VOLVER A PONER EN FALSE!!!
        self.Vistas.setTabEnabled(2, True)
        self.Vistas.setTabEnabled(3, True)
        #Click de inicio de sesion
        self.IniciarSesion.clicked.connect(self.PassaworOk)
        self.GuardarHoras.clicked.connect(self.agregaNuevoRecorrido)

    def PassaworOk(self):
        UsuarioQT = self.EntradaUsuario.toPlainText()
        ContraQT = self.EntradaContra.toPlainText()

        if UsuarioQT==Usuario and Contra==ContraQT:
            result=True
        else:
            result =False

        if result == False:
            self.Vistas.setTabEnabled(1, False)
            self.Vistas.setTabEnabled(2, False)
            self.Vistas.setTabEnabled(3, False)
        else:
            self.Vistas.setTabEnabled(1, True)
            self.Vistas.setTabEnabled(2, True)
            self.Vistas.setTabEnabled(3, True)

    def agregaNuevoRecorrido(self):

        nombreSeleccionado = self.NombresPacientes.currentText()
        hora_elegida = self.HorasComoBox.currentText()
        minutos_elegidos = self.MinutosComoBox.currentText()
        hora_en_formato = hora_elegida + ":" + minutos_elegidos
        
        nombre_hilo = nombreSeleccionado + ":hora=" + hora_elegida + " minutos=" + minutos_elegidos

        hora_elegida = int(hora_elegida)
        minutos_elegidos = int(minutos_elegidos)

        personaDelRecorrido = self.buscaAHabitante(nombreSeleccionado)
        
        nuevoRecorrido = Recorrido(personaDelRecorrido.Nombre, personaDelRecorrido.habitacionX, personaDelRecorrido.habitacionY, hora_elegida, minutos_elegidos)
        #mi_Asilo.myArrayRecorridos.append(nuevoRecorrido)          #LO GUARDO EN UN ARREGLO DE RECORRIDOS???
            
        renglonPos = self.tablaRecorridos.rowCount()
        self.tablaRecorridos.insertRow(renglonPos)
        self.tablaRecorridos.setItem(renglonPos , 0, QtWidgets.QTableWidgetItem(nombreSeleccionado))
        self.tablaRecorridos.setItem(renglonPos , 1, QtWidgets.QTableWidgetItem(hora_en_formato))
        self.tablaRecorridos.setItem(renglonPos , 2, QtWidgets.QTableWidgetItem(str(personaDelRecorrido.Habitacion)))
        self.tablaRecorridos.setItem(renglonPos , 3, QtWidgets.QTableWidgetItem(str(personaDelRecorrido.Pastillero)))        

        print("Ando en agregaNuevoRecorrido: " + nombreSeleccionado)
        print("Hora: " + str(hora_elegida))
        print("Minutos: " + str(minutos_elegidos))

        self.funcion_nuevo_recorrido(nuevoRecorrido, nombre_hilo)

    def funcion_nuevo_recorrido(self, unRecorrido, nombre_recorrido):
        hilo_pendiente_de_la_hora = threading.Thread(target= mi_Robot.checa_la_hora, args=(unRecorrido,), name=nombre_recorrido)
        hilo_pendiente_de_la_hora.start()
     
    def buscaAHabitante(self, nombre_a_buscar):
        for i in range(0, len(mi_Asilo.habitantes_lista)):
            if mi_Asilo.habitantes_lista[i].Nombre == nombre_a_buscar:
                return mi_Asilo.habitantes_lista[i]

	
    def web(self,u,i,a):
        enviar=requests.get("https://api.thingspeak.com/update?api_key=6Y2UK5ORG1Z4BLWL&field1="+ str(u)+"&field2="+ str(i)+"&field3="+ str(a))

if __name__ == "__main__":

    rospy.loginfo("Iniciando nodo MainPastillero con GUI...")
    rospy.init_node('nodo_main')

    mi_Asilo = Asilo()
    mi_Robot = Robot()

    app = QtWidgets.QApplication([])
    ui = Ui_InterfazViva()
    ui.show()
    app.exec_()