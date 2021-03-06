import os
import os.path
import sys 
try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("fuzzywuzzy Is Not Installed, Installing it :)")
    os.system("pip3 install python-Levenshtein fuzzywuzzy")
from colorama import Fore, Back, Style

#Checking if system is 32 bit or 64 bit
if sys.maxsize > 32 == False:
    system=64
else:
    system=32

PiAppsDirectory = os.listdir("/home/pi/pi-apps/apps")
AppsName=[]
AppsNameNoSpaces=[]
InstalledApps= os.listdir("/home/pi/pi-apps/data/status")

for appname in PiAppsDirectory:
    #Checking if system is 32-bit
    if system == 32:
        #Checking if app is 32-bit
        if os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install-32") or os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install") and appname != "template":
            AppsName.append(appname)
            appname = appname.replace(" ","\ ")
            AppsNameNoSpaces.append(appname)
    #Checking if system is 64-bit
    elif system == 64:
        #Checking if app is 64-bit
        if os.path.isfile("/home/pi/pi-apps/apps/" + appname + "/install-64") or os.path.isfile("/home/pi/pi-apps/apps/" + appname + "install") and appname != "template":
            AppsName.append(appname)
            appname = appname.replace(" ","\ ")
            AppsNameNoSpaces.append(appname)


def list_installed():
    for InstalledApp in InstalledApps:
        AppStatus = open("/home/pi/pi-apps/data/status/" + InstalledApp ,"r")
        status = AppStatus.read()
        AppStatus.close()
        if status.strip() == "installed":
            print(Fore.GREEN + InstalledApp)
            descriptionfile = open("/home/pi/pi-apps/apps/" + InstalledApp + "/description","r")
            description = descriptionfile.read()
            print(Fore.CYAN + description)
            descriptionfile.close()
                
def list_uninstalled():
    for InstalledApp in InstalledApps:
        AppStatus = open("/home/pi/pi-apps/data/status/" + InstalledApp ,"r")
        status = AppStatus.read()
        AppStatus.close()
        if status.strip() == "uninstalled":
            print(Fore.GREEN + InstalledApp)
            descriptionfile = open("/home/pi/pi-apps/apps/" + InstalledApp + "/description","r")
            description = descriptionfile.read()
            print(Fore.CYAN + description)
            descriptionfile.close()

def list_all():
    for appname in AppsName:
        print(Fore.GREEN + appname)
        descriptionfile = open("/home/pi/pi-apps/apps/" + appname + "/description","r")
        description = descriptionfile.read()
        print(Fore.CYAN + description)
        descriptionfile.close()

def install(AppName):
    for i in AppsName:
        AppExists=False
        if AppName == i:
            print(f"The {AppName} App Exists")
            AppExists=True
            AppNameNoSpace = str(AppsNameNoSpaces[AppsName.index(AppName)])
            os.system("~/pi-apps/manage multi-install " + AppNameNoSpace)
            break
        else:
            AppExists=False
    if AppExists == False:
        print(Fore.RED + "App Doesnt Exist. Use command 'pi-apps list-all' to list the available apps also make sure to use '' while entering app name")

def uninstall(AppName):
    for i in AppsName:
        AppExists=False
        if AppName == i:
            print("The '" + i + "' App Exists")
            AppExists=True
            AppNameNoSpace = str(AppsNameNoSpaces[AppsName.index(i)])
            os.system("~/pi-apps/manage multi-uninstall " + AppNameNoSpace)
            break
        else:
            AppExists=False
    if AppExists == False:
        print(Fore.RED + "App Doesnt Exist. Use command 'pi-apps list-installed' to list the installed apps also make sure to use '' while entering app name")


def search(AppName):
    SearchResults=0
    SimilarityRubric=100
    if sys.argv[1] == "search":
        while SearchResults==0:
            if SimilarityRubric > 0:
                SimilarityRubric -= 10
                for i in AppsName:
                    similarity= fuzz.ratio(i.lower(), AppName.lower())
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

def update():
    if sys.argv[1] == "update":
        os.system("/home/pi/pi-apps/manage update-all")


def website(AppName):
    AppFound = False
    for App in AppsName:
        if AppName == App:
            WebsiteFile = open("/home/pi/pi-apps/apps/" + App + "/website","r")
            website = WebsiteFile.read()
            print(Fore.CYAN + website.strip())
            WebsiteFile.close()
            AppFound = True
            quit()
    if AppFound == False:
        print(Fore.RED + "Please enter valid appname. Use command 'pi-apps list-all' to get the list of apps")            
                
def help():
    print(Fore.BLUE + "Usage")
    print(Fore.GREEN + "pi-apps [argument]")
    print()
    print(Fore.BLUE + "Available Arguments: ")
    print(Fore.GREEN + "list-all" +Fore.CYAN+ "  Prints the list of available apps that are installable")
    print(Fore.GREEN + "list-installed" +Fore.CYAN+ "  Prints all installed apps")
    print(Fore.GREEN + "list-uninstalled" +Fore.CYAN+ "  Prints all uninstalled apps")
    print(Fore.GREEN + "install '[appname]'" +Fore.CYAN+ "  Install any app available in pi-apps")
    print(Fore.GREEN + "uninstall '[appname]'" +Fore.CYAN+ "  Uninstall any app available in pi-apps")
    print(Fore.GREEN + "search '[appname]'" +Fore.CYAN+ "  Search for a app in pi apps")
    print(Fore.GREEN + "update" +Fore.CYAN+ "  Update pi-apps")
    print(Fore.GREEN + "website '[appname]'" +Fore.CYAN+ "  Prints website for app")
    print(Fore.GREEN + "gui" +Fore.CYAN+ "  Launches gui for pi-apps")


if len(sys.argv) > 1:
    if sys.argv[1] == 'install':
        if len(sys.argv) > 2:
            install(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'pi-apps list-all' to list the apps also make sure to use '' while entering app name if it contains spaces")
            quit()
    elif sys.argv[1] == 'uninstall':
        if len(sys.argv) > 2:
            uninstall(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'pi-apps list-all' to list the apps also make sure to use '' while entering app name if it contains spaces")
            quit()
    elif sys.argv[1] == 'website':
        if len(sys.argv) > 2:
            website(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'pi-apps list-all' to list the apps also make sure to use '' while entering app name if it contains spaces")
            quit()
    elif sys.argv[1] == 'search':
        if len(sys.argv) > 2:
            search(sys.argv[2])
        else:
            print(Fore.RED + "Enter valid search term")
            quit()
    elif sys.argv[1] == 'list-all':
        list_all()
    elif sys.argv[1] == 'list-installed':
        list_installed()
    elif sys.argv[1] == 'list-uninstalled':
        list_uninstalled()
    elif sys.argv[1] == 'gui':
        os.system('~/pi-apps/gui')
    elif sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'update':
        update()
    else:
        print(Fore.RED + "Please enter valid argument. Use command 'pi-apps help' to get a list of valid arguments")
        quit()
else:
    os.system('~/pi-apps/gui')
