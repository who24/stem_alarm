import time
import picamera

name = "Girlpower"

print "Hello " + name
print "This program will take 1 picture and 1 video 5 times now!"
print "Look for the pics in the 'Pictures' folder and videos in 'Videos'"
number = 1

with picamera.PiCamera() as camera:
  while number < 6: 
    time.sleep(2)
    camera.hflip = True
    camera.vflip = True
    camera.start_preview()
    print "Taking Picture Number %d: SAY CHEESE!!!!" % number
    camera.capture('/home/pi/Pictures/pic-%d.jpg' % number) 
    print "Taking Video Number %d: SMILE AT THE CAMERA !!!!" % number
    camera.start_recording('/home/pi/Videos/vid-%d.h264' % number)
    time.sleep(7)
    camera.stop_recording()
    camera.stop_preview()
    print time.strftime("%I:%M:%S") + "ALERT: Camera was activated!"
    number += 1
