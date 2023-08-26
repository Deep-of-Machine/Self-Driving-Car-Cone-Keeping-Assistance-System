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

#define MOTOR_OUT 9
#define range 10 // error range
int now_target = 0;

void setting(void);
void target_check(int, int);
void motor_run(int);
void motor_stop(void);

int main()
{
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    setting(); // Pin Setting

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
            { // auto state
                target_check(frame.data[1], frame.data[2]);
            }
            else
            {
                motor_stop();
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

    softPwmCreate(MOTOR_OUT, 0, 200);
}

void target_check(int current_speed, int new_target)
{
    if ((current_speed < (new_target - range)) || (current_speed > (new_target + range)))
    {
        // set new target value
        now_target = new_target;

        motor_run(now_target);
    }
    else
    {
        motor_run(now_target);
    }
}

void motor_run(int new_target)
{
    // add PID code
    softPwmWrite(MOTOR_OUT, new_target);
}

void motor_stop(void)
{
    softPwmWrite(MOTOR_OUT, 0);
}
