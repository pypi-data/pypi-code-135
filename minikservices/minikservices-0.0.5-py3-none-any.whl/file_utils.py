import subprocess
from subprocess import PIPE
import os
import sys
import time
from kservice.colors import bcolors

# minikube service argocd-server --url -n argocd
def run_command(command=None):
    save = sys.stdout

    os.system("nohup minikube service argocd-server --url -n argocd > /tmp/argocd.out 2>&1 &")

    
   

def print_colored(msg=None):
    print(f"{bcolors.HEADER}{msg}{bcolors.ENDC}")

def print_error(msg=None):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")