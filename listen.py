# main() and listen methods - Runs continuously, detects and parses text message input
# Hafner, Devi, Strenio 2020

import os
from capture import take_pic
from capture import take_vid
from send_email import send_mail
from time import sleep


# expected file size for listen
# this allows for a newline character but still shows file as empty
MIN_SIZE = 6
cmd_list = []

# check for change in file
def listen():
    if os.stat("/home/pi/WildLive/sms_input.txt").st_size > MIN_SIZE:
        print("opening file")

        # if changed open it
        with open("/home/pi/WildLive/sms_input.txt", 'r+') as filestream:
            # read and parse commands
            line = filestream.readline()
            cmd_list = line.split(",")
            cmd_list[-1] = cmd_list[-1].rstrip("\n")
            for i in range(len(cmd_list)):
                cmd_list[i] = cmd_list[i].strip()
            print(cmd_list)

            # check if photo is in the commands list
            if 'photo' in cmd_list:
                print("taking photo")
                path = take_pic()
#                send_mail(path, line)

            # check if photo is in the commands list
            if 'video' in cmd_list:
                print("taking video")
                path = take_vid()
#                send_mail(path, line)
        

            # wipe file for next command
            filestream.truncate(0)
    else:
        print("file empty")
        sleep(3)



def main():
    # runs continuously
    while (True):
        # check if the file has been written to
        listen()


if __name__ == "__main__":
    main()




