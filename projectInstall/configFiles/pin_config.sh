#!/bin/sh -e

# motor pins
config-pin p1.06 gpio # DIRR	gpio0_5
config-pin p1.32 gpio # DIRL 	gpio1_10
config-pin p2.10 gpio # nSLPL	gpio1_20
config-pin p2.02 gpio # nSLPR	gpio1_27
config-pin p2.01 pwm  # PWMR	good
config-pin p2.03 pwm  # PWML	good

# motor encoder pins
config-pin p2.08 gpio # ERA		good
config-pin p2.29 gpio # ELA		good

# LED pins
config-pin p2.27 gpio # LEDBR	gpio1_8
config-pin p1.31 gpio # LEDBL	gpio3_18
config-pin p1.36 gpio # LEDFR	gpio3_14
config-pin p2.17 gpio # LEDFL	gpio2_1

# bumper pins
config-pin p1.12 gpio # BMP0	gpio0_4
config-pin p1.02 gpio # BMP1	gpio2_23
config-pin p1.29 gpio # BMP2	gpio3_21
config-pin p1.33 gpio # BMP3	gpio3_15
config-pin p1.30 gpio # BMP4	gpio1_11
config-pin p1.35 gpio # BMP5	gpio2_24

# misc
config-pin p2.20 gpio # RST		gpio2_0

# IR sensors
config-pin p2.04 gpio # CTRLE	gpio1_26
config-pin p2.06 gpio # CTRLO	gpio1_25
config-pin p1.20 gpio # QTR1	gpio0_20
config-pin p2.33 gpio # QTR2	gpio1_13
config-pin p1.34 gpio # QTR3	gpio0_26
config-pin p2.19 gpio # QTR4	gpio0_27
config-pin p2.24 gpio # QTR5	gpio1_12
config-pin p2.22 gpio # QTR6	gpio1_14
config-pin p2.18 gpio # QTR7	gpio1_15

# Grove
config-pin p1.28 gpio # Buzzer 
config-pin p1.08 gpio # Distance



# I'm pretty sure Ain, UART, and I2C are already properly configured

exit 0
