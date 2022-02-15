#!/usr/bin/python3


# This is a script to blink the PB onboard LEDs as well as those on the RSLK chassis
# while also displaying a message on an OLED display. The pins used for the display are
# the SDA and SCL designated I2C1 on the PB

import Adafruit_BBIO.GPIO as GPIO
import time

# Chassis LEDs
fl = "P2_17"
fr = "P1_36"
bl = "P1_31"
br = "P2_27"

# Onboard LEDs
board0 = "USR0"
board1 = "USR1"
board2 = "USR2"
board3 = "USR3"

# Put all LEDs in array to access them quicker
LEDs = [fl, fr, bl, br, board0, board1, board2, board3]
LEDstats = [0, 0, 0, 0, 0, 0]

#initialize LEDs
def init():
    for pin in LEDs:
        # GPIOs used set to output
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for stat in LEDstats:
        stat = 0
#turn all LEDs off
def all_off():
    # Initialize all LEDs to off
    for led in LEDs:
        GPIO.output(led, GPIO.LOW)
    for stat in LEDstats:
        stat = 0

#turn all LEDs on
def all_on():
    # Initialize all LEDs to off
    for led in LEDs:
        GPIO.output(led, GPIO.HIGH)
    for stat in LEDstats:
        stat = 1

#toggle single LED state
def switch(bump):
    val = LEDstats[bump]
    if val:
        GPIO.output(LEDs[bump], GPIO.LOW)
    else:
        GPIO.output(LEDs[bump], GPIO.HIGH)
    LEDstats[bump] = not val
        
#release GPIOs
def cleanup():
    for led in LEDs:
        GPIO.cleanup(led)
