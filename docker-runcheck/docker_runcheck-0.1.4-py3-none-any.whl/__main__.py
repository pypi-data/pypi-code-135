import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import docker_runcheck 

if __name__ == "__main__":
    docker_runcheck.run()
