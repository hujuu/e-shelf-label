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
from PIL import Image, ImageDraw, ImageFont
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
    font25 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 25)
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image

    newimage = Image.open(os.path.join(picdir, 'qrcode420.bmp'))
    HBlackimage.paste(newimage, (0, 0))

    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.text((100, 5), u'天然本マグロ', font=font20, fill=0)
    drawblack.text((100, 30), u'¥10,000', font=font25, fill=1)
    drawblack.text((100, 60), u'税込価格  ¥10,800', font=font15, fill=0)
    drawblack.text((100, 75), u'100g当たり ¥2,000', font=font15, fill=0)
    # drawry.line((165, 50, 165, 100), fill=0)
    # drawry.line((140, 75, 190, 75), fill=0)
    # drawry.arc((140, 50, 190, 100), 0, 360, fill=0)
    # drawry.rectangle((80, 50, 130, 100), fill=0)
    # drawry.chord((85, 55, 125, 95), 0, 360, fill=1)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

    logging.info("Clear...")
    # epd.init()
    # epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
