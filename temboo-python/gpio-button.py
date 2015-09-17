import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Components are plugged into these digital pins
led = 14
button = 15

# Tell the Pi the LED is an output, and the button is an input using the built-in pullup resistor
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

# Turn the LED on for 2 seconds, then off again
GPIO.output(led, 1)
time.sleep(2)
GPIO.output(led, 0)

# Wait around to see if the button is pressed. If so, blink LED
while True:
    if GPIO.input(button) == False:
        print("Button pressed")
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)

# Clean up your mess
GPIO.cleanup()
