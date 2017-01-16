import time
import picamera

name = "Girlpower"

print("Hello " + name)
picture_number = 1

with picamera.PiCamera() as camera:
  while picture_number < 6: 
    time.sleep(2)
    camera.hflip = True
    camera.vflip = True
    print("Taking Picture Number %d: SAY CHEESE!!!!" % picture_number)
    camera.start_preview()
    time.sleep(5)
    camera.stop_preview()
    camera.capture('/home/pi/Pictures/pic-(%d).jpg' % picture_number)
    print(time.strftime("%I:%M:%S"))
    picture_number += 1
            

