#include <SoftwareSerial.h>

SoftwareSerial lora(10, 11);

union {
  int i;
  byte b[2];
} myunion;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //PC하고 아두이노하고의 통신라인!
  lora.begin(9600); //아두이노하고 로라모듈하고의 통신라인!
  pinMode(A3, OUTPUT);
}

void loop() {
  //analogWrite(A1,200);
  // put your main code here, to run repeatedly:
  if (lora.available()) {
    lora.readBytes(myunion.b, 2);
    Serial.println(myunion.i);

    if (myunion.i == 20) {
      analogWrite(A3, 200);
      analogWrite(A2, 0);
      analogWrite(13, 0);
      delay(500);
    }
    if (myunion.i == 20) {
      analogWrite(A3, 200);
      analogWrite(A2, 0);
      analogWrite(A1, 0);
      delay(500);
    }
    if (myunion.i == 30) {
      analogWrite(A3, 0);
      analogWrite(A2, 0);
      analogWrite(13, 200);
      delay(500);
    }
  }

  analogWrite(A3, 0);
  analogWrite(A2, 0);
  analogWrite(A1, 0);
}
