import RPi.GPIO as GPIO
import time
import requests

LedPin = 18

def setup():
    print('setup1')
    GPIO.setmode(GPIO.BOARD)
    print('setup2')
    GPIO.setup(LedPin, GPIO.OUT)
    print('setup3')
    GPIO.output(LedPin, True)
    print('setup4')


def loop():
    while True:
        if GPIO.input(LedPin):
            print ('LED on')
            r=requests.get('https://04501e5b.ngrok.io/led')
            print('request',r)
            print('request.text', r.text)
            time.sleep(1)
            GPIO.output(LedPin, False)
        elif not GPIO.input(LedPin):
            print ('LED off')
            session = {'me': 'ana', 'you':'brock'}
            r=requests.post('https://04501e5b.ngrok.io/hamster', data=session)
            print('r', r)
            print('r.text', r.text)
            time.sleep(1)
            GPIO.output(LedPin, True)
##          GPIO.output(LedPin, GPIO.LOW)
##          time.sleep(1)
##          print('LED on')
##          GPIO.output(LedPin, GPIO.HIGH)
##          time.sleep(1)

def destroy():
    print('destroyhere')
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
