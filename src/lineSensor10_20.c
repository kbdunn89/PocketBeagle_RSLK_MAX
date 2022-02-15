#include <gpiod.h>
#include <unistd.h>
#include <stdio.h>

const char *chipname2 = "gpiochip2";
const char *chipname0 = "gpiochip0";

struct gpiod_chip *chip2;
struct gpiod_chip *chip0;

struct gpiod_line *QTR3;
struct gpiod_line *QTR4;
//struct gpiod_line *QTR5;
//truct gpiod_line *QTR2;
unsigned int val = 0x00;
unsigned long count = 0;

void init() {
    // Open GPIO chip
    chip0 = gpiod_chip_open_by_name(chipname0);
    chip2 = gpiod_chip_open_by_name(chipname2);
    
    // Open GPIO lines
    // chip info at gpioinfo
    //QTR2 = gpiod_chip_get_line(chip0, 4);        // P1.12
    //QTR5 = gpiod_chip_get_line(chip0, 19);        // P2.31
    QTR3 = gpiod_chip_get_line(chip0, 26);        // P1.20
    QTR4 = gpiod_chip_get_line(chip2, 27);        // P2.35
    gpiod_line_request_output(QTR3, "SensorRead", 0);
    gpiod_line_request_output(QTR4, "SensorRead", 0);
    //gpiod_line_request_output(QTR2, "a", 0);
    //gpiod_line_request_output(QTR5, "a", 0);
}

unsigned int readSensor(int delay) {
    if(count % 100)
        val = 0x00;
    int temp[4];
    gpiod_line_set_value(QTR3, 1);
    gpiod_line_set_value(QTR4, 1);
    
    // Charge the capacitors
    usleep(10);
    
    gpiod_line_release(QTR3);
    gpiod_line_release(QTR4);
    
    // Open switch line for input
    gpiod_line_request_input(QTR3, "a");
    gpiod_line_request_input(QTR4, "a");
    
    // Sleep for 1 msec
    usleep(delay);
    
    // Read input
    temp[1] = gpiod_line_get_value(QTR3);
    temp[2] = gpiod_line_get_value(QTR4);
    
    gpiod_line_release(QTR3);
    gpiod_line_release(QTR4);
    
    gpiod_line_request_output(QTR3, "a", 0);
    gpiod_line_request_output(QTR4, "a", 0);
    
    /*
    gpiod_line_set_value(QTR2, 1);
    gpiod_line_set_value(QTR5, 1);
    
    usleep(10);
    
    gpiod_line_release(QTR5);
    gpiod_line_release(QTR2);
    
    // Open switch line for input
    gpiod_line_request_input(QTR5, "a");
    gpiod_line_request_input(QTR2, "a");
    
    // Sleep for 1 msec
    usleep(delay);
    
    // Read input
    temp[3] = gpiod_line_get_value(QTR5);
    temp[0] = gpiod_line_get_value(QTR2);
    
    gpiod_line_release(QTR5);
    gpiod_line_release(QTR2);
    
    gpiod_line_request_output(QTR5, "a", 0);
    gpiod_line_request_output(QTR2, "a", 0);
    */
    for(unsigned int i = 0; i < 2; i++) {
        val |= temp[i]<<i;
    }
    count++;
    return val;
}

void release() {
    gpiod_line_release(QTR3);
    gpiod_line_release(QTR4);
    //gpiod_line_release(QTR5);
    //gpiod_line_release(QTR2);
    gpiod_chip_close(chip0);
    gpiod_chip_close(chip2);
}