import RPi.GPIO as GPIO
from time import sleep

def dec2bin(value):
     
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


flag = 1
t = 0 
x = 0

try:
    try:
        period = float(input("Введи период сигнала: "))
        while True:
            GPIO.output(dac, dec2bin(x))

            if   x == 0:    
                flag = 1
            elif x == 255:  
                flag = 0

            if flag == 1:
                x = x + 1  
            else: 
                x = x - 1

            sleep(period/256/2)
            print("время: ", t," напряжение: ", x/255*3.3)
            t = t + 1
    except Exception:
        print("Нормально введи")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")