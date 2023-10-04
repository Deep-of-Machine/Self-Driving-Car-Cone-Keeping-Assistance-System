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

#define MOTOR_OUT 21
#define RANGE 5 // error range
int now_target = 0;

int initial = 1;

void setting(void);
void motor_run(int);
void motor_stop(void);

int main()
{
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    time_t start_time = time(NULL);

    setting();

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
    rfilter[0].can_id = 0x123; // receive from CAN0
    rfilter[0].can_mask = CAN_SFF_MASK;
    setsockopt(s, SOL_CAN_RAW, CAN_RAW_FILTER, &rfilter, sizeof(rfilter));

    // 5.Receive data and exit
    while (1)
    {
        nbytes = read(s, &frame, sizeof(frame));
        if (nbytes > 0)
        {
            if (frame.data[0] == 1)
            { // auto state
                if(initial) {
                    delay(3000);
                    initial = 0;
                }
                
                if (frame.data[4] == 1) {
                    // detect stop line
                    motor_stop();
                } else {
                    motor_run(frame.data[1]);
                }
            }
            else
            {
                initial = 1;
                motor_stop();
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

    softPwmCreate(MOTOR_OUT, 0, 255);

    softPwmWrite(MOTOR_OUT, 0);
}

void motor_run(int new_target)
{
    softPwmWrite(MOTOR_OUT, new_target);
}

void motor_stop(void)
{
    softPwmWrite(MOTOR_OUT, 0);
}
