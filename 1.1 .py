import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
while True:
    time.sleep(5)
    GPIO.output(16,GPIO.input(24))
    time.sleep(5)




