#logToFile method for WildLive python module 
#Devi 2020

from datetime import datetime
#paramerters: text to be logged, file name including extension

def logToFile(text, file):
    t = datetime.now()
    logTime = t.strftime("%m%d%Y %H:%M:%S- ")

    log = open("/home/pi/WildLive/logs/"+file, 'a+')
    log.write(logTime+text+'\n')
    log.close()
    
    return
  
  #testing
logToFile('This another log!', 'testlog.txt')