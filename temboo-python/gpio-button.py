import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 14
button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led, 1)

time.sleep(2)

GPIO.output(led, 0)

while True:
    if GPIO.input(button) == False:
        print("Button pressed")
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)

GPIO.cleanup()
