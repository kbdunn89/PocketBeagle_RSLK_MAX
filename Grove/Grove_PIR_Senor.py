import time
import Adafruit_BBIO.GPIO as GPIO

pin = "P1_8"
leds = ["P2_27", "P1_31", "P1_36", "P2_17", "USR0", "USR1", "USR2", "USR3"]
def trig(arg):
    global state
    state = True
    for led in leds:
            GPIO.output(led, GPIO.HIGH)
    print("Motion Detected")
    
def main():
    import sys
    GPIO.setup(pin, GPIO.IN)
    global state
    state = False
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        
    GPIO.add_event_detect(pin, GPIO.RISING, callback = trig)
    
    while True:
        time.sleep(3)
        print(state)
        if state:
            state = False
            for led in leds:
                GPIO.output(led, GPIO.LOW)
 
 
if __name__ == '__main__':
    main()