#!/usr/bin/env python
from __future__ import print_function
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

#RASPBERRYPI RIGHT WHEEL PINS
DIR_PIN_RIGHT = 19
STEP_PIN_RIGHT = 26

#RASBERYPI LEFT WHEEL PINS
DIR_PIN_LEFT = 20
STEP_PIN_LEFT = 21 

#SETUP PINS
GPIO.setup(DIR_PIN_RIGHT, GPIO.OUT)
GPIO.setup(STEP_PIN_RIGHT, GPIO.OUT)

GPIO.setup(DIR_PIN_LEFT, GPIO.OUT)
GPIO.setup(STEP_PIN_LEFT, GPIO.OUT)


def direction(value = 0):
    d =[]
    # forward True, backward False
    if value in ("forward","f",0):
        d = [False, True]
    elif value in ("backwords","b",1):
        d = [True, False]
    elif value in ("left","l",2):
        d = [False, False]
    elif value in ("right", "r", 3) :
        d = [True, True]

    GPIO.output(DIR_PIN_RIGHT, d[0])
    GPIO.output(DIR_PIN_LEFT,  d[1])
    
for arg in sys.argv:
    print(arg)
    direction(value=arg[0])

while True:
     direction(value=arg[0])
     GPIO.output(STEP_PIN_RIGHT, True)
     GPIO.output(STEP_PIN_LEFT, True)
     time.sleep(0.0001)
     GPIO.output(STEP_PIN_RIGHT, False)
     GPIO.output(STEP_PIN_LEFT, False)
     time.sleep(0.0001)
