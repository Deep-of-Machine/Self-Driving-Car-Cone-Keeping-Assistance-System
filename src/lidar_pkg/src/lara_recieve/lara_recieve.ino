#include <SoftwareSerial.h>
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

std_msgs::Int16 asms_msg;
std_msgs::Int16 steering_msg;

ros::Publisher asms_chatter("/ASMS", &asms_msg);
ros::Publisher steering_chatter("/steering_angle_self", &steering_msg);

SoftwareSerial lora(2, 3);

int asms_status = 3;

union {
  int i;
  byte b[2];
} myunion;

int kill = 0;
int self_driving = 0 ;
int val = 0;

void setup() {
  Serial.begin(57600);
  lora.begin(9600);

  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(A0, INPUT);

  nh.initNode();
  nh.advertise(asms_chatter);
  nh.advertise(steering_chatter);

  asms_msg.data = asms_status;
}

void loop() {



  self_driving = digitalRead(7);
  kill = digitalRead(6);

  asms_msg.data = kill;
  asms_chatter.publish(&asms_msg);

  asms_msg.data = self_driving;
  asms_chatter.publish(&asms_msg);
  val = analogRead(A0);
  val = int((float(val) / 1023) * 78);

  steering_msg.data = val;  // Set the analog value
  steering_chatter.publish(&steering_msg);  // Publish the analog value

  if (lora.available()) {
    lora.readBytes(myunion.b, 2);

    if (myunion.i == 3) {
      asms_status = 3;

    } else if (myunion.i == 2) {
      asms_status = 2;
    } else if (myunion.i == 1) {
      asms_status = 1;
    }
  }

  if (asms_status == 1) {
    if (self_driving == 1) {
      asms_status = 3;
    }
    if (kill == 1) {
      asms_status = 2;
    }

  } else {


    if (kill == 1) {
      asms_status = 2;
    }
    if (self_driving == 1) {
      asms_status = 3;
    }

  }

  asms_msg.data = asms_status;
  asms_chatter.publish(&asms_msg);
  //Serial.println(asms_status);

  nh.spinOnce();
  delay(500);
}
