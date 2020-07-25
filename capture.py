# methods for capturing image and video for WildLiveCam
# Devi 2020

from picamera import PiCamera
from time import sleep
from datetime import datetime
from datetime import timezone
import logToFile

t = datetime.now()
stamp = t.strftime("%m%y%H%M%S")

camera = PiCamera()
camera.start_preview()
sleep(3)
err = camera.capture('/home/pi/photos/'+stamp+'.jpg')
#add try/except to send error alert 
camera.stop_preview()

t = datetime.now()
logtime = t.strftime("%m%y%H%M%S")
if err ==0:
	logToFile(logtime, 'saved image ' + stamp)
else
	logToFile(logtime, 'failed to capture image ' + stamp)

