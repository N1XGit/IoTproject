import RPi.GPIO as GPIO
import time

# Set up GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
# Set up PWM on the pin
pwm = GPIO.PWM(12,2000)  # 1 kHz frequency

pwm.start(0) 

chords = [300, 600, 800, 1000, 1500, 1800, 2300]
    # Play sound (DO, RE, MI, etc.), pausing for 0.5 seconds between notes
try:
	for note in chords:
		pwm.ChangeFrequency(note)
		pwm.ChangeDutyCycle(20)
		time.sleep(0.5) 
		print(note)	

finally:
	if pwm is not None:
		pwm.stop()
	GPIO.cleanup()