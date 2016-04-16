#!/usr/bin/env python

# Clock for 4 8x8 LED matrices.

import time
import datetime
import socket
import threading
import RPi.GPIO as GPIO  
import max7219.led as led
from max7219.font import proportional, LCD_FONT
from random import randrange

GPIO.setmode(GPIO.BCM)  

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Clock
  def __init__(self):
    self.device = led.matrix(cascaded=4)
    self.device.brightness(2)
    
  def run(self):
    self.device.scrollMessage("Clock 1.2 ", font=proportional(LCD_FONT))
    self.device.scrollMessage(get_ip_address(), font=proportional(LCD_FONT))
    time.sleep(5)
    self.device.brightness(0)
    while 1:
      str = datetime.datetime.now().strftime('%H:%M  ')
      self.device.displayMessage(str, font=proportional(LCD_FONT), delay=0.06)
      time.sleep(10)


class DisplayTimeThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = False

  def run(self):
    self.running = True
    #self.ledStrip.bar2(self.color)
    #self.ledStrip.animate(delay = 1.0, steps=numberOfSteps)
 
  def stop(self):
    self.running = False

def buttonCallback(channel):
  print "button callback"
  
GPIO.add_event_detect(16, GPIO_FALLING, callback=buttonCallback, bouncetime=300)

clock = Clock()
clock.run()


