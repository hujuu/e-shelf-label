#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13bc Demo")
    
    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    logging.info("3.read bmp file")
    HBlackimage = Image.open(os.path.join(picdir, '2in13bc-b.bmp'))
    HRYimage = Image.open(os.path.join(picdir, '2in13bc-ry.bmp'))
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)
    
    logging.info("4.read bmp file on window")
    blackimage1 = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    redimage1 = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
    newimage = Image.open(os.path.join(picdir, '100x100.bmp'))
    blackimage1.paste(newimage, (10,10))    
    epd.display(epd.getbuffer(blackimage1), epd.getbuffer(redimage1))
    
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
