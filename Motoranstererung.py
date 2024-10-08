#!/usr/bin/env python
#coding: utf8

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Ein und Ausgänge festlegen
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Ausgang K02
if GPIO.input(11, GPIO.HIGH): GPIO.output(18, GPIO.HIGH)
else  : GPIO.output(16, GPIO.LOW)
    
# Ausgang K03
if GPIO.input(13, GPIO.HIGH): GPIO.output(18, GPIO.HIGH)
else : GPIO.output(18, GPIO.LOW)
    
# Ausgänge wieder freigeben
GPIO.cleanup()