## read tag, store tag in a variable
## count revolutions
## on first revolution, get start_time, store in a variable
## once revolutions stop for 5 sec OR new tag:
## get end_time, store in a variable
## send post request to server where
## session: {
##                animal: RFID number,
##                start_time: start_time
##                end_time: end_time
##                revolutions: revolutions
##                distance: revolutions * circumference
##                speed: distance / (end_time-start_time)
##            }

## This file is run when wanting to initialize animals.
## Only prints RFID to screen.

# must pip install pyserial before can import serial
## or python3 setup.py install

import RPi.GPIO as GPIO
import requests
import serial

LED = 7
HALL = 18
led_status = False
hall_status = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    GPIO.setup(HALL, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)
    
    GPIO.output(LED, led_status)

    ## open a serial port Serial(port, baudrate)
    ## issues between Pi 2 and 3, try port '/dev/ttyAMA0' or '/dev/ttyS0'
    ## may have config issues, look online if so
    ser = serial.Serial('/dev/serial0', 9600)
    ser.flushInput()
    

def loop():
    while True:
        ser.flushInput() ## here
        junk1 = ser.read(1)
        raw_tag = ser.read(10)
        tag = int(raw_tag, 16) ## convert from hexadecimal string to integer using base 16
        junk2 = ser.read(5)

        if len(junk1) == 0:
            led_status = False
            print("Scan animal")
        elif:
            led_status = True
            print("Animal RFID number is: " raw_tag)
            ser.flushInput() ## or here

            

def destroy():
    GPIO.output(LED, False)
    ser.close()
    GPIO.cleanup()

if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
