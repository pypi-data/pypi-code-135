# encoding: utf-8
import os
import sys
import jdk
import glob
import psutil
import shutil
import zipfile
import logging
import requests
from nodejs import node, npm, npx
from robot.api.deco import keyword

current_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

class AppiumGridServer(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 0.1

    def __init__(self):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        logger = logging.getLogger(__name__)

    @keyword('Set Grid Server')
    def set_grid_server(self, port=4724, version='latest'):
        """
        Examples:
        | ${remote_url} | `Set Grid Server` | port=4444  | version=latest  | 
        | ${remote_url} | `Set Grid Server` | port=1234  | version=latest  |
        | ${remote_url} | `Set Grid Server` | port=4444  | version=gc:106.0.5249.61  |
        | ${remote_url} | `Set Grid Server` | port=4444  | version=ff:latest  |
        """
        npm.call(['install', '--save', 'appium@1.22.3'])
        npm_process = npm.Popen(['config', 'get', 'prefix'])
        appiunPath = 'node_modules/appium/build/lib/main.js'
        os.environ['PATH'] += ';%s' %(npm_process.args[0].replace('npm.cmd',''))
        os.popen('node %s -p %s --session-override > log_%s.txt' %(appiunPath, port, port))
        print('AppiumGridServer Pull Success')

