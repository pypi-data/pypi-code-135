import os
import sys
import platform
import ctypes

systeminformation = platform.uname()
ask_for_admin = 'asadmin'


class System():
        @staticmethod
        def askadmin():
                try:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                
                except:
                    print("Error, Permission Denied.")





        # waits for developer to call variables, then provides the details to the developer
        #When called the variables run a functions by using the platform library, which then fetches the values and stores them in the variable.
        os = systeminformation.system
        computer_name = systeminformation.node
        os_version = systeminformation.release
        os_build = systeminformation.version
        cpu_architechture = systeminformation.machine
        processor = systeminformation.processor

        
        
        # this can be used so if your program has dependencies you can easily use this funtion to install required libraries for your program!
        # Always make sure you have the users permission to install the dependencies/libraries
        # also make sure the libraries you are using are safe to use
        @staticmethod
        def dep_install(libname):
                os.system(f"pip install {libname}")
        
        

        
        @staticmethod
        def create_File(filepath):
            open(f"{filepath}", "x")
        
        
        @staticmethod
        def move_File(filepath1, filepath2):
                os.rename(filepath1, filepath2)
            
        

        @staticmethod
        def remove_File(filename):
            os.remove(filename)
        

        @staticmethod
        def exec_File(filename1):
            os.startfile(filename1)

        
        @staticmethod
        def exec_cmd(cmd):
            os.system(cmd)
        
        @staticmethod
        def exec_CommandPrompt(cmd1):
            os.system(f"cmd /k {cmd1}");
