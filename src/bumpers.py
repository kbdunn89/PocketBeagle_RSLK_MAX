#!/usr/bin/python
#This file contains a complete setup for the bumpers.
#So that the Pocket Beagle can receive signals from the bumpers.

import Adafruit_BBIO.GPIO as GPIO
import time

#Define pins
bumper_0 = "P1_12"
bumper_1 = "P1_2"
bumper_2 = "P1_29"
bumper_3 = "P1_33"
bumper_4 = "P1_30"
bumper_5 = "P1_35"

#pins put into an array for easier mass operations using for each loop
bumpers = [bumper_0, bumper_1, bumper_2, bumper_3, bumper_4, bumper_5]

#Set GPIOs as input and enable pull-up resistors
for pin in bumpers:
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)