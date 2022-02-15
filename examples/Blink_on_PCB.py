#!/usr/bin/python3


# This is a script to blink the PB onboard LEDs as well as those on the RSLK chassis
# while also displaying a message on an OLED display. The pins used for the display are
# the SDA and SCL designated I2C1 on the PB

import Adafruit_BBIO.GPIO as GPIO
import time

# Chassis LEDs
fl = "P2_29"
fr = "P1_6"
bl = "P1_12"
br = "P1_20"

# Onboard LEDs
board0 = "USR0"
board1 = "USR1"
board2 = "USR2"
board3 = "USR3"

# GPIOs used set to output
GPIO.setup(board0, GPIO.OUT)
GPIO.setup(board1, GPIO.OUT)
GPIO.setup(board2, GPIO.OUT)
GPIO.setup(board3, GPIO.OUT)
GPIO.setup(fl, GPIO.OUT)
GPIO.setup(fr, GPIO.OUT)
GPIO.setup(bl, GPIO.OUT)
GPIO.setup(br, GPIO.OUT)

# Put all LEDs in array to access them quicker
LEDs = [fl, fr, bl, br, board0, board1, board2, board3]

# Initialize all LEDs to off
for led in LEDs:
    GPIO.output(led, GPIO.LOW)
    

# Blink the LEDs one by one then blink all at once
for x in range(3):
    for led in LEDs:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(.5)
    for led in LEDs:
        GPIO.output(led, GPIO.LOW)
        time.sleep(.5)
    for i in range(3):
        for led in LEDs:
            GPIO.output(led, GPIO.HIGH)
        time.sleep(.25)
        for led in LEDs:
            GPIO.output(led, GPIO.LOW)
        time.sleep(.25)


# Cleanup
GPIO.cleanup()  # release all GPIO resources
