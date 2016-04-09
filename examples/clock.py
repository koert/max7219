#!/usr/bin/env python

# Clock for 4 8x8 LED matrices.

import max7219.led as led
import time
import datetime
import socket
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, LCD_FONT, CP437_FONT, CP437KZ_FONT
from random import randrange

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

device = led.matrix(cascaded=4)

device.brightness(2)

device.scrollMessage("Clock 1.1 ", font=proportional(LCD_FONT))
device.scrollMessage(get_ip_address(), font=proportional(LCD_FONT))

time.sleep(1)
device.brightness(0)

while 1:
  str = datetime.datetime.now().strftime('%H:%M  ')
  device.displayMessage(str, font=proportional(LCD_FONT), delay=0.06)
  #device.show_message(str, font=proportional(SINCLAIR_FONT))
  time.sleep(10)


