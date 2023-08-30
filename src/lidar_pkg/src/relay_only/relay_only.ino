#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float64.h>  // For the yaw value

ros::NodeHandle nh;

std_msgs::Float64 yaw_msg;  // To store the received yaw value

int relay2 = 9;  // relay 1, red actuator
int relay1 = 10;
int target = 512;
float threshold = 0.03;  // 1.4mm

void yawCallback(const std_msgs::Float64& msg) {
  target = msg.data;
}

ros::Subscriber<std_msgs::Float64> sub("/filtered/imu/yaw", yawCallback);
void setup() {
  Serial.begin(57600);
  nh.initNode();
  nh.subscribe(sub);
  
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  pinMode(A0, INPUT);
}

void loop() {
  nh.spinOnce();  // To receive messages
  
  int sensorValue = analogRead(A0);
  Serial.print("sensor");
  Serial.println(sensorValue);
  delay(20);

  if (((35 <= target) && (target <= 995)) && ((0 < sensorValue) && (sensorValue < 1024))) {
    if (((target - target * threshold) < sensorValue) && (sensorValue < (target + target * threshold))) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, HIGH);
      Serial.println("target");
      delay(50);
    } else if (target > sensorValue) {
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, HIGH);
      Serial.println("on");
      delay(50);
    } else if (target < sensorValue) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, LOW);
      Serial.println("down");
      delay(50);
    }
  }
  else {
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);
    Serial.println("Trash");
  }

   // Optionally use current_yaw in your code
   
  Serial.println(target);

  delay(50);
}
