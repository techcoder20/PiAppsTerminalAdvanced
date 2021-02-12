import os
import os.path
import sys 
try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("fuzzywuzzy Is Not Installed, Installing it :)")
    os.system("pip3 install fuzzywuzzy")
from colorama import Fore, Back, Style

#Checking if system is 32 bit or 64 bit
if sys.maxsize > 32 == False:
    system=64
else:
    system=32

PiAppsDirectory = os.listdir("/home/pi/pi-apps/apps")
AppsName=[]
AppsNameNoSpaces=[]
InstalledApps= os.listdir("/home/pi/pi-apps/data/installed-packages")
SearchResults=0
SimilarityRubric=100

for appname in PiAppsDirectory:
    #Checking if system is 32-bit
    if system == 32:
        #Checking if app is 32-bit
        if os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install-32") or os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install"):
            AppsName.append(appname)
            appname = appname.replace(" ","\ ")
            AppsNameNoSpaces.append(appname)
    #Checking if system is 64-bit
    elif system == 64:
        #Checking if app is 64-bit
        if os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install-64") or os.path.isfile("/home/pi/pi-apps/apps/" + appname + "install"):
            AppsName.append(appname)
            appname = appname.replace(" ","\ ")
            AppsNameNoSpaces.append(appname)

#List Argument
try: 
    if sys.argv[1] == "list-installed":
        for InstalledApp in InstalledApps:
            print(Fore.GREEN + InstalledApp)
            fo = open("/home/pi/pi-apps/apps/" + InstalledApp + "/description","r")
            description = fo.read()
            print(Fore.CYAN + description)
            fo.close()
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

try:
    if sys.argv[1] == "list-all":
        for appname in AppsName:
            print(Fore.GREEN + appname)
            fo = open("/home/pi/pi-apps/apps/" + appname + "/description","r")
            description = fo.read()
            print(Fore.CYAN + description)
            fo.close()
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

#Install argument
try:
    if sys.argv[1] == "install":
        for i in AppsName:
            AppExists=False
            if sys.argv[2] == i:
                print("The '" + i + "' App Exists")
                AppExists=True
                AppNameNoSpace = str(AppsNameNoSpaces[AppsName.index(i)])
                os.system("~/pi-apps/manage multi-install " + AppNameNoSpace)
                break
            else:
                AppExists=False
        if AppExists == False:
            print(Fore.RED + "App Doesnt Exist. Use command 'papm list --all' to list the apps also make sure to use '' while entering app name")
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

#Uninstall argument
try:
    if sys.argv[1] == "uninstall":
        for i in AppsName:
            AppExists=False
            if sys.argv[2] == i:
                print("The '" + i + "' App Exists")
                AppExists=True
                AppNameNoSpace = str(AppsNameNoSpaces[AppsName.index(i)])
                os.system("~/pi-apps/manage multi-uninstall " + AppNameNoSpace)
                break
            else:
                AppExists=False
        if AppExists == False:
            print(Fore.RED + "App Doesnt Exist. Use command 'papm installed list --all' to list the installed apps also make sure to use '' while entering app name")
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

#Search argument
try:
    if sys.argv[1] == "search":
        while SearchResults==0:
            if SimilarityRubric > 0:
                SimilarityRubric -= 10
                for i in AppsName:
                    similarity= fuzz.ratio(i.lower(), sys.argv[2].lower())
                    #print(str(i) + str(similarity))
                    if similarity > SimilarityRubric or similarity == SimilarityRubric:
                        print(Fore.GREEN + i)
                        fo = open("/home/pi/pi-apps/apps/" + i + "/description","r")
                        description = fo.read()
                        print(Fore.CYAN + description)
                        fo.close()
                        SearchResults += 1
            else:
                print("No Search Results Found :(")
                quit()
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

try:
    if sys.argv[1] == "update":
        os.system("/home/pi/pi-apps/manage update-all")
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()

try:
    if sys.argv[1] == "help":
        print(Fore.BLUE + "Usage")
        print(Fore.GREEN + "papm [argument]")
        print()
        print(Fore.BLUE + "Available Arguments: ")
        print(Fore.GREEN + "list-all" +Fore.CYAN+ "  Prints the list of available apps that are installable")
        print(Fore.GREEN + "list-installed" +Fore.CYAN+ "  Prints all installed apps")
        print(Fore.GREEN + "install '[appname]'" +Fore.CYAN+ "  Install any app available in pi-apps")
        print(Fore.GREEN + "uninstall '[appname]'" +Fore.CYAN+ "  Uninstall any app available in pi-apps")
        print(Fore.GREEN + "search '[appname]'" +Fore.CYAN+ "  Search for a app in pi apps")
        print(Fore.GREEN + "update" +Fore.CYAN+ "  Update pi-apps")
except IndexError:
    print(Fore.RED + "Please enter valid argument. Use command 'papm --help' to get a list of valid arguments")
    quit()