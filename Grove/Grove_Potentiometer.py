import time
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM

led = "P1_36"
duty = 0
ADC.setup()
inputPin  = "AIN2"  # J7
PWM.start(led, duty)



while True:
    value = ADC.read(inputPin)
    #print(value)
    duty = value * 100
    PWM.set_duty_cycle(led, int(duty))
    time.sleep(0.2)