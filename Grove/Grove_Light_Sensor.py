#!/usr/bin/python
# This file is used to test the grove - light sensor and sound sensor
# We are using one of the analog grove port
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

ADC.setup()
inputPin  = "AIN2"  # J7

while True:
    value = ADC.read(inputPin)
    print(((value - 0.47)/0.53) * 100)  # Normalize the output to fall between 0-100
    time.sleep(1)