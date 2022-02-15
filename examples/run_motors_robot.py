#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import Motor_Functions as MOTORS

print("test started")
#time.sleep(3)
MOTORS.Motors_Init() #inits motors
print("motors inited")
time.sleep(3)
MOTORS.Motors_Start(20, MOTORS.REVERSE, 20, MOTORS.FORWARD)
print("both started")
time.sleep(3)
MOTORS.Motors_Left_Stop()
print("left stopped")
time.sleep(3)
MOTORS.Motors_Right_Stop()
print("left stopped")
time.sleep(3)
MOTORS.Motors_Left_Start(50, MOTORS.FORWARD)
print("left STARTED")
time.sleep(3)
MOTORS.Motors_Right_Start(70, MOTORS.REVERSE)
print("right STARTED")
time.sleep(3)
MOTORS.Motors_Stop()
print("STOPPED")
MOTORS.Motors_Cleanup()
print("cleaned up")