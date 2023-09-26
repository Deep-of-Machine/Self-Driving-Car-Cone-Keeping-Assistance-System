#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float64.h>  // For the yaw value

ros::NodeHandle nh;

int relay1 = 2;  // relay 1, red actuator
int relay2 = 3;
int target = 450;
float threshold = 0.1;  // 1.4mm

//double current_yaw = 0.0;  // Variable to store the current yaw value

std_msgs::Float64 sensor_msg;
// ros::Publisher sensor_pub("sensor_value_topic", &sensor_msg);

void yawCallback(const std_msgs::Float64& msg) {
  target = msg.data;  // Store the current yaw value
}

ros::Subscriber<std_msgs::Float64> yaw_sub("/filtered/imu/yaw", yawCallback);  // Subscribe to the yaw topic

void setup() {
  nh.initNode();
  //nh.advertise(sensor_pub);
  //  nh.subscribe(target_sub);
  nh.subscribe(yaw_sub);  // Add the yaw subscriber

  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(A0, INPUT);
}

void loop() {
  int sensorValue = analogRead(A0);
  //  sensor_msg.data = sensorValue;
  //  sensor_pub.publish(&sensor_msg);
  nh.spinOnce();

  // You can now use current_yaw in your logic
  // For example, you might use current_yaw to decide how to set your relays

  if ((100 < target) && (target < 900)) && ((100 < sensorValue) && (sensorValue < 900)) {

    if (((target - target * threshold) < sensorValue) && (sensorValue < (target + target * threshold))) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, HIGH);
    } else if (target > sensorValue) {
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, HIGH);
    } else if (target < sensorValue) {
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, LOW);
    }

  }
  else {
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);
  }

  delay(50);
}
