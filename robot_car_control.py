import paho.mqtt.client as mq
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
pin1=31
pin2=33
pin3=11
pin4=13
gpio.setup(pin1,gpio.OUT)
gpio.setup(pin2,gpio.OUT)
gpio.setup(pin3,gpio.OUT)
gpio.setup(pin4,gpio.OUT)
c=mq.Client()
c.connect("iot.eclipse.org",1883)
def onc (c,userdata,flag,rc):
	print("connected to broker with rc",rc)
	c.subscribe("rpi/led")

def onm(c,userdata,msg):
	m=msg.payload.decode()
	print(m)
	if(m=='r'):
		gpio.output(pin1,1)
		gpio.output(pin2,0)
		gpio.output(pin3,1)
		gpio.output(pin4,0)
	elif(m=='f'):
		gpio.output(pin1,0)
		gpio.output(pin2,1)
		gpio.output(pin3,0)
		gpio.output(pin4,1)
	elif(m=='s'):
		gpio.output(pin1,0)
		gpio.output(pin2,0)
		gpio.output(pin3,0)
		gpio.output(pin4,0)
	elif(m=='w'):
		gpio.output(pin1,0)
		gpio.output(pin2,1)
		gpio.output(pin3,0)
		gpio.output(pin4,0)
	elif(m=='l'):
		gpio.output(pin1,0)
		gpio.output(pin2,0)
		gpio.output(pin3,0)
		gpio.output(pin4,1)
c.on_connect=onc
c.on_message=onm
c.loop_forever()
