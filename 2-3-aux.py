import RPi.GPIO as GPIO
import time

#leds = sorted(list(range(8)), key = lambda x: -x)
#aux = sorted(list(range(8)), key = lambda x: -x)

leds = [2, 3, 4, 17, 27, 22, 10, 9] #норм порты
aux = [21, 20, 16, 12, 7, 8, 25, 24] #Норм порты

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    for i in range(8):
        #print(7 ,GPIO.input(aux[7]))
        GPIO.output(leds[i], GPIO.input(aux[i]))
