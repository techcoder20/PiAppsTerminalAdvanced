# PiAppsTerminalAdvanced
This is a prototype of PiAppsPackageManager terminal commands

## Install Command
```
wget -qO- https://raw.githubusercontent.com/techcoder20/PiAppsTerminalAdvanced/main/install.sh | bash
```

## Available Arguments

`papm install '[appname]'`  
You can use this command to install any app available in pi apps. If your app's name has a space make sure to put the name in quotes.  

`papm uninstall '[appname]'`  
You can use this command to uninstall any app available in pi apps. If your app's name has a space make sure to put the name in quotes.  

`papm list-all`  
Prints a list of all available apps in pi apps with their description.  

`papm list-installed`  
Prints a list of installed apps.  

`papm list-uninstalled`  
Prints a list of uninstalled apps.  

`papm search '[appname]'`
Search for any app in Pi-Apps

`papm update`  
Update all installed apps

`papm '[appname]'`  
Prints website for app
