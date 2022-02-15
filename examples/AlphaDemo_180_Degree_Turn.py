#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
import Motor_Functions as MOTORS

test = "P1_20" #Left motor tachometer read

slots = 0
done = 0

def countPulses(arg):
	global slots
	global done
	
	slots = slots + 1
	if (slots >= 745):
		done = 1
		
		
#Left motor config        
GPIO.setup(test, GPIO.IN)
GPIO.add_event_detect(test, GPIO.RISING, callback = countPulses)	
		
def travel180(setPWM):
	global slots
	global done
	MOTORS.Motors_Left_Start(setPWM, MOTORS.FORWARD)
	slots = 0
	done = 0
	while(done == 0):
		pass
	MOTORS.Motors_Left_Stop()
	GPIO.cleanup()
	GPIO.remove_event_detect(test)