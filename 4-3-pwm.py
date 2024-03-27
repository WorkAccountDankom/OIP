import RPi.GPIO as GPIO

def dec2bin(value):
     
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

#dac = [8, 11, 7, 1, 0, 5, 12, 6, 2, 3]
#dac = [2, 3]
outpin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(outpin, GPIO.OUT)

p = GPIO.PWM(outpin, 1000)
p.start(0)

try:
    while True:
        f = int(input("Введи от 0 до 100:"))
        p.ChangeDutyCycle(f)
        print("Напряжение: ",3.3*f/100)

finally:
    p.stop()
    GPIO.output(outpin,0)
    GPIO.cleanup()