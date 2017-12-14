## Use this to scan animal initially
## need rfid as id
## sex as 'M' or 'F'
## age opt (weeks)
## notes opt
## cageId (1-22)

import RPi.GPIO as GPIO
import serial
import requests

ser = serial.Serial('/dev/serial0', 9600)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
rfid = 22
GPIO.setup(rfid, GPIO.IN)

RFID = str(input("Scan animal (press enter when done)"))
junk1 = ser.read(1)
rawtag = ser.read(10)
tag = int(rawtag, 16)
junk2 = ser.read(5)
print(tag)

Sex = str(input("Sex of animal (M or F):"))
Age = int(input("Age of animal (in weeks):"))
Notes = str(input("Optional notes on animal:"))
CageId = int(input("Cage Id (1-22):"))

input_data = {
    "sex": Sex,
    "age": Age,
    "notes": Notes,
    "cageId": CageId,
    "id": tag
    }

r = requests.post('https://24a46cb5.ngrok.io/new/mouse', data = input_data)
print(r.text)
        
