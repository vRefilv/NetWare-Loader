#imports
import psutil
import subprocess
import os
import time
import sys
from time import sleep as wait
import webbrowser
from pystyle import Colors,Colorate,Write
import configparser

config_file = 'cfg.ini'
# Check if the config file exists
if not os.path.exists(config_file):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Add sections and options with default values
    config['Settings'] = {'autorun': 'False'}

    # Write the configuration to the file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(config_file)

# Access values from the configuration file
autorun = config.getboolean('Settings', 'autorun')  # getboolean() converts the value to a boolean

#clear console function
def cls():
    os.system("cls")
cls()
#waiting animation function
def waiting_animation():
    d = ''
    Write.Print("[/] Waiting for 1v1.lol   ", Colors.blue_to_green, interval=0.05,end='\r')
    for i in range(0,4):
        print(Colorate.Horizontal(Colors.blue_to_green, "[/] Waiting for 1v1.lol"+d, True,),end='\r')
        d=d+'.'
        wait(0.5)

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
        Write.Print("\nRunning 1v1.lol from steam\n", Colors.blue_to_green, interval=0.05)
        webbrowser.open("steam://rungameid/2305790")
        autorun = False
    waiting_animation()
else:
    #if netware found
    cls()
    Write.Print("[+] 1v1.lol found\n", Colors.blue_to_green, interval=0.05)
    wait(2)
    Write.Print("[/] NetWare.dll: Injecting\n", Colors.blue_to_green, interval=0.05)
    
    # injecting netware with sharp mono injector
    try:
        result = subprocess.run(
            ["smi.exe", "inject", "-p", "1v1_LOL", "-a", "NetWare.dll", "-n", "NetWare", "-c", "Loader", "-m", "Load"],
            capture_output=True,
            text=True
        )

        output_str = result.stdout.strip()  # Get the captured output as a string
        Write.Print("[/] "+output_str, Colors.blue_to_green, interval=0.05)

        if result.returncode == 0 and "could not read the file" not in output_str.lower():
            Write.Print("\n[+] NetWare.dll: Injected successfully", Colors.blue_to_green, interval=0.05)
        else:
            Write.Print(f"\n[-] Error: {result.returncode}", Colors.red, interval=0.05)
            if result.returncode == 0:
                Write.Print(f"\n[-] Error: NetWare.dll not found", Colors.red, interval=0.05)
            elif result.returncode == 3762504530:
                Write.Print(f"\n[-] Error: SharpMonoInjector.dll not found", Colors.red, interval=0.05)

    except FileNotFoundError:
        Write.Print("[-] Error: smi.exe not found", Colors.red, interval=0.05)
    except Exception as e:
        Write.Print(f"[-] Error: {str(e)}", Colors.red, interval=0.05)
input()