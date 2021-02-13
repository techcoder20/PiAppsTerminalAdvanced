#!/bin/bash

#Downloading terminal script
wget https://raw.githubusercontent.com/techcoder20/PiAppsPackageManagerTerminal/main/papm.py
#Move it to pi-apps directory
mv papm.py ~/pi-apps
#Create a alias
unalias papm
echo "alias papm='python3 ~/pi-apps/papm.py'" >> ~/.bashrc
