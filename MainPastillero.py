import os
import datetime
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#import numpy as np
#import requests
from Pastillero import *

myAPI = ""#MATLAB
Usuario='A01329786'
Contra='Password'

class Ui_InterfazViva(QtWidgets.QDialog,Ui_InterfazViva):
    def __init__(self, *args, **kwargs):
        QtWidgets.QApplication.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #------------------------------------------------------------------------
        #Disable Tab
        self.Vistas.setTabEnabled(1, False)
        self.Vistas.setTabEnabled(2, False)
        self.Vistas.setTabEnabled(3, False)
        #Click de inicio de sesion
        self.IniciarSesion.clicked.connect(self.PassaworOk )


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

	
    def web(self,u,i,a):
        enviar=requests.get("https://api.thingspeak.com/update?api_key=6Y2UK5ORG1Z4BLWL&field1="+ str(u)+"&field2="+ str(i)+"&field3="+ str(a))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = Ui_InterfazViva()
    ui.show()
    app.exec_()