#!/usr/bin/env python
import os

class Robot:
    
    #def __init__(self):

    def decir_hola_hora_medicina(self):
        os.system("mpg321 ../voice/medicina_only.mp3")

    def decir_tenga_buen_dia(self):
        os.system("mpg321 ../voice/tenga_buen_dia.mp3")

    def decir_gracias_hasta_luego(self):
        os.system("mpg321 ../voice/gracias_hasta_luego.mp3")

if __name__ == '__main__':
    robot_prueba = Robot()

    robot_prueba.decir_gracias_hasta_luego()