import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12,200)

pwm.start(0)

chords = [246,0,246,0,246,0,61,0,98,0,98,0,98,0,61,0,246,0,246,0,246,0,61,0,98,0,246,0,493]

#EADGBE

try:
    for note in chords:
        if note == 0:
            pwm.ChangeDutyCycle(1)
            time.sleep(0.2)
        else:
            pwm.ChangeFrequency(note)
            pwm.ChangeDutyCycle(20)
            time.sleep(0.6)
            print(note)
finally:
    if pwm is not None:
        pwm.stop()
    GPIO.cleanup()
