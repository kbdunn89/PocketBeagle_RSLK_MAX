#!/usr/bin/python3


# This is a script to blink the PB onboard LEDs as well as those on the RSLK chassis
# while also displaying a message on an OLED display. The pins used for the display are
# the SDA and SCL designated I2C1 on the PB

import Adafruit_BBIO.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import Adafruit_BBIO.GPIO as GPIO

display = Adafruit_SSD1306.SSD1306_128_64(rst=None)

# Chassis LEDs
fl = "P2_2"
fr = "P2_4"
bl = "P2_6"
br = "P2_8"

# Onboard LEDs
board0 = "USR0"
board1 = "USR1"
board2 = "USR2"
board3 = "USR3"

# GPIOs used set to output
GPIO.setup(board0, GPIO.OUT)
GPIO.setup(board1, GPIO.OUT)
GPIO.setup(board2, GPIO.OUT)
GPIO.setup(board3, GPIO.OUT)
GPIO.setup(fl, GPIO.OUT)
GPIO.setup(fr, GPIO.OUT)
GPIO.setup(bl, GPIO.OUT)
GPIO.setup(br, GPIO.OUT)

# Put all LEDs in array to access them quicker
LEDs = [fl, fr, bl, br, board0, board1, board2, board3]

# Initialize all LEDs to off
for led in LEDs:
    GPIO.output(led, GPIO.LOW)
    
# Set up SSD1306 OLED display
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.load_default()  # load and set default font
# Draw text
draw.text((0,0), "BeagleBoiz:\nThis is a demo\nof the PocketBeagle\nGPIO functionality", fill=255)
# Display to screen
display.image(image)  # set display buffer with image buffer
display.display()  # write display buffer to physical display

# Blink the LEDs one by one then blink all at once
for x in range(3):
    for led in LEDs:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(.5)
    for led in LEDs:
        GPIO.output(led, GPIO.LOW)
        time.sleep(.5)
    for i in range(3):
        for led in LEDs:
            GPIO.output(led, GPIO.HIGH)
        time.sleep(.25)
        for led in LEDs:
            GPIO.output(led, GPIO.LOW)
        time.sleep(.25)

# Display second message
image = Image.new('1', (displayWidth, displayHeight))
draw = ImageDraw.Draw(image)
display.clear()
display.display()
draw.text((0,0), "I hope you\nenjoyed it!", fill=255)
display.image(image)
display.display()

# Cleanup
GPIO.cleanup()  # release all GPIO resources
