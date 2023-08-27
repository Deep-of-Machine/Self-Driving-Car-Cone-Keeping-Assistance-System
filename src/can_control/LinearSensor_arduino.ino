#include <SPI.h>
#include <mcp2515.h>

#define master 0x003

struct can_frame canMsg;
const int analogPin = A0;  // 리니어 센서 연결된 아날로그 핀 번호
const float sensorLength = 78.0;  // 센서의 총 길이 (mm)

MCP2515 mcp2515(10);

void setup() {
  Serial.begin(9600);

	mcp2515.reset();
	mcp2515.setBitrate(CAN_500KBPS);
  mcp2515.setNormalMode();
}

void loop() {
  int sensorValue = analogRead(analogPin);  // 아날로그 핀으로부터 값을 읽어옴
  float voltage = sensorValue * (5.0 / 1023.0);  // 아날로그 값을 전압으로 변환
  float distance = (voltage * sensorLength) / 5.0;  // 전압 값을 거리로 변환 (단위: mm)
 
	// distance 값을 소수점 2자리까지만 저장할 수 있도록
	int trans = distance * 100;
	distance = trans / 100;

  Serial.print("Distance: ");
  Serial.println(distance);  // 소수점 2자리까지 출력되는지 확인
  
	byte data[8] = {distance, 0x00,0x00,0x00,0x00,0x00,0x00,0x00};
	mcp2515_send(master, data);
}

void mcp2515_send(unsigned int id, byte data[]){
  canMsg.can_id  = id;
  canMsg.can_dlc = 8;
  for(int i =0;i<8;i++){
    canMsg.data[i] = data[i];
  }
  mcp2515.sendMessage(&canMsg);
  // Serial.println("[CAN1으로 보낸 메시지]");
  // Serial.println(id,HEX);
  // for (int i = 0; i<canMsg1.can_dlc; i++)  {  // print the data
      // Serial.print(canMsg1.data[i],HEX);
      // Serial.print(" ");
  // }
  // Serial.println();
}
