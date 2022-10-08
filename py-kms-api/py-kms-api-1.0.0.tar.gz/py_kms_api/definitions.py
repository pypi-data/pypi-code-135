"""
# PyKMS API Definitions
"""

# standard
from subprocess import Popen
from pathlib import Path


__py_kms = Path(__file__).parent / 'py-kms/py-kms'


def start_server() -> Popen[bytes]:
    """
    # Start KMS Server
    """
    return Popen(['python', f'{__py_kms}/pykms_Server.py'])
    

def stop_server(proc: Popen[bytes]) -> None:
    """
    # Stop KMS Server
    """
    proc.terminate()
