#include <SoftwareSerial.h>

//DFPlayer setting (will be used in "executed_CMD" function)
#define Start_Byte 0x7E //start value
#define Version_Byte 0xFF   //version value
#define Command_Length 0x06   //length
#define End_Byte 0xEF   //end value
#define Acknowledge 0x00    //feedback false value

SoftwareSerial bgm(18, 19); //RX1, TX1

void specify_Volume(byte level) {
  executed_CMD(0x06, 0x00, level);
}

void specify_Track(int16_t track) {
  executed_CMD(0x03, highByte(track), lowByte(track));
}

void executed_CMD(byte CMD, byte Par1, byte Par2) {
  int16_t checksum = -(Version_Byte + Command_Length + CMD + Acknowledge + Par1 + Par2);

  byte Command_line[10] = {Start_Byte, Version_Byte, Command_Length, CMD, Acknowledge, Par1, Par2, highByte(checksum), lowByte(checksum), End_Byte};

  for (byte k = 0; k < 10; k++) {
    bgm.write(Command_line[k]);
  }
}

specify_Track(1); //play only Auto signal bgm
specify_Track(2); //play Auto signal + engine sound
executed_CMD(0x0E, 0x00, 0x00); //stop playing bgm

void setup() {
  // put your setup code here, to run once:
  bgm.begin(9600);

  specify_Volume(20); // set Volume
}

void loop() {
  // put your main code here, to run repeatedly:

}
