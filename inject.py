#imports
import psutil, subprocess, os, sys, webbrowser, configparser
from time import sleep as wait
from pystyle import Colors,Colorate,Write
from refilmodules import *
from autoupdate import *

cls(None)

cwd = os.path.abspath(os.path.dirname(__file__))
smi = os.path.expandvars(os.path.join(r"%temp%", "NetWare_Loader", "NetWare_Files", "smi.exe"))
dll = os.path.expandvars(os.path.join(r"%temp%", "NetWare_Loader", "NetWare_Files", "NetWare.dll"))
color = Colors.purple_to_blue

repo_url = "https://github.com/waxnet/NetWare"
destination_folder = os.path.expandvars(r"%temp%\NetWare_Loader\NetWare_Files")

config_file = 'cfg.ini'
# Check if the config file exists
if not os.path.exists(config_file):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Add sections and options with default values
    config['Settings'] = {
    'autorun': 'True',
    'autoupdate': 'True'
    }

    # Write the configuration to the file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(config_file)

# Access values from the configuration file
autorun = config.getboolean('Settings', 'autorun')  # getboolean() converts the value to a boolean
autoupdates = config.getboolean('Settings', 'autoupdate')  # getboolean() converts the value to a boolean
#clear console function

banner= r"""
--------------------------------------------------------------------------------

    ____               _           __     _   __     __ _       __              
   / __ \_________    (_)__  _____/ /_   / | / /__  / /| |     / /___ _________ 
  / /_/ / ___/ __ \  / / _ \/ ___/ __/  /  |/ / _ \/ __/ | /| / / __ `/ ___/ _ \
 / ____/ /  / /_/ / / /  __/ /__/ /_   / /|  /  __/ /_ | |/ |/ / /_/ / /  /  __/
/_/   /_/   \____/_/ /\___/\___/\__/  /_/ |_/\___/\__/ |__/|__/\__,_/_/   \___/ 
                /___/                                                           

                        --------------------------
                        | Loader made by Refil   |
                        | NetWare made by waxnet |
                        --------------------------

--------------------------------------------------------------------------------
 
"""
stb = "print(Colorate.Horizontal(color, center_text(banner), True,))"
exec(stb)
wait(2)

if autoupdates == True:
    # Check for update and download the latest release if needed
    check_for_update(repo_url, destination_folder)
    wait(2)
cls(stb)
#check if process is running function
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

#While loop that checks if 1v1_LOL.exe process is running, return true or false
while checkIfProcessRunning('1v1_LOL.exe') == False:
    #if 1v1_LOL.exe process is not found then
    #and if autorun is true then runs 1v1 lol
    if autorun == True:
        slowType(center_text("Running 1v1.lol from steam"))
        webbrowser.open("steam://rungameid/2305790")
        autorun = False
    waiting_animation("[/] Waiting for 1v1.lol")
else:
    #if netware found
    cls(stb)
    slowType(center_text("[+] 1v1.lol found"))
    wait(2)
    slowType(center_text("[/] NetWare.dll: Injecting"))
    
    # injecting netware with sharp mono injector
    try:
        result = subprocess.run(
            [smi, "inject", "-p", "1v1_LOL", "-a", dll, "-n", "NetWare", "-c", "Loader", "-m", "Load"],
            capture_output=True,
            text=True
        )

        output_str = result.stdout.strip()  # Get the captured output as a string
        slowType(center_text("[/] "+output_str))

        if result.returncode == 0 and "could not read the file" not in output_str.lower():
            slowType(center_text("[+] NetWare.dll: Injected successfully"))
        else:
            slowType(center_text(f"[-] Error: {result.returncode}"))
            if result.returncode == 0:
                slowType(center_text("[-] Error: NetWare.dll not found"))
            elif result.returncode == 3762504530:
                slowType(center_text("[-] Error: SharpMonoInjector.dll not found"))

    except FileNotFoundError:
        slowType(center_text("[-] Error: smi.exe not found"))
    except Exception as e:
        slowType(center_text(f"[-] Error: {str(e)}"))
input()