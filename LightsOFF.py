import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup (22, gpio.OUT)
gpio.setup (27, gpio.OUT)
gpio.setup (23, gpio.OUT)
gpio.setup (24, gpio.OUT)

     #Turn off Lights
gpio.output(23, gpio.LOW)
gpio.output(24, gpio.LOW)
print ("Lights OFF")
time.sleep(10)
