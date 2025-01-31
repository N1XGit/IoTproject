import rPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PVM(12,200)

pwm.start(0)

chords = [246,246,246,61,98,98,98,61,246,246,246,61,98,246,493]

#EADGBE

try:
    for note in chords:
        pwm.ChangeFrequency(note)
        pwm.ChangeDutyCycle(20)
        time.sleep(0.4)
        print(note)
finally:
    if pwm is not None:
        pwm.stop()
    GPIO.cleanup()