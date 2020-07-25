#logToFile method for WildLive python module 
#Devi 2020

from datetime import datetime
#paramerters: text to be logged, file name including extension

def logToFile(text, file):
    t = datetime.now()
    logTime = t.strftime("%m%y%H%M%S")

    log = open('\\logs\\'+file, 'a+')
    log.write(logTime+': '+text+'\n')
    log.close()
    
    return
  
  #testing
logToFile('This a log!', 'testlog.txt')