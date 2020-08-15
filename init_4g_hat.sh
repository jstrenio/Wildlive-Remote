#!/bin/bash
#Filename: init_4g_hat.sh
#Original Author: John Strenio
#Sources: User: mkrzysztofowicz Website: raspberrypi.org see README for details
#Description: this script needs to be run at startup and initializes the modem
#             connects with the network, and begins running the SMS program
sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'
sudo qmicli --d /dev/cdc-wdm0 -w
sudo ip link set wwan0 down
echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip
sudo ip link set wwan0 up
sudo qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --wds-start-network="apn='phone',ip-type=4" --client-no-release-cid
sudo qmi-network /dev/cdc-wdm0 start
sudo udhcpc -i wwan0
cd /home/pi/Wildlive/wildlive_remote_repo/
sudo gnome-terminal -- python3 capture.py
cd /home/pi/WildLive/wildlive_remote_repo/c/SMS/
sudo ./wildlive
exec bash
