#include <SoftwareSerial.h>
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;
std_msgs::Int16 int16_msg;
ros::Publisher chatter("/ASMS", &int16_msg);

SoftwareSerial lora(2, 3);

int led = 8;
int kill_num = 5;
int asms_status = 3;
union {
  int i;
  byte b[2];
} myunion;

void setup() {
  Serial.begin(9600);
  lora.begin(9600);

  pinMode(led, OUTPUT);
  pinMode(kill_num, INPUT);

  nh.initNode();
  nh.advertise(chatter);

  int16_msg.data = asms_status;
}

void loop() {
  
  Serial.println(asms_status);

  if (lora.available()) {
    lora.readBytes(myunion.b, 2);

    if (myunion.i == 3) {
      Serial.println("OFF");
      digitalWrite(led, LOW);
      asms_status = 3;
    } else if (myunion.i == 2) {
      Serial.println("Emergency");
      asms_status = 2;
    } else if (myunion.i == 1) {
      asms_status = 1;
      Serial.println("ON");
      digitalWrite(led, HIGH);
    } else {
      Serial.println("Exception");
    }
  }

  int16_msg.data = asms_status;
  chatter.publish(&int16_msg);
  nh.spinOnce();
  delay(100);
}
