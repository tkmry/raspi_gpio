#!/usr/bin/env python
# -*- coding: utf-8 -*-

# base code on
#    http://developersnote.jp/knowhow/raspberry-pi-zero-kawaii-yo.html

import RPi.GPIO as GPIO
import time

led_port = 16
t = 0.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_port, GPIO.OUT)

try:
        while True:
                GPIO.output(led_port, True)
                time.sleep(t)

                GPIO.output(led_port, False)
                time.sleep(t)

except KeyboardInterrupt:
        pass

GPIO.cleanup()

