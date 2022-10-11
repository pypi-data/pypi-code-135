from tkinter import * 
from tkinter import messagebox


#Hiding tkinter root window.
root = Tk()
root.geometry("1x1")
w = Label(root, text ='empty', font = "50")
root.withdraw()
w.pack()

class errors():
        @staticmethod
        def cli_err_warning():
            print("""
                          (_)            
 __      ____ _ _ __ _ __  _ _ __   __ _ 
 \ \ /\ / / _` | '__| '_ \| | '_ \ / _` |
  \ V  V / (_| | |  | | | | | | | | (_| |
   \_/\_/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/        
        """)
        
@staticmethod
def cli_err_error():
        print("""
   ___ _ __ _ __ ___  _ __ 
  / _ \ '__| '__/ _ \| '__|
 |  __/ |  | | | (_) | |   
  \___|_|  |_|  \___/|_|   
""")
    
    #these 3 show GUI error boxes with the desired text, very convenient for the developer
@staticmethod
def gui_err_show_info(arg1, arg2):   
        messagebox.showinfo(arg1, arg2)
    
@staticmethod
def gui_err_show_warning(arg3, arg4):
        messagebox.showwarning(arg3, arg4)

@staticmethod
def gui_err_show_error(arg5, arg6):
        messagebox.showerror(arg5, arg6)
