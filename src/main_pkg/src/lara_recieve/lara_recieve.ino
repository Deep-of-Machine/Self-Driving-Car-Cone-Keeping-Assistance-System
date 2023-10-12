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
int kill_D =0;
int kill_B = 0;
int self_driving = 0 ;
int val = 0;

void setup() {
  Serial.begin(9600);
  lora.begin(9600);

  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(A5, INPUT);

  nh.initNode();
  nh.advertise(asms_chatter);
  nh.advertise(steering_chatter);

  asms_msg.data = asms_status;
}

void loop() {



  self_driving = digitalRead(6);
  kill_D = digitalRead(5);
  kill_B = digitalRead(7);
  val = analogRead(A5);
  val = int((float(val) / 1023) * 78);

  steering_msg.data = val;  // Set the analog value
  steering_chatter.publish(&steering_msg);  // Publish the analog value

  //  Serial.print("asms_status : ");
  //  Serial.println(asms_status);
  //
  //Serial.print("kill_D : ");
  //Serial.println(kill_D);
  //
  //Serial.print("kill_B : ");
  //Serial.println(kill_B);
  //
  //Serial.print("Self_driving : ");
  //Serial.println(self_driving);
  //
  //  Serial.print("val");
  //  Serial.println(val);
  if (lora.available()) {
    lora.readBytes(myunion.b, 2);
    Serial.println("dd");
    if (myunion.i == 3) {
      asms_status = 3;

    } else if (myunion.i == 2) {
      asms_status = 2;
    } else if (myunion.i == 1) {
      asms_status = 1;
    }
  }

  if (asms_status == 1) {
    Serial.println("aa");
    if (self_driving == 1) {
      asms_status = 3;
    }
    if (kill_B == 1 || kill_D == 1) {
      asms_status = 2;
      Serial.println("kk");
    }

  } else {
    if (kill_B == 1|| kill_D == 1) {
      asms_status = 2;
      Serial.println("dd");
    }
    if (self_driving == 1) {
      asms_status = 3;
      Serial.println("cc");
    }

  }

  asms_msg.data = asms_status;
  asms_chatter.publish(&asms_msg);

  nh.spinOnce();
  delay(100);
}
