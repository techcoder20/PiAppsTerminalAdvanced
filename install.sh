#!/bin/bash

#Removing existing pi-apps binary
sudo rm /usr/local/bin/pi-apps
#Downloading papm file
wget https://raw.githubusercontent.com/techcoder20/PiAppsTerminalAdvanced/main/PiAppsTerminalAdvanced.py
#Moving pi apps file to pi apps directory
mv PiAppsTerminalAdvanced.py ~/pi-apps
#Removing alias if there before
sed -i '/alias pi-apps/d' ~/.bashrc
#Adding alias to bash file
echo "alias pi-apps='python3 ~/pi-apps/PiAppsTerminalAdvanced.py'" >> ~/.bashrc

source ~/.bashrc

