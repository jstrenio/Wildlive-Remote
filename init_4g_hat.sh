#!/bin/bash
sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'
sudo qmicli --d /dev/cdc-wdm0 -w
sudo ip link set wwan0 down
echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip
sudo ip link set wwan0 up
sudo qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --wds-start-network="apn='phone',ip-type=4" --client-no-release-cid
sudo qmi-network /dev/cdc-wdm0 start
sudo udhcpc -i wwan0
cd /home/pi/WildLive/wildlive_remote_repo/c/SMS/
sudo ./wildlive
exec bash
