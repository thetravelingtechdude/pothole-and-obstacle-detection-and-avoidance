import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
pin1=31
pin2=33
pin3=11
pin4=13
print "Distance Measurement In Progress"
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
        GPIO.output(TRIG, False)
        print "Waiting For Sensor To Settle"
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
                pulse_start = time.time()

        while GPIO.input(ECHO)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
        if(distance>25):
                        GPIO.output(pin1,0)
                        GPIO.output(pin2,0)
                        GPIO.output(pin3,0)
                        GPIO.output(pin4,0)

        print "Distance:",distance,"cm"

       
