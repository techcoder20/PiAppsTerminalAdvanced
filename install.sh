#!/bin/bash

#Removing existing pi-apps binary
sudo rm -f /usr/local/bin/pi-apps
rm -f ~/pi-apps/PiApps.py
#Downloading papm file
echo "HOME = \"$HOME\"" >PiApps.py
wget -qO- https://raw.githubusercontent.com/techoder20/PiAppsTerminalAdvanced/main/PiAppsTerminalAdvanced.py >>PiApps.py
mv PiApps.py ~/pi-apps/PiApps.py
#Removing alias if there before
sed -i '/alias pi-apps/d' ~/.bashrc
#Adding alias to bash file
echo "alias pi-apps='python3 ~/pi-apps/PiApps.py'" >> ~/.bashrc
source ~/.bashrc

