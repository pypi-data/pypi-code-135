from termcolor import colored
import colorama
import os
import time
import os
import ctypes
import msvcrt
import subprocess
import datetime

from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)


def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)


maximize_console()

colorama.init()


def start():
    colors=["green","cyan","magenta","red","yellow"]
    while True:
        for color in colors:
            print(colored('''
            ██╗   ██╗ ██████╗     ██████╗ ██████╗  ██████╗     ██╗    ████████╗██████╗  █████╗ ██╗   ██╗███████╗██╗     ██╗     ███████╗██████╗ 
            ╚██╗ ██╔╝██╔═══██╗    ██╔══██╗██╔══██╗██╔═══██╗    ██║    ╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██║     ██║     ██╔════╝██╔══██╗
             ╚████╔╝ ██║   ██║    ██████╔╝██████╔╝██║   ██║    ██║       ██║   ██████╔╝███████║██║   ██║█████╗  ██║     ██║     █████╗  ██║  ██║
              ╚██╔╝  ██║   ██║    ██╔══██╗██╔══██╗██║   ██║    ██║       ██║   ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║     ██║     ██╔══╝  ██║  ██║
               ██║   ╚██████╔╝    ██████╔╝██║  ██║╚██████╔╝    ██║       ██║   ██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗███████╗███████╗██████╔╝
               ╚═╝    ╚═════╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ 
                                                                                                                                                
            ''',f"{color}"))

            print(colored('''
            ██████╗ ███████╗    ██████╗  █████╗  ██████╗██╗  ██╗     ██████╗ ███╗   ██╗    ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗   ██╗
            ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
            ██████╔╝█████╗      ██████╔╝███████║██║     █████╔╝     ██║   ██║██╔██╗ ██║    ███████╗███████║   ██║   ██║   ██║██████╔╝██║  ██║███████║ ╚████╔╝ 
            ██╔══██╗██╔══╝      ██╔══██╗██╔══██║██║     ██╔═██╗     ██║   ██║██║╚██╗██║    ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║  ██║██╔══██║  ╚██╔╝  
            ██████╔╝███████╗    ██████╔╝██║  ██║╚██████╗██║  ██╗    ╚██████╔╝██║ ╚████║    ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██████╔╝██║  ██║   ██║   
            ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                                                                                   
            ''',f"{colors[colors.index(color)-1]}"))

            timer_remaining=datetime.datetime.strptime('Oct 2 2022  1:33AM', '%b %d %Y %I:%M%p')
            print(f"\n[   ] count down to update at {'Oct 2 2022  1:33AM'}\n")

            print(colored(f"[  ] Next update will occur in {timer_remaining-datetime.datetime.now()}", "cyan"))
            time.sleep(0.5)
            os.system("cls")
