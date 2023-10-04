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
#include <time.h>

#define IN1 19
#define IN2 13

#define IN3 7

int initial = 1;

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
                if ( initial == 1 ) {
                    brake_off();
                    softPwmWrite(IN3, 0);
                    initial = 0;
                }
                
                if (frame.data[4] == 1) {
                    brake_on();
                } else if (frame.data[2] == 1) {
                    // for voltage brake execute
                    softPwmWrite(IN3, 1000);
                    delay(1);
                } else if(frame.data[2] == 0) {
                    softPwmWrite(IN3, 0);
                }
            } else if (frame.data[0] == 2)
            { // emergency state
                initial = 1;
                brake_on();
            } else {
                // passive state
                initial = 0;
                softPwmWrite(IN3, 0);
                brake_off();
            }
        }
    }

    // 6.Close the socket and can1
    close(s);

    return 0;
}

void setting(void)
{
    wiringPiSetupGpio();

    softPwmCreate(IN1, 0, 1000);
    softPwmCreate(IN2, 0, 1000);
    softPwmCreate(IN3, 0, 1000);
}

void brake_on(void)
{
    softPwmWrite(IN1, 1000);
    softPwmWrite(IN2, 0);

    delay(2000);

    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 0);
}

void brake_off(void)
{
    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 1000);

    delay(4000);

    softPwmWrite(IN1, 0);
    softPwmWrite(IN2, 0);
}
