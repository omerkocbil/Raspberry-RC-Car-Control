import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
pwm = GPIO.PWM(5, 50) #GPIO pin:2 , 50Hz : period of the signal 1/50=0.2 seconds or 20 milliseconds    
pwm.start(5)

def set_angle(aci):    
    pwm.ChangeDutyCycle(aci)
    sleep(1)

def kapat():
    pwm.stop()
    GPIO.cleanup()



