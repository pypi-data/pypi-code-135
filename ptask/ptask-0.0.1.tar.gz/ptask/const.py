"""Important constants to use for this project code."""

import platform

# Operating system architecture
ARCH = platform.architecture()[0]
SYS64 = platform.machine().endswith('64')
SYS32 = not SYS64

# Get current platforms
WIN32 = (platform.system() == 'Windows')
LINUX = (platform.system() == 'Linux')
MACOS = (platform.system() == 'Darwin')

OS = ''
if WIN32:
    OS = 'win32'
elif LINUX:
    OS = 'linux'
elif MACOS:
    OS = 'macos'
