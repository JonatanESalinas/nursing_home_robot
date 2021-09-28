from ventanaYaEsHora import *
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class Ui_ventanaYaEsHora(QtWidgets.QDialog,Ui_ventanaYaEsHora):
    def __init__(self, *args, **kwargs):
        QtWidgets.QApplication.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.cierraVentanita)
    
    def cierraVentanita(self):
        self.close()