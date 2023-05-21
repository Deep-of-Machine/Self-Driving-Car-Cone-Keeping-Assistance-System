#include <SoftwareSerial.h>

SoftwareSerial lora(2, 3);

int Bsw = 7;
int Rsw = 6;

union {
  int i;
  byte b[2];
} myunion;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600); //PC하고 아두이노하고의 통신라인!
  lora.begin(9600); //아두이노하고 로라모듈하고의 통신라인!

  pinMode(Bsw, INPUT_PULLUP);
  pinMode(Rsw, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.print(digitalRead(Bsw));
  //Serial.println(digitalRead(Rsw));

  if (digitalRead(Rsw) == 0) {
    myunion.i = 20;
    lora.write(myunion.b, 2);
    // delay(500);
  }
  if (digitalRead(Bsw) == 0) {
    myunion.i = 30;
    lora.write(myunion.b, 2);
    // delay(500);
  }
}
