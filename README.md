# wildlive_remote

A Portland State University Project for CS 461/561
Open Source Summer '20
Professor Bart Bassey

Team: John Strenio, Aster Devi, Daniel Hafner

WildLive remote is an open source project to turn a raspberry pi into a remote pingable webcam that can be setup up anywhere with cell signal to record and send live video to any registered cell phone or email address. This project's inital intent is to allow for a live surf conditions check in remote locations but its potential applications are far less trivial and  nearly limitless. For more info contact jstrenio@pdx.edu

DEMO VIDEO: https://youtu.be/Jb2pPwleDmY

Current Phone number for SIM card: 360-593-1550

pi project directory: /home/pi/WildLive/

subdirectories:

/photos

/logs

/c/SMS

SETUP:
    This software requires any SIM card with 4G service connected to a waveshare SIM7600E 4G hat to any linux based system.
    To run this program at startup init_4g_hat.sh must be placed in the default
    users .bashrc file or run at startup using a similar method. This program
    can also simply be run by executing the shell script from the terminal or by
    separately executing ./wildlive located at /c/SMS/wildlive and capture.py
    located at /capture.py concurrently

CITATIONS:
    All of the modem related functions utilize the AT commands from the demo code provided by the manufacturer Waveshare. The AT Commands were pulled from the header files under the /c subdirectory. The C based program portion of this system that actually runs written by the Wildlive team can be found at /c/SMS/wildlive.cpp 
    sources:
    AT commands: https://www.waveshare.com/w/upload/5/54/SIM7500_SIM7600_Series_AT_Command_Manual_V1.08.pdf
    demo code: https://www.waveshare.com/wiki/File:SIM7600X-4G-HAT-Demo.7z
    man pages:https://www.waveshare.com/w/upload/6/6d/SIM7600E-H-4G-HAT-Manual-EN.pdf
    The bash scripts init_4g_hat.sh and wildlive_init.sh are used to connect to the network on startup and are adapted from User: mkrzysztofowicz on the website: raspberrypi.org 
    source: https://www.raspberrypi.org/forums/viewtopic.php?f=36&t=224355