#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime as datetime
from time import sleep
import sys
import math

now = datetime.datetime.now()

GPIO.setmode(GPIO.BOARD)
HES=18
is_HES_off=False
LED=7
LED_status=False

diameter=0.01397 # diameter in meters 
circumference=math.pi*diameter
distance=circumference
count=1

GPIO.setwarnings(False)

GPIO.setup(HES,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,LED_status)
file=open("Animal 1.txt", "a")

while True:
	try:
		is_HES_off=GPIO.input(HES)
		GPIO.wait_for_edge(18, GPIO.BOTH)
	
		#  magnet present
		if is_HES_off==True:
			now = datetime.datetime.now()
			print "Animal __ has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S"))
			file.write("Animal __ has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S")))
			file.write ('\n')
			count+=1
			distance=distance+circumference
			LED_status=True
			
		# no magnet present
		else: 
			LED_status=False
		
		GPIO.output(LED,LED_status)

	except KeyboardInterrupt:
		GPIO.output(LED, False)
		sys.exit()
		file.close()

GPIO.cleanup()
