'''
    asilo.py

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
from Persona import Persona

class Asilo:
    def __init__(self):

        #Nursing home habitants list
        self.habitantes_lista = list()

        #Coordinates of the nursing home cardboard model that we used to test the application with the real TurtleBot3
        self.xBase = 1.27
        self.yBase = -0.731
        self.xRoom1 = 4.06
        self.yRoom1 = -0.791
        self.xRoom2 = 3.22
        self.yRoom2 = -0.721
        self.xRoom3 = 2.27
        self.yRoom3 = -0.731

        self.goalReached = False

        self.llena_habitantes()

    #Function that adds elderly people information to a list
    def llena_habitantes(self):
        self.habitantes_lista.append(Persona("Omar Perez", 1, "PK1UENEO00MJXH4R", 1, self.xRoom1, self.yRoom1))
        self.habitantes_lista.append(Persona("Ricardo Flores", 2, "1GRO3H7UWGWXBYHQ", 2, self.xRoom2, self.yRoom2))   
        self.habitantes_lista.append(Persona("Jacobo Sanchez", 3, "XKUO9A2ENYHRFWIL", 3, self.xRoom3, self.yRoom3))