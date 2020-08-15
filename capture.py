# Image and video capture functionality for WildLiveCam
# Hafner, Devi, Strenio 2020

# picamera code structure based on https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

from picamera import PiCamera
from time import sleep
from datetime import datetime
from logToFile import logToFile


# capture and save still image
def take_pic():
    t = datetime.now()
    stamp = t.strftime("%m%y%H%M%S")
    #path variable to return from this function
    path = '/home/pi/WildLive/photos/'+stamp+'.jpg'

    camera = PiCamera()
    camera.start_preview()
    sleep(3)

    camera.capture(path)
    #add try/except to send error alert 
    camera.stop_preview()
    camera.close()

    t = datetime.now()
    logtime = t.strftime("%m%y%H%M%S")
    logToFile('saved image ', stamp+'.jpg')
    print("photo taken")
    return path


# capture and save video
def take_vid():
    t = datetime.now()
    stamp = t.strftime("%m%y%H%M%S")
    #path variable to return from this function
    path = '/home/pi/WildLive/video/' + stamp +'.h264'
    length = 5 #video length

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    sleep(3)
    camera.start_recording(path)
    sleep(length)
    camera.stop_recording()
    camera.stop_preview()
    camera.close()

    t = datetime.now()
    logtime = t.strftime("%m%y%H%M%S")
    logToFile('saved 10s video', stamp)
    print("video saved")
    return path




