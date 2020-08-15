#logToFile method for WildLive python module 
#Devi 2020

from datetime import datetime
#paramerters: text to be logged, file name including extension

def logToFile(text, file):
    t = datetime.now()
    logDay = t.strftime("%m%d%Y")
    logTime = t.strftime("%m%d%Y %H:%M:%S- ")

    log = open('/home/pi/WildLive/logs/'+logDay, 'a+')
    log.write(logTime+text+file)
    log.close()

