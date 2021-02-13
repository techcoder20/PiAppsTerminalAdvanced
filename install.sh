#!/bin/bash

wget https://raw.githubusercontent.com/techcoder20/PiAppsPackageManagerTerminal/main/papm.py
mv papm.py ~/pi-apps
alias papm='python3 ~/pi-apps/papm.py'
echo "alias papm='python3 ~/pi-apps/papm.py'" >> ~/.bashrc
papm help
