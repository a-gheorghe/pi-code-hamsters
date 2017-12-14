import RPi.GPIO as GPIO
import serial


ser = serial.Serial('/dev/serial0', 9600)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
rfid = 22
GPIO.setup(rfid, GPIO.IN)

##ser.reset_input_buffer()

reading = False

while True:
        
        if (reading == False and GPIO.input(rfid)):
                reading = True
                junk1 = ser.read(1)
                rawtag = ser.read(10)
                tag= int(rawtag, 16)
                junk2 = ser.read(5)
                
                
                print('The RFID tag is ', tag)
        elif (GPIO.input(rfid) == 0 and reading == True):
                print('pin leaves')
                reading = False

####
##        if len(tag) == 0:
##                print ("Please insert tag")
##                continue
##        else:
##                print(tag)
##                ser.reset_input_buffer()

##                
##	elif tag==Animal1:
##		print "Animal 1 is running"
##		Animal1_file=open("Animal 1real.txt", "a")
##		Animal1_file.write("YAY ANIMAL 1")
##		Animal1_file.write ('\n')
##
##        elif tag==Animal2:
##		print "Animal 2 is running"
##		Animal2_file=open("Animal 2.txt", "a")
##		Animal2_file.write("WOOT ANIMAL 2")
##		Animal2_file.write ('\n')
##
##                
##	ser.flushInput()




