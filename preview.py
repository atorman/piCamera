# Test script for using a rasberry pi camera
# more here: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

from picamera import PiCamera, Color
from os import system
import datetime
from time import sleep
import numpy as np

effect = np.array(['solarize', 'emboss', 'colorswap', 'cartoon', 'oilpaint'])
brightness = np.array([50, 60, 70, 80])
contrast = np.array([30, 40, 50])
iso = np.array([100, 200, 400, 800])

camera = PiCamera()

camera.start_preview()
camera.rotation = 180

for x in iso:
    camera.iso = x
    camera.annotate_text = "ISO: %s" %x
    sleep(10)

#for i in effect:
    #camera.image_effect = i
    #camera.annotate_text = "Effect: %s" % i
    #sleep(5)
    #for j in brightness:
        #camera.brightness = j
        #camera.annotate_text = "Brightness: %s" % j
        #sleep(2)

    
camera.stop_preview()