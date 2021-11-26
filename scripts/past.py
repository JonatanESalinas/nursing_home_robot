#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name
'''
    Code to test serial communication with an Arduino Board.
'''
import serial,time


if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyUSB1", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=raw_input("Enter command : ")
                    arduino.write(cmd.encode())
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
