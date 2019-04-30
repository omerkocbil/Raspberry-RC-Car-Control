import os     #importing os library so as to communicate with the system   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod")
import time
import pigpio
import RPi.GPIO as IO 



pi = pigpio.pi()                      
IO.setwarnings(False)             
IO.setmode (IO.BOARD)
IO.setup(3,IO.OUT)           
p = IO.PWM(3,100)        
p.start(0)

def calis():
    p.ChangeDutyCycle(9)
    print "9"
    time.sleep(2)
    p.ChangeDutyCycle(11)
    print "11"
    time.sleep(2)
    p.ChangeDutyCycle(13)
    print "13"
    time.sleep(2)
    p.ChangeDutyCycle(15)
    print "15"
    time.sleep(2)
    p.ChangeDutyCycle(17)
    print "17"
    time.sleep(2)
    p.ChangeDutyCycle(19)
    print "19"
    time.sleep(2)
    

def dur():
    p.ChangeDutyCycle(0)




            
        
