from ctypes import *
from time import sleep
import time
import Motor_Functions as MOTORS
import Adafruit_BBIO.GPIO as GPIO
import bumpers as b

reverse = 0
sensor = CDLL("./bulk.so")
sensor.init()
leds = CDLL("./LEDs.so")
leds.init()
results = [0,0]
delayVal = 600
MOTORS.Motors_Init() #inits motors
print("Ready")
sleep(2)
startTime = time.time()
while ((time.time() - startTime) < 50): #run the whole simulation for 120 sec
    if reverse == 0: #if the robot is in the forward motion towards the book
        leds.turnOn()
        val = sensor.readSensor(delayVal)
        leds.turnOff()
        #if not (i % 25):
            #delayVal = delayVal + 25
        for x in range(2):
            results[x] = val>>x & 0x01
        if(sum(results) < 1):
            #print("White")
            MOTORS.Motors_Left_Stop()
            MOTORS.Motors_Right_Start(10, MOTORS.FORWARD)
        else:
            #print("Black")
            MOTORS.Motors_Right_Stop()
            MOTORS.Motors_Left_Start(10, MOTORS.FORWARD)
        #print(results, "\n\n")
        if ((GPIO.input(b.bumper_0) == 0) or (GPIO.input(b.bumper_1) == 0) or (GPIO.input(b.bumper_2) == 0) or (GPIO.input(b.bumper_3) == 0) or (GPIO.input(b.bumper_4) == 0) or (GPIO.input(b.bumper_5) == 0)): #any of the bumpers are presssed
            reverse = 1   
            MOTORS.Motors_Stop()
        sleep(0.1)
    else:
        MOTORS.Motors_Stop()
        sleep(1)
        reverseTime = time.time()
        while ((time.time() - reverseTime) < 3): #goes back for 20 sec
            leds.turnOn()
            val = sensor.readSensor(delayVal)
            leds.turnOff()
            #if not (i % 25):
                #delayVal = delayVal + 25
            for x in range(2):
                results[x] = val>>x & 0x01
            if(sum(results) < 1):
                #print("White")
                MOTORS.Motors_Left_Start(15, MOTORS.REVERSE)
                MOTORS.Motors_Right_Start(7, MOTORS.REVERSE)
            else:
                #print("Black")
                MOTORS.Motors_Right_Start(7, MOTORS.REVERSE)
                MOTORS.Motors_Left_Start(15, MOTORS.REVERSE)
            sleep(0.1)
            #print(results, "\n\n")
        MOTORS.Motors_Stop()
        reverse = 0    
        sleep(2)
        MOTORS.Motors_Left_Start(15, MOTORS.FORWARD) #rotates the robot about 180 degrees
        sleep(3)
        MOTORS.Motors_Stop()
        sleep(1)
        MOTORS.Motors_Right_Start(10, MOTORS.FORWARD) #robot starts to move straight
        MOTORS.Motors_Left_Start(10, MOTORS.FORWARD)
        leds.turnOn()
            #print("White")
        val = sensor.readSensor(delayVal)
        leds.turnOff()
            #if not (i % 25):
                #delayVal = delayVal + 25
        for x in range(2):
            results[x] = val>>x & 0x01
        while (sum(results) < 1): #while the robot is on white keep on going straight
            leds.turnOn()
            #print("White")
            val = sensor.readSensor(delayVal)
            leds.turnOff()
            #if not (i % 25):
                #delayVal = delayVal + 25
            for x in range(2):
                results[x] = val>>x & 0x01
            if(sum(results) < 1):
                print("White")
            else:
                print("Black")
        sleep(0.1)
        MOTORS.Motors_Stop() #once robot finds black line stop
        sleep(1)
        MOTORS.Motors_Left_Start(15, MOTORS.FORWARD) #again rotate the robot about 180 degrees, preffer overshoot of black line rather than undershoot
        MOTORS.Motors_Right_Start(15, MOTORS.REVERSE)
        sleep(1)
        MOTORS.Motors_Stop()
        sleep(1) #after this continues to follow blackline
            
        
        
    

sensor.release()
leds.turnOff()
leds.release()
MOTORS.Motors_Stop()
print("STOPPED")
MOTORS.Motors_Cleanup()
print("cleaned up")

print("All done")