#include <ros.h>
#include <std_msgs/Int32.h>

int Relaypin1 = 4;                 // IN1
int Relaypin2 = 5;                 // IN2
int Relaypin3 = 6;                 // IN3
int Relaypin4 = 7;                 // IN4

int count = 0;
boolean flag = LOW;
boolean flag2 = LOW;

boolean stop_msg = LOW;

ros::NodeHandle  nh;

void asms_state(const std_msgs::Int32& cmd_msg) {
  switch (cmd_msg.data) {
    case 0:
      count = 0;
      break;

    case 1:
      count = 1;
      break;

    case 2:
      count = 2;
      break;

    case 3:
      count = 3;
      break;

    case 4:
      count = 4;
      break;
  }
}

ros::Subscriber<std_msgs::Int32> linear_asms_sub("linear_asms", asms_state);

void actuator_stop() {
  digitalWrite (Relaypin1, HIGH);
  digitalWrite (Relaypin2, HIGH);
  digitalWrite (Relaypin3, HIGH);
  digitalWrite (Relaypin4, HIGH);
}

void actuator_down() {
  digitalWrite (Relaypin1, HIGH);
  digitalWrite (Relaypin2, LOW);
  digitalWrite (Relaypin3, LOW);
  digitalWrite (Relaypin4, HIGH);
}

void actuator_up() {
  digitalWrite (Relaypin1, LOW);
  digitalWrite (Relaypin2, HIGH);
  digitalWrite (Relaypin3, HIGH);
  digitalWrite (Relaypin4, LOW);
}

void setup() {
  nh.initNode();
  nh.subscribe(linear_asms_sub);

  pinMode(Relaypin1, OUTPUT);
  pinMode(Relaypin2, OUTPUT);
  pinMode(Relaypin3, OUTPUT);
  pinMode(Relaypin4, OUTPUT);

  actuator_up();
  delay(100);
  actuator_stop();
}

void loop() {
  nh.spinOnce();
  delay(10);

  switch (count) {
    case 0:
      if (flag2 == LOW) {
        actuator_up();
        delay(150);
        actuator_stop();

        flag2 = HIGH;
      }
      break;

    case 1:
      actuator_down();
      break;

    case 2:
      actuator_down();
      break;

    case 3:
      if (flag == LOW) {
        actuator_up();
        delay(800);
        actuator_stop();

        flag = HIGH;
      }

      else {
        count = 5;
      }
      break;

    case 4:
      if (flag == LOW) {
        actuator_up();
        delay(800);
        actuator_stop();

        flag = HIGH;
      }

      else {
        count = 5;
      }
      break;

    case 5:
      actuator_stop();
      delay(3000);
      count = 6;
      break;

    case 6:
      actuator_down();
      break;
  }
}
