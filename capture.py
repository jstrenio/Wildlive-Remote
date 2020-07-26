# methods for capturing image and video for WildLiveCam
# Devi 2020

from picamera import PiCamera
from time import sleep
from datetime import datetime
from logToFile import logToFile

t = datetime.now()
stamp = t.strftime("%m%y%H%M%S")

camera = PiCamera()
camera.start_preview()
sleep(3)
camera.capture('/home/pi/WildLive/photos/'+stamp+'.jpg')
#add try/except to send error alert 
camera.stop_preview()
camera.close()

t = datetime.now()
logtime = t.strftime("%m%y%H%M%S")
logToFile(logtime, 'saved image ' + stamp)



