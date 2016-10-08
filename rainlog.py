#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler("log",
                                       when="midnight",
                                       interval=1,
                                       backupCount=30)
logger.addHandler(handler)


pin = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)


output = ""
def bucket_tipped(channel):
    global output
    timestamp = str(long((time.time() + 0.5) * 1000)) 
    output = output +  timestamp + ","

print "Logging started"
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=100)
while True:
    logger.info(output)
    output = ""
    time.sleep(1800)

GPIO.cleanup()
print "Logging stopped"

