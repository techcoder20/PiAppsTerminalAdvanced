#!/bin/bash
pip3 install python-Levenshtein fuzzywuzzy
#Removing existing pi-apps binary
sudo rm -f /usr/local/bin/pi-apps
#Downloading papm file
echo "HOME = \"$HOME\"">PiApps.py
wget -qO- https://raw.githubusercontent.com/techcoder20/PiAppsTerminalAdvanced/main/PiAppsTerminalAdvanced.py >>PiApps.py
#Moving pi apps file to pi apps directory
mv PiApps.py ~/pi-apps
#Removing alias if there before
sed -i '/alias pi-apps/d' ~/.bashrc
#Adding alias to bash file
echo "alias pi-apps='python3 ~/pi-apps/PiApps.py'" >> ~/.bashrc

source ~/.bashrc

