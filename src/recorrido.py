class Recorrido:
    def __init__(self, una_persona, coordenada_X, coordenada_Y, hora, minutos, pastillero):
        self.persona_a_atender = una_persona
        self.habitacion_X = coordenada_X
        self.habitacion_Y = coordenada_Y
        self.hora_medicina = hora
        self.minutos_medicina = minutos
        self.un_pastillero = pastillero