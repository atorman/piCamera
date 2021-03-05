# Timelapse.py modified from a blog I read on Tom's Hardware: 
# https://www.tomshardware.com/how-to/raspberry-pi-time-lapse-video
# and the code is originally from https://github.com/carolinedunn/timelapse
# I modified it for a 6 month construction project 
# Requires crontab -e set to run from 8am - 2pm
# 30 7 * * 1-5 python /home/pi/timelapse/timelapse.py

# Import necessary libraries

from picamera import PiCamera, Color
from os import system
import datetime
from time import sleep

# Set variables to capture camera configurations

#set this to the number of minutes (6 hours = 360 minutes) you wish to run your timelapse camera
tlminutes = 390 

#number of seconds (600 sec = 10 minutes) delay between each photo taken
secondsinterval = 600 

#frames per second timelapse video (default 30)
fps = 30 

# number of photos to take
numphotos = int((tlminutes*60)/secondsinterval) 

# print to screen the calculated number of photos 
print("number of photos to take = ", numphotos)

# set the raw date time stamp 
dateraw= datetime.datetime.now()

# uncomment to reset to original format
#datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M") # format the date time for the file names

# format the day and month for the file name (i.e. 02-01)
datetimeformat = dateraw.strftime("%m-%d") 

# print to screen when the timelapse session begins
print("RPi started taking photos for your timelapse at: " + datetimeformat)

# create the camera object for this session
camera = PiCamera() 

# Rotate the Camera 180 degrees if it's upside down
camera.rotation = 180

# preview camera to line up the image
#camera.start_preview()
#sleep(5)
#camera.stop_preview()

camera.resolution = (1024, 768) # set resolution to 4:3 ratio
#camera.brightness = 50

# Comment out when ready to do long term photo capture to keep from deleting old photos
# system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start

# start looping through to capture images
# name the images after the sequence and date time: 02-20-00.jpg

for i in range(numphotos):
    camera.capture('/home/pi/Pictures/{}-{}.jpg'.format(datetimeformat,i))
    sleep(secondsinterval)

print("Done taking photos.")

# ------------------------------------------------------------

# uncomment code below IF you want to create a video based on a single
# session of timelapse photos

#print("Please standby as your timelapse video is created.")

# Comment out when ready to do long term photo capture to convert separately
#system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
#print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
