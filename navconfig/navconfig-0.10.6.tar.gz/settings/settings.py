# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
from navconfig import config, DEBUG

print('::: LOADING SETTINGS ::: ')

# we are in local aiohttp development?
LOCAL_DEVELOPMENT = (DEBUG is True and sys.argv[0] == 'run.py')
SEND_NOTIFICATIONS = config.get('SEND_NOTIFICATIONS', fallback=True)
