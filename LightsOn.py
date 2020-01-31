import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup (22, gpio.OUT)
gpio.setup (27, gpio.OUT)
gpio.setup (23, gpio.OUT)
gpio.setup (24, gpio.OUT)

#while True:
     #set all pins low
gpio.output(22, gpio.LOW)
gpio.output(27, gpio.LOW)
gpio.output(23, gpio.LOW)
gpio.output(24, gpio.LOW)

     #Turn on Lights
gpio.output(23, gpio.HIGH)
gpio.output(24, gpio.HIGH)
print ("Lights On")
time.sleep(10)
