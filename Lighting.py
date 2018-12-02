import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

while True:
    try:
        GPIO.setup(18, GPIO.OUT)

        GPIO.output(18, False)
        time.sleep(20)

        GPIO.output(18, True)
        time.sleep(20)

        if time.strftime("%H-%M-%S") > "14-10-00":  # if time is later than 14:10:00, set the pin 23 as False (on)
            GPIO.setup(23, GPIO.OUT)
            GPIO.output(23, False)

        if time.strftime("%H-%M-%S") > "14-13-00":  # if time is later than 14:12:00, set the pin 23 as True(off)
            GPIO.output(23, True)
            
    except KeyboardInterrupt:
        break