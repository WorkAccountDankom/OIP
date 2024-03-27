import RPi.GPIO as GPIO
import time
from itertools import repeat
from random import randint

#dac = sorted(list(range(8)), key = lambda x: -x)
dac = [8, 11, 7, 1, 0, 5, 12, 6] #Норм порты

GPIO.setmode(GPIO.BCM)

number = list(repeat(0, len(dac)))

GPIO.setup(dac, GPIO.OUT)

for i in range(len(number)):
    number[i] = randint(0, 1)


number = [0, 0, 0, 0, 0, 0, 0, 0] #0

GPIO.output(dac, number)
time.sleep(20)
GPIO.output(dac, 0)
GPIO.cleanup()

number = [0, 0, 0, 0, 0, 0, 1, 0] #2
number = [1, 1, 1, 1, 1, 1, 1, 1] #255
number = [0, 1, 1, 1, 1, 1, 1, 1] #127
number = [0, 0, 1, 0, 0, 0, 0, 0] #64
number = [0, 0, 0, 1, 0, 0, 0, 0] #32
number = [0, 0, 0, 0, 0, 1, 0, 1] #5
number = [0, 0, 0, 0, 0, 0, 0, 0] #0

