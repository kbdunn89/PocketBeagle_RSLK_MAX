#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
from ctypes import *

sensor = CDLL("./test.so")
sensor.init()
sensor.argtype = None
sensor.MeasureInInches.restype = c_float
count = 0
while True:
    if GPIO.input(reset) == 0:
        sensor.release()
        break
    time.sleep(1)
    d = sensor.MeasureInInches()
    print("Distance is: ", "{:.3f}".format(d), "in")