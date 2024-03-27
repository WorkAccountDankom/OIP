import RPi.GPIO as GPIO

def decimal2binary(value):
     
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Введи число от 0 до 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, decimal2binary(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Текущее напрящение: {voltage:.4} вольт")
            else:
                print("Нормально введи")
        except Exception:
            if num == "q": break
            print("NAN")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")