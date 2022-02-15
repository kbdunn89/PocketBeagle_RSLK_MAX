#!/usr/bin/python

'''
Alpha demo motor and encoder demo

This program sets the motors to a desired speed, then lets the PID
controller bring the motors to the desired speed. Then after running
for a certian distance, it stops the motors, turns the robot around
180 degrees and sets motor to same speed and travels to 
original spot
''' 

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import Motor_Functions as MOTORS
import AlphaDemo_MotorsAndEncoders_PID as PID
#import AlphaDemo_180_Degree_Turn as TURN

print("Starting program")
time.sleep(3)
MOTORS.Motors_Init() #inits motors
print("motors inited")
#time.sleep(3)
PID.runPID(30)
time.sleep(2)
MOTORS.Motors_Left_Start(20, MOTORS.FORWARD)
time.sleep(2.92)
MOTORS.Motors_Left_Stop()
time.sleep(2)
PID.runPID(30)
#time.sleep(1)
#TURN.travel180(20)
MOTORS.Motors_Cleanup()
print("Demo Done")