#include <stdio.h>
#include <stdlib.h>
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

void setting(void);
void brake_on(void);
void brake_off(void);

int main()
{
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    memset(&frame, 0, sizeof(struct can_frame));

    system("sudo ip link set can1 type can bitrate 100000");
    system("sudo ifconfig can1 up");
    printf("this is a can receive demo\r\n");

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
            { // ready state
                setting();
            }
            else if (frame.data[0] == 4)
            { // emergency state
                brake_on();
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

    // do I need it ?
    // SET EVERY ACTUATOR RESET
    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 1000);
    softPwmWrite(IN3, 0);
    softPwmWrite(IN4, 1000);

    delay(1000);

    brake_off();
}

void brake_on(void)
{
    softPwmWrite(IN1, 1000);
    softPwmWrite(IN2, 0);
    softPwmWrite(IN3, 1000);
    softPwmWrite(IN4, 0);

    delay(10000);

    brake_off();
}

void brake_off(void)
{
    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 0);
    softPwmWrite(IN3, 0);
    softPwmWrite(IN4, 0);
}