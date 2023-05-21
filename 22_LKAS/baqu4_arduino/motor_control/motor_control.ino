/* CODE FOR CONTROLL MOTOR
   Belows are concept that we must consider

  [변수]
  -- 현재 모터 속도 : 급제동을 방지하기 위해 이 변수가 필요. 그러나 이는 엑추에이터와 연관되어있기에 폐기
  -- 제동 영역 임계값 : 빨간 콘이 많아지는 구간이 바로 제동 구간. 이를 인식하는 기준이 필요
  -- LoRa 통신 신호 READ : ASMS 상태에 따라 다른 모터 제어를 수행하기 위함

  [6가지의 ASMS 상태]
  -- 모터가 stop 하는 기능은 총 2개. 그러나 조향과 제동 상태 또한 고려하여 코드 작성
  -- 바로 급제동 혹은 감속 제동 中, 택 1
  -- 현재는 급제동을 선택

  [미션 1 : 제동]
  -- 주행 속도 노 상관. 느려도 괜찮음
  -- 그러나 제동 구간 이내에 들어오면 무조건 정지해야한다. (모터 속도 0 && 엑추에이터)

  [미션 2 : 가속]
  -- 제동 미션에 가속 성능 평가가 추가됨

*/

/* INCLUDE */
#include <ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Float32.h>

/* DEFINE */
#define throttle 3                                // !--> throttle pin from KLS controller 
#define hall_sensor A1                             // !--> hall sensor

#define R 0.23
#define TOOTHNUM 23
#define M_PI 3.14159265358979323846

/* GLOBAL VARIABLE */
float curr_speed;                                   // !--> speed that reads from hall effect sensor
int input_speed;                                  // !--> speed which user want to set
int flag;
int VAL;
int curr_status;

ros::NodeHandle  nh;

std_msgs::Float32 str_msg;
ros::Publisher chatter("RPM", &str_msg);

float diffT() {
  while (flag < 3000) {
    VAL = analogRead(hall_sensor);
    ++flag;
    if (VAL >= 300) {
      flag = 0;
      break;
    }
  }

  float start_t = millis(), dt;

  while (flag < 3000) {
    VAL = analogRead(hall_sensor);
    ++flag;
    if (VAL <= 100) {
      flag = 0;
      break;
    }
  }

  while (flag < 3000) {
    VAL = analogRead(hall_sensor);
    ++flag;
    if (VAL >= 300) {
      flag = 0;
      break;
    }
  }

  if (flag >= 2999) {
    flag = 0;
    return 0;
  }

  float end_t = millis();

  dt = (end_t - start_t) / 1000;

  return dt;
}

// 현재 모터의 속도를 읽음
float read_speed() {
  float dt = diffT();

  if (dt == 0) return 0;

  float w = 2 * M_PI / TOOTHNUM / dt;
  float RPM = w * 60 / 2 / M_PI;
  float V = 0.1885 * RPM * R * 2;

  return V;
}

// 입력 값에 맞게 throttle 핀에 인가되는 값 설정 (속도 설정)
void set_speed(int input) {
  analogWrite(throttle, input);
}

// 현재 속도가 0이 될 때까지 감속
void motor_deceleration(float speed) {
  for (int i = speed; speed <= 0; i--) {
    set_speed(i);
  }
}

// ASMS 상태를 읽고 이를 문자열로 변환
void read_ASMS_status( const std_msgs::Int32& asms_status) {
  switch (asms_status.data) {
    case 0: // ready
      curr_status = 0;
      break;

    case 1: // delay
      curr_status = 1;
      break;

    case 2: // driving
      curr_status = 2;
      break;

    case 3: // finished
      curr_status = 3;
      break;

    case 4: // emergency
      curr_status = 4;
      break;
  }
}

ros::Subscriber<std_msgs::Int32> motor_asms_sub("motor_asms", read_ASMS_status);

// 제동 영역과 조향 상태에 따라 자율적으로 주행
void auto_drive() {
  switch (curr_status) {
    case 0:
      set_speed(0);
      break;

    case 1:
      set_speed(0);
      break;

    case 2:
      set_speed(250);                 // ! --> input speed that defined with user's want
      break;

    case 3:
      set_speed(0);
      break;

    case 4:
      set_speed(0);
      break;
  }
}

void setup() {
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(motor_asms_sub);

  pinMode(throttle, OUTPUT);
  pinMode(hall_sensor, INPUT_PULLUP);
}

void loop() {
  nh.spinOnce();
  delay(10);

  float V = read_speed();

  str_msg.data = V;
  chatter.publish( &str_msg );

  auto_drive();
}
