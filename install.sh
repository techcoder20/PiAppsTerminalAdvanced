#!/bin/bash

wget https://raw.githubusercontent.com/techcoder20/PiAppsPackageManagerTerminal/main/papm.py
mv papm.py ~/pi-apps
echo "alias papm='python3 ~/pi-apps/papm.py'" >> ~/.bashrc
alias papm='python3 ~/pi-apps/papm.py'
bash
papm help
