//RST          D9
//SDA(SS)      D10
//MOSI         D11
//MISO         D12
//SCK          D13

#include <SPI.h>
#include <MFRC522.h>

const int buttonPIN = 14;      //Pin 7 para botón de apagado
const int ledPIN = 8;         //Pin 8 para el LED (Servomotor más adelante)
const int RST_PIN = 9;        // Pin 9 para el reset del RC522
const int SS_PIN = 10;        // Pin 10 para el SS (SDA) del RC522


MFRC522 mfrc522(SS_PIN, RST_PIN);   // Crear instancia del MFRC522

byte validKey1[4] = { 0xD2, 0x35, 0x5B, 0x1B };  // Ejemplo de clave valida

//Función para comparar dos vectores
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
}

void loop() {
  // Detectar tarjeta
  if (mfrc522.PICC_IsNewCardPresent())
  {
    //Seleccionamos una tarjeta
    if (mfrc522.PICC_ReadCardSerial())
    {
      // Comparar ID con las claves válidas
      if (isEqualArray(mfrc522.uid.uidByte, validKey1, 4)){
        Serial.println("Tarjeta valida. Pastillero abierto");
        digitalWrite(ledPIN , HIGH); //Enceder LED (Más adelante, función del servomotor)
      }else
        Serial.println("Tarjeta invalida");
      // Finalizar lecturahttps://www.tinkercad.com/things/eXSTGxfu3sF actual
      mfrc522.PICC_HaltA();
    }
  }

  if (digitalRead(buttonPIN) == HIGH){
    digitalWrite(ledPIN, LOW); //Apagar LED (Más adelante, función del servomotor)
    Serial.println("Pastillero Cerrado");
  }
  
  delay(250);

}
