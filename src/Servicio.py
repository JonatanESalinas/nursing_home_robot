#!/usr/bin/env python
import os
import rospy
import serial,time
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import String

class HabitacionServer(object):
    def __init__(self):
        self.my_serviceHabitacion = rospy.Service('/habitacion_service_server', Trigger, self.habitacionServerFun)
        self.myResponse = TriggerResponse()
        rospy.loginfo("Service server de habitacion listo.")

        self.sub_pastillero = rospy.Subscriber('/Pastillero', String, self.actualiza_Habitacion)
        self.miHabitacion= String()

    def actualiza_Habitacion(self, msg):
        self.miHabitacion = msg

    def decir_hola_hora_medicina(self):
        os.system("mpg321 ../voice/medicina_only.mp3")

    def decir_tenga_buen_dia(self):
        os.system("mpg321 ../voice/tenga_buen_dia.mp3")

    def decir_gracias_hasta_luego(self):
        os.system("mpg321 ../voice/gracias_hasta_luego.mp3")

    def habitacionServerFun(self, request):
        self.decir_hola_hora_medicina()

        #Se hace todo el proceso de autenticacion, entrega de medicina
        rospy.loginfo("Aca va lo del serial...")
        print("****Se supone que voy a mandar al arduino esto : " + self.miHabitacion.data)
        rospy.sleep(5)
        '''
        print('Running. Press CTRL-C to exit.')
        with serial.Serial("/dev/ttyUSB1", 9600, timeout=1) as arduino:
            time.sleep(0.1) #wait for serial to open
            if arduino.isOpen():
                print("{} connected!".format(arduino.port))
                try:
                    while True:
                        arduino.write(self.miHabitacion.data)
                        while arduino.inWaiting()==0: pass
                        if arduino.inWaiting()>0:
                            #print "hola"
                            while True:
                                answer=arduino.readline()
                                print "recibi respuesta"
                                if answer =='L':
                                    print "recibi la L"
                                    break
                            print answer

                                    #if  arduino.inWaiting()>0:
                                        #while(arduino.readline()!='L'):
                                            #answer =  "N"
                                            #print answer
                                            #break

                            arduino.flushInput() #remove data after reading
                except KeyboardInterrupt:
                    print("KeyboardInterrupt has been caught.")
        '''

        self.decir_gracias_hasta_luego()
        self.decir_tenga_buen_dia()

        self.myResponse.success = True
        self.myResponse.message = "Success"

        rospy.loginfo("Termine bien el servicio!")
        
        return self.myResponse

#The node for the service and an instance of the class are
#created.
if __name__=="__main__":
    rospy.init_node('habitacion_server_node', log_level=rospy.DEBUG)
    rospy.loginfo("Iniciando Habitacion Service Server...")
    HabitacionServer()
    rospy.spin()
