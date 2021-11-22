//RST          D9
//SDA(SS)      D10
//MOSI         D11
//MISO         D12
//SCK          D13

#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

const int servo1 = 4;         //Pin 4 Servo 1
const int servo2 = 5;         //Pin 5 Servo 2
const int servo3 = 6;         //Pin 6 Servo 3
const int buttonPIN = 7;      //Pin 7 para botón de apagado
const int ledPIN = 8;         //Pin 8 para el LED (Servomotor más adelante)
const int RST_PIN = 9;        // Pin 9 para el reset del RC522
const int SS_PIN = 10;        // Pin 10 para el SS (SDA) del RC522

Servo myServo1;                       //Crear instancia del primer servo
Servo myServo2;                       //Crear instancia del segundo servo
Servo myServo3;                       //Crear instancia del tercer servo
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Crear instancia del MFRC522

int pastillero;                 //Variable para conocer en que servo(pastillero) estamos
int pos1 = 0;                       //Variables de posición    
int pos2 = 0;
int pos3 = 0;
byte validKey1[4] = { 0xD2, 0x35, 0x5B, 0x1B };   //Clave de salida actual

//Función para comparar dos vectores (Autenticación)
bool isEqualArray(byte* arrayA, byte* arrayB, int length)
{
  for (int index = 0; index < length; index++)
  {
    if (arrayA[index] != arrayB[index]) return false;
  }
  return true;
}

void setup() {
  Serial.begin(9600);         // Iniciar serial
  SPI.begin();                // Iniciar SPI
  mfrc522.PCD_Init();         // Iniciar MFRC522
  pinMode(ledPIN , OUTPUT);   // Definir PIN de salida
  pinMode(buttonPIN,INPUT);   // Definir PIN de entrada
  myServo1.attach(servo1);    //Asignar el servo en el pin 4 al objeto myServo1
  myServo2.attach(servo2);    //Asignar el servo en el pin 5 al objeto myServo2
  myServo3.attach(servo3);    //Asignar el servo en el pin 6 al objeto myServo3
  myServo1.write(pos1);
  myServo2.write(pos2);
  myServo3.write(pos3);
}

void loop() {
  
  Serial.flush();
  if(Serial.available()>0){
    //int pastillero = Serial.readStringUntil('\n').toInt();
    String nombre ="";
    nombre += Serial.readStringUntil('\n');
    if (nombre == "Carlos"){
      pastillero = 1;
    }else if (nombre =="Ximena"){
      pastillero = 2;
    }else if (nombre == "Jona"){
      pastillero = 3;
    }
    //Serial.print("Voy a abrir el pastillero ");
    //Serial.println(pastillero);
      
    // Detectar tarjeta
    while(not mfrc522.PICC_IsNewCardPresent())
    {}
    //Seleccionamos una tarjeta
    if (mfrc522.PICC_ReadCardSerial())
    {
      // Comparar ID con las claves válidas
      if (isEqualArray(mfrc522.uid.uidByte, validKey1, 4)){
        Serial.println("Tarjeta valida.");
        if (pastillero==1){
          pos1 = 80;
          myServo1.write(pos1);
          //Serial.println("Pastillero 1 Abierto");
        }else if (pastillero == 2 ){
          pos2 = 80;
          myServo2.write(pos2);
          //Serial.println("Pastillero 2 Abierto");
        }else if (pastillero == 3){
          pos3 = 80;
          myServo3.write(pos3);
          //Serial.println("Pastillero 3 Abierto");
        }
      }//else
        //Serial.println("Tarjeta inválida");
      // Finalizar lectura actual
      mfrc522.PICC_HaltA();
    }
    //Serial.println("Between");
    while(digitalRead(buttonPIN) == LOW){}
    if (pastillero==1 and pos1 == 80){
      pos1 = 0;
      myServo1.write(pos1);
      //Serial.println("Pastillero 1 Cerrado");
      Serial.write("L");
    }else if (pastillero == 2 and pos2 == 80){
      pos2 = 0;
      myServo2.write(pos2);
      //Serial.println("Pastillero 2 Cerrado");
      Serial.write("L");
    }else if (pastillero == 3 and pos3 == 80){
      pos3 = 0;
      myServo3.write(pos3);
      //Serial.println("Pastillero 3 Cerrado");
      Serial.write("L");
    }else{
      Serial.println('F');
    }
    Serial.flush();
  }
}
