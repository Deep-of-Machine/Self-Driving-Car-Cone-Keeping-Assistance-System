#include <ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/Float64.h>  // For the yaw value
#include <math.h> // For M_PI

ros::NodeHandle nh;

int relay1 = 2;  // relay 1, red actuator
int relay2 = 3;
float target = 556;
float threshold = 0.03;  // 1.4mm
int asms_status = 1;
float center = 556;
int trigger = 0;
void targetCallback(const std_msgs::Float64& msg) {
  target = msg.data;
}

void asmsCallback(const std_msgs::Int8& msg) {
  asms_status = msg.data;
}

ros::Subscriber<std_msgs::Float64> sub1("/steering_angle", targetCallback);
ros::Subscriber<std_msgs::Int8> sub2("/asms_status", asmsCallback);

void setup() {
  Serial.begin(115200);
  nh.initNode();
  nh.subscribe(sub1);
  nh.subscribe(sub2);


  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  pinMode(A1, INPUT);
}

void loop() {
  nh.spinOnce();  // To receive messages

  int sensorValue1 = analogRead(A1);
  Serial.print("sensor1: ");
  Serial.println(sensorValue1);
  Serial.println(target);
  delay(50);
  int sensorValue = sensorValue1;

  switch (asms_status) {
    case 1:           // AS-ON
      Serial.println("AS-ON");
      if (trigger > 0) {
        digitalWrite(relay1, LOW);
        digitalWrite(relay2, HIGH);
        Serial.println("left");
        delay(7000);
        digitalWrite(relay1, HIGH);
        digitalWrite(relay2, LOW);
        Serial.println("right");
        delay(7000);
      }
      trigger = 0;
      if (((0 <= target) && (target <= 1024)) && ((0 < sensorValue) && (sensorValue < 1024))) {
        if (((target - target * threshold) < sensorValue) && (sensorValue < (target + target * threshold))) {
          digitalWrite(relay1, HIGH);
          digitalWrite(relay2, HIGH);
          Serial.println("target");
          delay(50);
        } else if (target < sensorValue) {
          digitalWrite(relay1, LOW);
          digitalWrite(relay2, HIGH);
          Serial.println("on");
          delay(50);
        } else if (target > sensorValue) {
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
      break;
    case 2:          // AS-Emergency
      break;
    case 3:         // AS-OFF
      if (trigger == 0) {
        digitalWrite(relay1, LOW);
        digitalWrite(relay2, HIGH);
        Serial.println("left");
        delay(5000);
        digitalWrite(relay1, HIGH);
        digitalWrite(relay2, LOW);
        Serial.println("right");
        delay(5000);
        trigger = trigger + 1;
      }

      if (((center - center * 0.1) < sensorValue) && (sensorValue < (center + center * 0.1))) {
        digitalWrite(relay1, HIGH);
        digitalWrite(relay2, HIGH);
        Serial.println("target");
        delay(20);
      } else if (center < sensorValue) {
        digitalWrite(relay1, LOW);
        digitalWrite(relay2, HIGH);
        Serial.println("on");
        delay(20);
      } else if (center > sensorValue) {
        digitalWrite(relay1, HIGH);
        digitalWrite(relay2, LOW);
        Serial.println("down");
        delay(20);
      }
      break;

    default:
      Serial.println("ASMS receive Error");
      break;
  }
}
