#!/usr/bin/env python
'''
    This is the main code. Running this code will execute the PillBot Graphical User Interface, with all its functionalities,
    as schedule the robot to deliver medicine at a specific hour, or register vital signs data.
    This code creates a new ROS node "nodo_main" too.

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

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import requests
from Pastillero import *

import rospy
from actionlib_msgs.msg import *
from asilo import Asilo
from robot import Robot
from recorrido import Recorrido
import threading

Usuario='Usuario'
Contra='Password'
anterior=1

class Ui_InterfazViva(QtWidgets.QDialog,Ui_InterfazViva):
    def __init__(self, *args, **kwargs):
        QtWidgets.QApplication.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #------------------------------------------------------------------------
        self.datos= []
        #Disable Tab
        self.Vistas.setTabEnabled(1, False)   
        self.Vistas.setTabEnabled(2, False)
        self.Vistas.setTabEnabled(3, False)
        #Click de inicio de sesion
        self.IniciarSesion.clicked.connect(self.PassaworOk)
        self.GuardarHoras.clicked.connect(self.agregaNuevoRecorrido)
        self.GuardarSignosVitales.clicked.connect(self.seleccionPaciente)

    #Function to verify the credentials
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

    def seleccionPaciente(self):
        nombrePaciente = self.NombresPacientes_2.currentText()
        temperatura = self.EntradaTemperatura.toPlainText()
        presion = self.PresionEntrada.toPlainText()
        oxigeno = self.Oxigenacion.toPlainText()

        print(nombrePaciente)
        print(temperatura)
        print(presion)
        print(oxigeno)

        if str(nombrePaciente)=='Omar Perez':
            #Substitute here your ThingSpeak API Key
            self.web("PK1UENEO00MJXH4R", int(temperatura), int(oxigeno), int(presion))
            self.inicio(str(nombrePaciente),str(temperatura),str(presion),str(oxigeno),1)
            self.agregar()
        elif str(nombrePaciente)=='Ricardo Flores':
            #Substitute here your ThingSpeak API Key
            self.web("1GRO3H7UWGWXBYHQ", int(temperatura), int(oxigeno), int(presion))
            self.inicio(str(nombrePaciente),str(temperatura),str(presion),str(oxigeno),2)
            self.agregar()
        else:
            #Substitute here your ThingSpeak API Key
            self.web("XKUO9A2ENYHRFWIL", int(temperatura), int(oxigeno), int(presion))
            self.inicio(str(nombrePaciente),str(temperatura),str(presion),str(oxigeno),3)
            self.agregar()

    def inicio(self,nom,temp,pre,oxi,control):
        global anterior
        
        if control==anterior:
            self.datos.append((nom,temp,pre,oxi))
        else:
            anterior=control
            self.datos=[]

            self.datos.append((nom,temp,pre,oxi))

    def agregar(self):
        fila =0
        for registro in self.datos:
            columna=0
            self.tablaSignosVitales.insertRow(fila)
            for elemento in registro:   
                celda= QTableWidgetItem(elemento)
                self.tablaSignosVitales.setItem(fila,columna,celda)
                columna+=1
            fila+=1       

    # This function creates a new object of the class "Recorrido", with the information of the route
    # that the robot will make.
    def agregaNuevoRecorrido(self):
        nombreSeleccionado = self.NombresPacientes.currentText()
        hora_elegida = self.HorasComoBox.currentText()
        minutos_elegidos = self.MinutosComoBox.currentText()
        hora_en_formato = hora_elegida + ":" + minutos_elegidos
        
        nombre_hilo = nombreSeleccionado + ":hora=" + hora_elegida + " minutos=" + minutos_elegidos

        hora_elegida = int(hora_elegida)
        minutos_elegidos = int(minutos_elegidos)

        personaDelRecorrido = self.buscaAHabitante(nombreSeleccionado)
        
        nuevoRecorrido = Recorrido(personaDelRecorrido.Nombre, personaDelRecorrido.habitacionX, personaDelRecorrido.habitacionY, hora_elegida, minutos_elegidos, personaDelRecorrido.Pastillero)
        
        #The new itinerary is put into a table in the GUI
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

    #This function creates and starts a new thread, that corresponds to a new programmed itinerary for the robot.
    def funcion_nuevo_recorrido(self, unRecorrido, nombre_recorrido):
        hilo_pendiente_de_la_hora = threading.Thread(target= mi_Robot.checa_la_hora, args=(unRecorrido,), name=nombre_recorrido)
        hilo_pendiente_de_la_hora.start()
    
    #Function that search for a specific elderly person in a list
    def buscaAHabitante(self, nombre_a_buscar):
        for i in range(0, len(mi_Asilo.habitantes_lista)):
            if mi_Asilo.habitantes_lista[i].Nombre == nombre_a_buscar:
                return mi_Asilo.habitantes_lista[i]

    #Function that upload vital signs data to a personalized ThingSpeak dashboard, according to the elderly person.
    def web(self,key_persona, valor_temp,valor_oxigenacion,valor_presion):
        enviar=requests.get("https://api.thingspeak.com/update?api_key=" + key_persona + "&field1="+ str(valor_temp)+"&field2="+ str(valor_oxigenacion)+"&field3="+ str(valor_presion))

if __name__ == "__main__":

    rospy.loginfo("Iniciando nodo MainPastillero con GUI...")
    rospy.init_node('nodo_main')

    mi_Asilo = Asilo()
    mi_Robot = Robot()

    app = QtWidgets.QApplication([])
    ui = Ui_InterfazViva()
    ui.show()
    app.exec_()