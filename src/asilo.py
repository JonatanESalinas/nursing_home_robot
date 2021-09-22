from Persona import Persona

class Asilo:
    def __init__(self):

        #PONER AQUI UNA LISTA DE PERSONAS HABITANTES DEL ASILO?
        self.habitantes_lista = list()
        self.llena_habitantes()

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
        self.xRoom4 = -6.5530	
        self.yRoom4 = 3.5
        self.xDinRoom = 6.125654
        self.yDinRoom = 1.5778
        self.xGarden = 3.125654
        self.yGarden = -1.9778
        self.goalReached = False

        #self.mapa = "map"

    def llena_habitantes(self):
        self.habitantes_lista.append(Persona("Omar Perez", 1, "PK1UENEO00MJXH4R", 1))
        self.habitantes_lista.append(Persona("Ricardo Flores", 2, "?", 2))        #RELLENAR CON LAS API KEYS DE VERDAD!!!!
        self.habitantes_lista.append(Persona("Jacobo Sanchez", 3, "?", 3))