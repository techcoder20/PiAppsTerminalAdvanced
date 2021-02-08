#!/bin/bash

generartlist() {
  appslist=() #appslist array
  #adding app names to applist aray
  for file in /home/pi/pi-apps/apps/*; do
      echo "$(basename "$file")"
  done
}

#Version argument for papm command
if [ "$1" == "version" ] || [ "$1" == "--v" ];then
  echo "Current Version: LoL I dont even know if pi apps has version :)"
#update argument for papm command
elif [ "$1" == "update" ];then
  ~/pi-apps/updater
#list argument for papm command
elif [ "$1" == "list" ];then
  generartlist
fi



