#include <ros.h>
#include <std_msgs/Int32.h>
#include <SoftwareSerial.h>
#include <Adafruit_NeoPixel.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial lora(10, 11);

// e-stop in car #1
#define bt_estop_1 2

// e-stop in car #2
#define bt_estop_2 3

//LED's PIN NUM
#define PIN 5

//maximum LED number
#define NUM_LEDS 184

//LED's brightness
#define BRIGHT 255

//DFPlayer setting (will be used in "executed_CMD" function)
#define Start_Byte 0x7E //start value
#define Version_Byte 0xFF   //version value
#define Command_Length 0x06   //length
#define End_Byte 0xEF   //end value
#define Acknowledge 0x00    //feedback false value

//create a NeoPixel strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

ros::NodeHandle  nh;

int count = 0;
int stop_msg = LOW;
boolean flag  = false;
boolean flag2 = LOW;

unsigned long currentMillis;
unsigned long previousMillis = 0;

std_msgs::Int32 str_msg;
ros::Publisher asms_control("asms_control", &str_msg);

void stop_cb( const std_msgs::Int32& cmd_msg) {
  if (cmd_msg.data == 1) {
    if (flag2 == LOW) {
      count = 3;
    }
    else {
      count = 4;
    }
  }
}

ros::Subscriber<std_msgs::Int32> stop_sub("stop_sign", stop_cb);

void bt_count() {
  count = 4;
}

union {
  int i;
  byte b[2];
} myunion;

void estop_remote() {
  if (lora.available()) {
    lora.readBytes(myunion.b, 2);

    if (count == 0) {
      if (myunion.i == 30) {
        count = 1;
        previousMillis = currentMillis;
      }
    }
    else if (count > 0) {
      if (myunion.i == 20) {
        count = 4;
      }
    }
  }
}

void specify_Volume(byte level) {
  execute_CMD(0x06, 0x00, level);
}

void specify_Track(int16_t track) {
  execute_CMD(0x03, highByte(track), lowByte(track));
}

void execute_CMD(byte CMD, byte Par1, byte Par2) {
  int16_t checksum = -(Version_Byte + Command_Length + CMD + Acknowledge + Par1 + Par2);

  byte Command_line[10] = { Start_Byte, Version_Byte, Command_Length, CMD, Acknowledge, Par1, Par2, highByte(checksum), lowByte(checksum), End_Byte};

  for (byte k = 0; k < 10; k++) {
    Serial1.write(Command_line[k]);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  lora.begin(9600); //아두이노하고 로라모듈하고의 통신라인!
  strip.begin();

  pinMode(bt_estop_1, INPUT_PULLUP);
  pinMode(bt_estop_2, INPUT_PULLUP);

  nh.initNode();
  nh.advertise(asms_control);
  nh.subscribe(stop_sub);

  delay(100);
  attachInterrupt(digitalPinToInterrupt(bt_estop_1), bt_count, FALLING);
  delay(100);
  attachInterrupt(digitalPinToInterrupt(bt_estop_2), bt_count, FALLING);

  specify_Volume(20); // set Volume
}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(10);

  currentMillis = millis();

  estop_remote();

  switch (count) {
    case 0:  // AS-Ready
      for (int idx = 0; idx < 184; ++idx) {
        strip.setPixelColor(idx, BRIGHT, BRIGHT, 0);
      }

      strip.show();
      break;

    case 1:  // AS-Ready -> 1sec delay -> AS-Driving
      if (currentMillis - previousMillis > 800) {
        count = 2;
      }
      break;

    case 2:  // AS-Driving
      if (currentMillis - previousMillis > 1000) {
        previousMillis = currentMillis;

        if (flag == false) {
          for (int idx = 0; idx < 184; ++idx) {
            strip.setPixelColor(idx, 0, 0, 0);
          }

          strip.show();

          flag = true;

          specify_Track(1);
        }

        else {
          for (int idx = 0; idx < 184; ++idx) {
            strip.setPixelColor(idx, BRIGHT, BRIGHT, 0);
          }

          strip.show();

          flag = false;
        }
      }

      break;

    case 3:  // AS-Finished
      for (int idx = 0; idx < 184; ++idx) {
        strip.setPixelColor(idx, 0, 0, BRIGHT);
      }

      strip.show();

      //execute_CMD(0x0E, 0x00, 0x00); //stop playing bgm
      break;

    case 4:  // AS-Emergency
      flag2 = HIGH;

      if (currentMillis - previousMillis > 1000) {
        previousMillis = currentMillis;

        if (flag == false) {
          for (int idx = 0; idx < 184; ++idx) {
            strip.setPixelColor(idx, 0, 0, BRIGHT);
          }

          strip.show();

          flag = true;
        }

        else {
          for (int idx = 0; idx < 184; ++idx) {
            strip.setPixelColor(idx, 0, 0, 0);
          }

          strip.show();

          flag = false;
        }
      }
      break;
  }

  str_msg.data = count;
  asms_control.publish( &str_msg );
}
