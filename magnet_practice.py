import serial
import RPi.GPIO as GPIO
from datetime import datetime, date, time, timedelta
from time import sleep
import sys
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
hall = 18
GPIO.setup(hall, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def begin():
    print("Start running")

def checkClose(session, last_rev, count, start_time):
    current_time = datetime.now()
    if session == True and (current_time - last_rev > timedelta(seconds = 5)):
        session_running_time = (last_rev - start_time).total_seconds() / 60 ## IN MIN
        session_running_distance = count * 0.0004388 #  IN KM diameter of 13.97 cm, converted to circumference in km
        start_time = start_time
        end_time = last_rev
        session_average_pace = session_running_time / session_running_distance  ## MIN / KM
        revolutions = count
        print("Session ending")
        session_data = {
            "revolutions": revolutions,
            "start_time": start_time,
            "end_time": end_time,
            "mouseId": 1
            ##session_running_time: session_running_time,
            ##session_running_distance: session_running_distance,
            ##session_average_pace: session_average_pace
            }
        r=requests.post('https://d0693ddc.ngrok.io/hamster', data = session_data)
        print(r.text)
        print("Session started at {}".format(start_time))
        print("Session ended at {}".format(end_time))
        print("Total time spent running: {} minutes".format(session_running_time))
        print("Total running distance: {} km".format(session_running_distance))
        print("Average running pace: {} min/km".format(session_average_pace))
        ## print("revolut, session_revolutions)
        session = False
        last_rev = None
        count = 0
    return [session, last_rev, count]
    
def loop():
    session = False
    count=0
    last_rev = None
    start_time = None
    GPIO.add_event_detect(hall, GPIO.RISING)
    while True:

        if last_rev is not None:
            
            some_var = checkClose(session, last_rev, count, start_time)
            session = some_var[0]
            last_rev = some_var[1]
            count = some_var[2]
        if GPIO.event_detected(hall):
            if not session:
                session = True
                start_time = datetime.now()
                print("Session starting at {}".format(start_time))
            count += 1
            last_rev = datetime.now()
            print ("Animal has run {} revolutions".format(count))

def destroy():
    GPIO.cleanup()

if __name__=='__main__':
    begin()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
