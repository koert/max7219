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

device = matrix(cascaded=4)

device.brightness(2)

device.scrollMessage("Clock ", font=proportional(CP437_FONT))
device.scrollMessage(get_ip_address(), font=proportional(CP437KZ_FONT))

time.sleep(1)
device.brightness(0)

while 1:
  str = datetime.datetime.now().strftime('%H:%M')
  device.displayMessage(str, font=proportional(CP437KZ_FONT), delay=0.1)
  #device.show_message(str, font=proportional(SINCLAIR_FONT))
  time.sleep(10)


