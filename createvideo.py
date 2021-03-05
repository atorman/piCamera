# Timelapse.py modified from a blog I read on Tom's Hardware: 
# https://www.tomshardware.com/how-to/raspberry-pi-time-lapse-video
# and the code is originally from https://github.com/carolinedunn/timelapse
# I modified it for a 6 month construction project 

# Import necessary libraries

from picamera import PiCamera, Color
from os import system
import datetime
from time import sleep

#frames per second timelapse video
fps = 20 

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")

# print to screen to let you know it's starting
print("Please standby as your timelapse video is created.")

system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))

# uncomment line below only if you want to delete photos after creating the video
#system('rm /home/pi/Pictures/*.jpg')

# print to screen to let you know it's done
print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
