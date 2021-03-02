#!/bin/bash

#Downloading papm file
wget https://raw.githubusercontent.com/techcoder20/PiAppsPackageManagerTerminal/main/papm.py
#Moving pi apps file to pi apps directory
mv papm.py ~/pi-apps
#Removing alias if there before
sed -i '/alias papm/d' ~/.bashrc
#Adding alias to bash file
echo "alias papm='python3 ~/pi-apps/papm.py'" >> ~/.bashrc
source ~/.bashrc

