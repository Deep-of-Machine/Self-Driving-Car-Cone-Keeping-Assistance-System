#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float64.h>  // For the yaw value
#include <math.h> // For M_PI

ros::NodeHandle nh;

std_msgs::Float64 yaw_msg;  // To store the received yaw value

int relay1 = 2;  // relay 1, red actuator
int relay2 = 3;
int relay3 = 4;  // relay 1, red actuator
int relay4 = 5;
float target = 512;
float threshold = 0.03;  // 1.4mm

int map_yaw_to_sensor(float yaw_value) {
  // Define the range for the yaw values and sensor values
  float yaw_min = -M_PI;
  float yaw_max = M_PI;
  int sensor_min = 924;
  int sensor_max = 100;

  // Map the yaw value to the sensor range
  int mapped_value = sensor_min + ((yaw_value - yaw_min) * (sensor_max - sensor_min)) / (yaw_max - yaw_min);

  return round(mapped_value);
}



void yawCallback(const std_msgs::Float64& msg) {
  target = msg.data;
}


ros::Subscriber<std_msgs::Float64> sub("/steering_angle", yawCallback);
void setup() {
  Serial.begin(57600);
  nh.initNode();
  nh.subscribe(sub);
  
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  digitalWrite(relay3, HIGH);
  digitalWrite(relay4, HIGH);
  pinMode(A0, INPUT);
}

void loop() {
  nh.spinOnce();  // To receive messages
  
  int sensorValue = analogRead(A0);
  Serial.print("sensor");
  Serial.println(sensorValue);
  Serial.println(target);
  delay(20);

  if (((0 <= target) && (target <= 1024)) && ((0 < sensorValue) && (sensorValue < 1024))) {
    if (((target - target * threshold) < sensorValue) && (sensorValue < (target + target * threshold))) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, HIGH);
      digitalWrite(relay3, HIGH);
      digitalWrite(relay4, HIGH);
      
      Serial.println("target");
      delay(50);
    } else if (target > sensorValue) {
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, HIGH);
      digitalWrite(relay3, HIGH);
      digitalWrite(relay4, LOW);
      Serial.println("on");
      delay(50);
    } else if (target < sensorValue) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, LOW);
      digitalWrite(relay3, LOW);
      digitalWrite(relay4, HIGH);
      Serial.println("down");
      delay(50);
    }
  }
  else {
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);
    digitalWrite(relay3, HIGH);
    digitalWrite(relay4, HIGH);
    Serial.println("Trash");
  }

   // Optionally use current_yaw in your code
  

  delay(50);
}
