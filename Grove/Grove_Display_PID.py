#!/usr/bin/python3
import Grove_4_Digit_Display as Display
import time
import motorPID as PID
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Motor_Functions as MOTORS
import bumpers as b

#Left motor config        
GPIO.setup(PID.inPin1, GPIO.IN)
GPIO.add_event_detect(PID.inPin1, GPIO.RISING, callback = PID.risingEdge1)

#Right motor config
GPIO.setup(PID.inPin2, GPIO.IN)
GPIO.add_event_detect(PID.inPin2, GPIO.RISING, callback = PID.risingEdge2) 

# Declare the display as an object
display = Display.Grove4DigitDisplay()

print("test started")
MOTORS.Motors_Init() #inits motors
print("motors inited")
time.sleep(1.5)

while True:
    PID.calculateRPM()
    print("RPM:", "{:.2f}".format(PID.rpm1))
    # Set brightness 0-7 (Default is 2)
    display.set_brightness(3)
    display.show(int(PID.rpm1))
    
    #Stop Motors for safety
    MOTORS.Motors_Stop()
    time.sleep(0.0001)
    if GPIO.input(b.bumper_0) == 0:
        print("Bump 0 is pressed")
        MOTORS.Motors_Start(40, MOTORS.FORWARD, 40, MOTORS.FORWARD)
        
    elif GPIO.input(b.bumper_1) == 0:
        print("Bump 1 is pressed")
        MOTORS.Motors_Start(60, MOTORS.FORWARD, 60, MOTORS.FORWARD)
        
    elif GPIO.input(b.bumper_2) == 0:
        print("Bump 2 is pressed")
        MOTORS.Motors_Start(80, MOTORS.FORWARD, 80, MOTORS.FORWARD)
        
    elif GPIO.input(b.bumper_3) == 0: 
        print("Bump 3 is pressed")
        MOTORS.Motors_Start(40, MOTORS.REVERSE, 40, MOTORS.REVERSE)
        
    elif GPIO.input(b.bumper_4) == 0: 
        print("Bump 4 is pressed")
        MOTORS.Motors_Start(60, MOTORS.REVERSE, 60, MOTORS.REVERSE)
        
    elif GPIO.input(b.bumper_5) == 0:   
        print("Bump 5 is pressed")
        MOTORS.Motors_Start(80, MOTORS.REVERSE, 80, MOTORS.REVERSE)
    time.sleep(0.5)