#include <SoftwareSerial.h>

SoftwareSerial lora(2, 3);

byte send_buff[4];
byte recv_buff[4];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //PC하고 아두이노하고의 통신라인!
  lora.begin(9600); //아두이노하고 로라모듈하고의 통신라인!
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    char c = Serial.read();

    if (c == '0') {
      //ADDH부터 request해보자!
      send_buff[0] = 0xC1;
      send_buff[1] = 0x00;
      send_buff[2] = 0x01;

      lora.write(send_buff, 3); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[0] == send_buff[0] && recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.print("ADDH=");
        Serial.println(recv_buff[3], HEX);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '1') {
      send_buff[0] = 0xC1;
      send_buff[1] = 0x01;
      send_buff[2] = 0x01;
      
      lora.write(send_buff, 3); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[0] == send_buff[0] && recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.print("ADDL=");
        Serial.println(recv_buff[3], HEX);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '2') {
      send_buff[0] = 0xC1;
      send_buff[1] = 0x04;
      send_buff[2] = 0x01;
      
      lora.write(send_buff, 3); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[0] == send_buff[0] && recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.print("CH=");
        Serial.print(850.125 + recv_buff[3]);
        Serial.println("Mhz");
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '3') {
      send_buff[0] = 0xC1;
      send_buff[1] = 0x05;
      send_buff[2] = 0x01;
      
      lora.write(send_buff, 3); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[0] == send_buff[0] && recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], BIN);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '4') {
      //주파수를 설정하는 모드!
      send_buff[0] = 0xC0;
      send_buff[1] = 0x04;
      send_buff[2] = 0x01;
      send_buff[3] = 0x47; //내가 원하는 주파수를 여기다가 넣기!
      
      lora.write(send_buff, 4); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], HEX);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '5') {
      //T모드로 설정하기!
      send_buff[0] = 0xC0;
      send_buff[1] = 0x05;
      send_buff[2] = 0x01;
      send_buff[3] = 0b00000011;
      
      lora.write(send_buff, 4); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], BIN);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '6') {
      //F모드로 설정하기!
      send_buff[0] = 0xC0;
      send_buff[1] = 0x05;
      send_buff[2] = 0x01;
      send_buff[3] = 0b01000011;
      
      lora.write(send_buff, 4); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], BIN);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '7') {
      //ADDH를 설정하기
      send_buff[0] = 0xC0;
      send_buff[1] = 0x00;
      send_buff[2] = 0x01;
      send_buff[3] = 0x01; //주소
      
      lora.write(send_buff, 4); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], BIN);
      }
      else {
        Serial.println("에러");
      }
    }
    else if (c == '8') {
      //ADDL를 설정하기
      send_buff[0] = 0xC0;
      send_buff[1] = 0x01;
      send_buff[2] = 0x01;
      send_buff[3] = 0x02; //주소
      
      lora.write(send_buff, 4); //전송!
      lora.readBytes(recv_buff, 4);

      if (recv_buff[1] == send_buff[1] && recv_buff[2] == send_buff[2]) {
        Serial.println(recv_buff[3], BIN);
      }
      else {
        Serial.println("에러");
      }
    }
  }
}
