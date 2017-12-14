import serial
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

ser = serial.Serial('/dev/serial0', 9600)

ser.flushInput()

Animal1 = 25774879505
Animal2 = 2015060149

while True:
	junk1 = ser.read(1)
	rawtag = ser.read(10)
	tag=int(rawtag, 16)
	junk2 = ser.read(5)

	if len(junk1) == 0:
		print "Please insert tag"
		
	elif tag==Animal1:
		Animal1_file=open("Animal 1real.txt","a")
		print "Animal 1 is running"

		try:
			while True:		

				is_HES_off=GPIO.input(HES)
				GPIO.wait_for_edge(18, GPIO.BOTH)

				#  magnet present
				if is_HES_off==True:
					now = datetime.datetime.now()
					print "Animal 1 has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S"))
					Animal1_file.write("Animal 1 has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S")))
					Animal1_file.write ('\n')
					count+=1
					distance=distance+circumference
					LED_status=True

				# no magnet present
				else:
					LED_status=False
			    		GPIO.output(LED,LED_status)
	elif tag==Animal2:
		Animal1_file=open("Animal 2real.txt","a")
		print "Animal 2 is running"

		try:
			while True:		

				is_HES_off=GPIO.input(HES)
				GPIO.wait_for_edge(18, GPIO.BOTH)

				#  magnet present
				if is_HES_off==True:
					now = datetime.datetime.now()
					print "Animal 1 has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S"))
					Animal1_file.write("Animal 1 has run %d rotations and %f meters as of %s" % (count, distance, now.strftime("%Y-%m-%d %H:%M:%S")))
					Animal1_file.write ('\n')
					count+=1
					distance=distance+circumference
					LED_status=True

				# no magnet present
				else:
					LED_status=False
			    		GPIO.output(LED,LED_status)		    		
