import RPi.GPIO as GPIO
import time


#leds = sorted(list(range(8)), key = lambda x: -x)
leds = [2, 3, 4, 17, 27, 22, 10, 9] #норм порты

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

for j in range(3):
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(20 / 100)
        GPIO.output(i, 0)

GPIO.output(leds, 0)

GPIO.cleanup()