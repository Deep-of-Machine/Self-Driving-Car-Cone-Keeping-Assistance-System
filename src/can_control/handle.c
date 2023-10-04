#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <net/if.h>
#include <fcntl.h>
#include <linux/spi/spidev.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include <wiringPi.h>
#include <softPwm.h>
#include <time.h>

#define IN1 5
#define IN2 6

#define HIGH 1
#define LOW 0

#define RANGE 2
#define SUM 78
#define MEDIUM 42

int current_target = 0;
int direction = 0;

// CAN variable
static const char *spi_device = "/dev/spidev0.2";
static uint8_t spi_mode = 0;
static uint8_t spi_bits_per_word = 8;
static uint32_t spi_speed = 500000;

static uint8_t tx_buffer[3];
static uint8_t rx_buffer[3];

static int spi_fd;

int setting(void);
static void select_channel(uint8_t);
void set_medium(void);
void target_check(int);
void actuator_run(int);
void actuator_stop(void);

int main()
{
    int ret;
    int s, nbytes;
    struct sockaddr_can addr;
    struct ifreq ifr;
    struct can_frame frame;

    memset(&frame, 0, sizeof(struct can_frame));

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
            if (frame.data[0] == 2) // emergency 상태
            {
                actuator_stop();
            }
            else // auto && passive 상태
            {
                if (frame.data[4] == 1) {
                    actuator_stop();
                } else {
                    target_check(frame.data[3]);
                }
            }
        }
    }

    // 6.Close the socket and can1
    close(s);
    close(spi_fd);

    return 0;
}

int setting(void)
{
    wiringPiSetupGpio();

    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);

    // linear sensor accept
    spi_fd = open(spi_device, O_RDWR);
    if (spi_fd == -1)
    {
        perror("Failed to open SPI device");
        return 1;
    }

    if (ioctl(spi_fd, SPI_IOC_WR_MODE, &spi_mode) == -1)
    {
        perror("Failed to set SPI mode");
        close(spi_fd);
        return 1;
    }

    if (ioctl(spi_fd, SPI_IOC_WR_BITS_PER_WORD, &spi_bits_per_word) == -1)
    {
        perror("Failed to set SPI bits per word");
        close(spi_fd);
        return 1;
    }

    if (ioctl(spi_fd, SPI_IOC_WR_MAX_SPEED_HZ, &spi_speed) == -1)
    {
        perror("Failed to set SPI speed");
        close(spi_fd);
        return 1;
    }

    return 0;
}

static void select_channel(uint8_t channel)
{
    tx_buffer[0] = 0x01;                  // Start bit
    tx_buffer[1] = 0x80 | (channel << 4); // Single-ended mode, channel selection
    tx_buffer[2] = 0x00;                  // Dummy byte

    struct spi_ioc_transfer tr = {
        .tx_buf = (unsigned long)tx_buffer,
        .rx_buf = (unsigned long)rx_buffer,
        .len = 3,
        .speed_hz = spi_speed,
        .bits_per_word = spi_bits_per_word,
    };

    ioctl(spi_fd, SPI_IOC_MESSAGE(1), &tr);
}

void target_check(int new_target)
{
    select_channel(0);

    int adc_value = ((rx_buffer[1] & 0x03) << 8) | rx_buffer[2];

    int min_value = 0;
    int max_value = SUM;

    if (adc_value < min_value)
    {
        adc_value = min_value;
    }
    else if (adc_value > max_value)
    {
        adc_value = max_value;
    }

    float mm_value = (float)(adc_value);
    mm_value = (mm_value/1023)*SUM;

    if ((mm_value < new_target - RANGE))
    {
        actuator_run(1);
    }
    else if ((mm_value > new_target + RANGE))
    {
        actuator_run(0);
    }
    else
    {
        actuator_stop();
    }
}

void actuator_run(int direction)
{
    if (direction == 0)
    {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        delay(1);
    }
    else
    {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        delay(1);
    }
}

void actuator_stop()
{
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, HIGH);
    delay(1);
}

