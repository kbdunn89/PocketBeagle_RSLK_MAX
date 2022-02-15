#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import Motor_Functions as MOTORS

print("test started")
time.sleep(3)
MOTORS.Motors_Init() #inits motors
print("motors inited")
time.sleep(3)
MOTORS.Motors_Start(50, MOTORS.FORWARD, 50, MOTORS.FORWARD)
print("motors started")
time.sleep(2)
MOTORS.Motors_Start(20, MOTORS.REVERSE, 90, MOTORS.FORWARD)
print("motors started")
time.sleep(2)
MOTORS.Motors_Stop()
print("motors stopped")
time.sleep(2)
MOTORS.Motors_Left_Start(80, MOTORS.FORWARD)
print("left started")
time.sleep(2)
MOTORS.Motors_Right_Start(50, MOTORS.REVERSE)
print("right started")
time.sleep(2)
MOTORS.Motors_Left_Stop()
print("left stopped")
time.sleep(2)
MOTORS.Motors_Right_Stop()
print("right stopped")
time.sleep(2)
MOTORS.Motors_Stop()
print("motors stopped")
#i = 3

"""
while i != 0:
    MOTORS.Motors_Start(50, MOTORS.FORWARD, 50, MOTORS.FORWARD) #everything changed
    time.sleep(3)
    MOTORS.Motors_Stop() #check to see slp and PWM changed
    time.sleep(3)
    MOTORS.Motors_Start(80, MOTORS.REVERSE, 80, MOTORS.REVERSE) #everything changed
    time.sleep(3)
    MOTORS.Motors_Stop()  #check to see slp and PWM changed
    time.sleep(3)
    i = i-1
    print(i)
"""

#print("test dun")

MOTORS.Motors_Cleanup()
print("cleaned up")



