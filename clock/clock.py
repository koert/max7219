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

BUTTON_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Clock():
  def __init__(self):
    self.device = led.matrix(cascaded=4)
    self.device.brightness(2)
    self.displayOn = True
    
  def run(self):
    self.device.scrollMessage("Clock 1.2 ", font=proportional(LCD_FONT))
    self.device.scrollMessage(get_ip_address(), font=proportional(LCD_FONT))
    time.sleep(5)
    self.device.brightness(0)
    while 1:
      if (self.displayOn):
        self.displayTime()
      #str = datetime.datetime.now().strftime('%H:%M  ')
      #self.device.displayMessage(str, font=proportional(LCD_FONT), delay=0.06)
      time.sleep(10)
      
  def setDisplayOn(self, displayOn):
    self.displayOn = displayOn
      
  def displayTime(self):
    str = datetime.datetime.now().strftime('%H:%M  ')
    self.device.displayMessage(str, font=proportional(LCD_FONT), delay=0.06)

  def displayMessage(self, message):
    self.device.displayMessage(message, font=proportional(LCD_FONT), delay=0.06)

class DisplayTimeThread(threading.Thread):
  def __init__(self, clock):
    threading.Thread.__init__(self)
    self.clock = clock
    self.running = False

  def run(self):
    self.running = True
    self.clock.setDisplayOn(True)
    self.clock.displayTime()
    time.sleep(10)
    self.clock.setDisplayOn(False)
    self.clock.displayMessage("        ")
    print ("end of run")
    #self.ledStrip.bar2(self.color)
    #self.ledStrip.animate(delay = 1.0, steps=numberOfSteps)
 
  def stop(self):
    self.running = False

def buttonCallback(channel):
  print ("button callback")
  DisplayTimeThread(clock).start()
  

#GPIO.wait_for_edge(16, GPIO.FALLING) 
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=buttonCallback, bouncetime=300)

clock = Clock()
clock.run()


