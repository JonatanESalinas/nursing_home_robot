from Persona import Persona

class Asilo:
    def __init__(self):

        #Lista de habitantes de asilo
        self.habitantes_lista = list()

        #Coordenadas de la casa de Gazebo - (Descomentar si se estan haciendo pruebas con simulacion)
        '''
        self.xBase = -6.5530	
        self.yBase = 3.5
        self.xRoom1 = 0.982978
        self.yRoom1 = 3.125654
        self.xRoom2 = 6.125654
        self.yRoom2 = -1.5778
        self.xRoom3 = -6.5520
        self.yRoom3 = -1.9778
        '''
        #Coordenadas del laboratorio - (Descomentar si se estan haciendo pruebas fisicas en el labo)
        
        self.xBase = 1.9	
        self.yBase = -3.54
        self.xRoom1 = 0.828
        self.yRoom1 = 4.83
        self.xRoom2 = -1.81
        self.yRoom2 = 2.03
        self.xRoom3 = 0.0192
        self.yRoom3 = -0.212
        #self.xRoom4 = -1.41       #por si no sirve alguna coordenada de arriba, intentar con esta otra coordenada
        #self.yRoom4 = -3.35  
        

        self.goalReached = False

        self.llena_habitantes()

    def llena_habitantes(self):
        self.habitantes_lista.append(Persona("Omar Perez", 1, "PK1UENEO00MJXH4R", 1, self.xRoom1, self.yRoom1))
        self.habitantes_lista.append(Persona("Ricardo Flores", 2, "1GRO3H7UWGWXBYHQ", 2, self.xRoom2, self.yRoom2))   
        self.habitantes_lista.append(Persona("Jacobo Sanchez", 3, "XKUO9A2ENYHRFWIL", 3, self.xRoom3, self.yRoom3))