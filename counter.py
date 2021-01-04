#!/usr/bin/env python2.7  
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3  

import sys
from time import gmtime, strftime
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 set up as inputs, pulled up to avoid false detection.  
# the ports are wired to connect to GND on button press.  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

count = 0
while True:
    try:  
        GPIO.wait_for_edge(23, GPIO.FALLING)  
        count += 1
        print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": count={}".format(count)
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
        Break
