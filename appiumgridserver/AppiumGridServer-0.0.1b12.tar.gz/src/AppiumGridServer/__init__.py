# encoding: utf-8
import os
import jdk
import glob
import logging
import requests
import zipfile
from nodejs import node, npm
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
    def set_grid_server(self, android_home, port=4723, debug=False):
        """
        Examples:
        | ${remote_url} | `Set Grid Server` | port=4444  | 
        """
        os.system('killport %s' %(port))
        npm.call(['--prefix', current_path, 'install', '--save', 'appium'])
        npm_process = npm.Popen(['config', 'get', 'prefix'])
        download_url = jdk.get_download_url('18', jre=True)
        responseJdk = requests.request("GET", download_url, allow_redirects=True)
        open('%s/OpenJDK.zip' %(current_path), 'wb').write(responseJdk.content)
        with zipfile.ZipFile('%s/OpenJDK.zip' %(current_path), 'r') as zip_ref:
            zip_ref.extractall(current_path)
        check_file = glob.glob('%s/jdk*/' %(current_path))
        os.remove('%s/OpenJDK.zip' %(current_path))
        appiunPath = '%s/node_modules/appium/build/lib/main.js' %(current_path)
        os.environ['PATH'] += ';%s' %(npm_process.args[0].replace('npm.cmd',''))
        os.environ['ANDROID_HOME'] = android_home
        os.environ['JAVA_HOME'] = check_file[0].replace('\\', '/')
        if debug:
            npm.call(['--prefix', current_path, 'install', '--save', 'appium-doctor'])
            os.system('appium-doctor')
        os.popen('node %s -p %s --session-override > %s/log_%s.txt' %(appiunPath, port, current_path, port))
        print('AppiumGridServer Pull Success')
        server = 'http://localhost:%s/wd/hub' %(port)
        return server

