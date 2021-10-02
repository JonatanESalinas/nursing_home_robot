from Persona import Persona

class Asilo:
    def __init__(self):

        #Lista de habitantes de asilo
        self.habitantes_lista = list()

        #Agregar una lista de recorridos?

        # declare the coordinates of interes
        self.xRespawn = -2.9973
        self.yRespawn = 0.9609
        self.xRoom1 = 0.982978
        self.yRoom1 = 3.125654
        self.xRoom2 = 6.125654
        self.yRoom2 = -1.5778
        self.xRoom3 = -6.5520
        self.yRoom3 = -1.9778
        self.xBase = -6.5530	
        self.yBase = 3.5
        self.xDinRoom = 6.125654
        self.yDinRoom = 1.5778
        self.xGarden = 3.125654
        self.yGarden = -1.9778
        self.goalReached = False

        self.llena_habitantes()

    def llena_habitantes(self):
        self.habitantes_lista.append(Persona("Omar Perez", 1, "PK1UENEO00MJXH4R", 1, self.xRoom1, self.yRoom1))
        self.habitantes_lista.append(Persona("Ricardo Flores", 2, "1GRO3H7UWGWXBYHQ", 2, self.xRoom2, self.yRoom2))   
        self.habitantes_lista.append(Persona("Jacobo Sanchez", 3, "XKUO9A2ENYHRFWIL", 3, self.xRoom3, self.yRoom3))