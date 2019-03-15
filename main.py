import RPi.GPIO as GPIO
import time
import os

buttonPIR = 17
buttonPush = 27
kek = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPIR,GPIO.IN)
GPIO.setup(buttonPush,GPIO.IN)
GPIO.setup(kek,GPIO.OUT)

GPIO.output(kek,1)
time.sleep(2)  
while True:
	i = GPIO.input(buttonPush)
	j = GPIO.input(buttonPIR)
	if (j == 1):
        	print("Intruder detected.") 
		time.sleep(2)  
		os.system("python /home/pi/my_project/pir.py")
	if (i == 1):
        	print("Button pressed.") 
		time.sleep(2)
        	os.system("python /home/pi/my_project/push.py")
	


