'''
    Para correr toda la interfaz:
        python MainPastillero.py
    Para cambiar de .ui a .py:
        pyuic5 Pastillero.ui -o Pastillero.py
    Para generar el archivo Imag_rc.py:
        pyrcc5 Imag.qrc -o Imag_rc.py
'''

import os
import datetime
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#import numpy as np
#import requests
from Pastillero import *
from recorrido import Recorrido
from asilo import Asilo
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

                            #MODIFICAR: PONER LAS COORDENADAS EN LA CLASE PERSONA
        nuevoRecorrido = Recorrido(mi_Asilo.xRoom1, mi_Asilo.yRoom1, hora_elegida, minutos_elegidos)
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

        #Habilitar esta linea para crear como tal el hilo!!!!!!!!!!
        #self.funcion_nuevo_recorrido(nuevoRecorrido, nombre_hilo)

    '''#Descomentar esta funcion para habilitar la funcion de los hilos
    def funcion_nuevo_recorrido(unRecorrido, nombre_recorrido):
        hilo_pendiente_de_la_hora = threading.Thread(target= mi_Robot.checa_la_hora, args=(unRecorrido,), name=nombre_recorrido)
        hilo_pendiente_de_la_hora.start()
    ''' 
    def buscaAHabitante(self, nombre_a_buscar):
        for i in range(0, len(mi_Asilo.habitantes_lista)):
            if mi_Asilo.habitantes_lista[i].Nombre == nombre_a_buscar:
                return mi_Asilo.habitantes_lista[i]

	
    def web(self,u,i,a):
        enviar=requests.get("https://api.thingspeak.com/update?api_key=6Y2UK5ORG1Z4BLWL&field1="+ str(u)+"&field2="+ str(i)+"&field3="+ str(a))

if __name__ == "__main__":

    mi_Asilo = Asilo()

    app = QtWidgets.QApplication([])
    ui = Ui_InterfazViva()
    ui.show()
    app.exec_()