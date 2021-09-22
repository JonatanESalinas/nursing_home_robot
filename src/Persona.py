class Persona:
	Nombre=''
	Horario=''
	Presion=''
	Oxigenacion=''
	Temperatura=''
	Habitacion=''
	APIKey=''
	Pastillero=''

	def __init__(self,Nombre,Habitacion,APIKey,Pastillero):
		self.Nombre=Nombre
		self.Habitacion=Habitacion
		self.APIKey=APIKey
		self.Pastillero=Pastillero

	def __str__(self):
		return "Habitacion: " + str(self.Habitacion) + " Nombre: " + self.Nombre + " APIKey: " + str(self.APIKey) +"Pastillero: " + str(self.Pastillero)


	'''	def inicializar(self,Presion,Oxigenacion,Temperatura):
		self.Nombre=Nombre
		self.Presion=Presion
		self.Oxigenacion= Oxigenacion
		self.Horario=Horario
		self.Temperatura= Temperatura
		self.Habitacion=Habitacion
		self.Habitacion=Habitacion'''
	
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