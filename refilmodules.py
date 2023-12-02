import psutil, win32gui, win32con, os
from pystyle import Colors,Colorate,Write,Center,Cursor
color = Colors.purple_to_blue
from time import sleep as wait
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def maximizewindow():
    '''
    Maximizes application window.
    '''
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def center_text(text):
    '''
    Centers text in cmd.
    '''
    terminal_width = os.get_terminal_size().columns
    text_lines = text.split('\n')
    max_line_length = max(len(line) for line in text_lines)

    centered_text = ""
    for line in text_lines:
        padding = (terminal_width - max_line_length) // 2
        centered_text += " " * padding + line + "\n"

    return centered_text

def cls(stb):
    '''
    Clears cmd.
    '''
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
    os.system("cls")
    if stb is not None:
        exec(stb)

#waiting animation function
def waiting_animation(text):
    '''
    Waiting animation like ...
    '''
    d=''
    centered_text = Center.XCenter(text)
    Write.Print(f"{centered_text}   ", color, interval=0.03,end='\r')
    for i in range(0,3):
        wait(0.5)
        d+='.'
        print(Colorate.Horizontal(color, centered_text+d, True,),end='\r')
        wait(0.5)

def slowTyping(text: str, speed: float, new_line=True):
    for char in text:
        if char == ' ':
            print(char, end="", flush=True)
        else:
            print(char, end="", flush=True)
            wait(speed)
    if new_line:
        print()

def slowType(text: str):
    Cursor.HideCursor()

    # Define the original text with leading spaces
    original_text = text

    # Print leading spaces normally
    leading_spaces = original_text[:len(original_text) - len(original_text.lstrip())]
    print(leading_spaces, end="", flush=True)

    # Apply slowType to the rest of the text
    rest_of_text = original_text[len(leading_spaces):]
    slowTyping(Colorate.Horizontal(Colors.purple_to_blue, rest_of_text), 0.0001)
