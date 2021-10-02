class Persona:
	Nombre=''
	Horario=''
	Presion=''
	Oxigenacion=''
	Temperatura=''
	Habitacion=''
	APIKey=''
	Pastillero=''

	def __init__(self,Nombre,Habitacion,APIKey,Pastillero, coord_X, coord_Y):
		self.Nombre=Nombre
		self.Habitacion=Habitacion
		self.APIKey=APIKey
		self.Pastillero=Pastillero

		self.habitacionX = coord_X
		self.habitacionY = coord_Y

	def __str__(self):
		return "Habitacion: " + str(self.Habitacion) + " Nombre: " + self.Nombre + " APIKey: " + str(self.APIKey) +"Pastillero: " + str(self.Pastillero)

	
	@property
	def temperaturaAlta(self,valorTemp):
		if valorTemp>38:
			raise ValorError("La temperatura del paciente es alta")
		self._Temperatura=valorTemp	

	@property
	def presionAlta(self,valorPre):
		if valorPre>129:
			raise ValorError("La presion del paciente es alta")
		self._Presion=valorPre	