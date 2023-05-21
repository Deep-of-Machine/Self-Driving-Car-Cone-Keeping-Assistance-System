// full brake 600ms
// half brake 150ms

#include <ros.h>
#include <std_msgs/Int32.h>

int Relaypin1 = 4;                 // IN1
int Relaypin2 = 5;                 // IN2
int Relaypin3 = 6;                 // IN3
int Relaypin4 = 7;                 // IN4

bool stop_msg = LOW;

ros::NodeHandle  nh;

void asms_state(const std_msgs::Int32& cmd_msg) {
  switch (cmd_msg.data) {
    case 1:
      actuator_down();
      break;

    case 2:
      actuator_stop();
      break;

    case 3:
      actuator_up();
      delay(300);
      actuator_stop();
      break;

    case 4:
      actuator_down();
      delay(300);
      actuator_stop();
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

  actuator_down();
  delay(1000);
  actuator_stop();
}

void loop() {

}
