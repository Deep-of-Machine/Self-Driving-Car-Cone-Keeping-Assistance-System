#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include <wiringPi.h>
#include <softPwm.h>

#define IN1 19
#define IN2 13
#define IN3 6
#define IN4 5

#define MAX_CAN_IDS 2
#define RANGE 10
#define SUM 78

int current_target = 0;
int direction = 0; // 0 : RIGHT, 1 : LEFT;
bool SENSOR_CAN_SETTING = true;

void setting(void);
void target_check(int, int);
void actuator_run(int, int);
void actuator_stop(void);

int main()
{
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    setting();

    memset(&frame, 0, sizeof(struct can_frame));

    // 1.Create socket
    s = socket(PF_CAN, SOCK_RAW, CAN_RAW);
    if (s < 0)
    {
        perror("socket PF_CAN failed");
        return 1;
    }

    // 2.Specify can1 device
    strcpy(ifr.ifr_name, "can1");
    ret = ioctl(s, SIOCGIFINDEX, &ifr);
    if (ret < 0)
    {
        perror("ioctl failed");
        return 1;
    }

    // 3.Bind the socket to can1
    addr.can_family = PF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;
    ret = bind(s, (struct sockaddr *)&addr, sizeof(addr));
    if (ret < 0)
    {
        perror("bind failed");
        return 1;
    }

    // 4.Define receive rules
    struct can_filter rfilter[1];
    rfilter[0].can_id = 0x001; // receive from CAN0
    rfilter[0].can_mask = CAN_SFF_MASK;
    setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));

    // 5.Receive data and exit
    while (1)
    {
        nbytes = read(s, &frame, sizeof(frame));
        if (nbytes > 0)
        {
            if (frame.data[0] == 1)
            {
                target_check(current_target, frame.data[3]);
            }
            else
            {
                actuator_stop();
            }
        }
    }

    // 6.Close the socket and can1
    close(s);
    system("sudo ifconfig can1 down");

    return 0;
}

void setting(void)
{
    wiringPiSetupGpio();

    softPwmCreate(IN1, 0, 1000);
    softPwmCreate(IN2, 0, 1000);
    softPwmCreate(IN3, 0, 1000);
    softPwmCreate(IN4, 0, 1000);
}

void target_check(int current_target, int new_target)
{
    if ((current_target < (new_target - RANGE)) || (current_target > (new_target + RANGE)))
    {
        // set new target value
        if (current_target < new_target)
            direction = 0;
        else
            direction = 1;

        current_target = new_target;

        actuator_run(current_target, direction);
    }
    else
    {
        actuator_run(current_target, direction);
    }
}

void actuator_run(int current_target, int direction)
{
    // assume that only accept the RIGHT value
    // assume that the sum of the both actuators is constant at 78 (make level)
    int RIGHT = current_target;
    int LEFT = SUM - RIGHT;
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    if (SENSOR_CAN_SETTING)
    {
        memset(&frame, 0, sizeof(struct can_frame));
        s = socket(PF_CAN, SOCK_RAW, CAN_RAW);
        if (s < 0)
        {
            perror("socket PF_CAN failed");
        }
        strcpy(ifr.ifr_name, "can1");
        ret = ioctl(s, SIOCGIFINDEX, &ifr);
        if (ret < 0)
        {
            perror("ioctl failed");
        }
        addr.can_family = PF_CAN;
        addr.can_ifindex = ifr.ifr_ifindex;
        ret = bind(s, (struct sockaddr *)&addr, sizeof(addr));
        if (ret < 0)
        {
            perror("bind failed");
        }
        struct can_filter rfilter[1];
        rfilter[0].can_id = 0x003; // receive from CAN2
        rfilter[0].can_mask = CAN_SFF_MASK;
        setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));

        SENSOR_CAN_SETTING = false;
    }

    nbytes = read(s, &frame, sizeof(frame));
    if (nbytes > 0)
    {
        if ((frame.data[0] < (RIGHT - 2)) || (frame.data[0] > (RIGHT + 2)))
        {
            if (direction == 0)
            {
                softPwmWrite(IN1, 0);
                softPwmWrite(IN2, 1000);
                softPwmWrite(IN3, 0);
                softPwmWrite(IN4, 1000);
            }
            else
            {
                softPwmWrite(IN1, 1000);
                softPwmWrite(IN2, 0);
                softPwmWrite(IN3, 1000);
                softPwmWrite(IN4, 0);
            }

            delay(1000);
        }
        else
        {
            // if sensor value is in error range -> stop moving
            actuator_stop();
        }
    }
}

void actuator_stop()
{
    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 0);
    softPwmWrite(IN3, 0);
    softPwmWrite(IN4, 0);
}
