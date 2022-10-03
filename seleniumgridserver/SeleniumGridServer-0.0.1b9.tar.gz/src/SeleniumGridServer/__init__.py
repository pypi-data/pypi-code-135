# encoding: utf-8
import os
import jdk
import glob
import psutil
import shutil
import zipfile
import logging
import requests
import webdrivermanager as wdm
from robot.api.deco import keyword

current_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

class SeleniumGridServer(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 0.1

    def __init__(self):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        logger = logging.getLogger(__name__)

    @keyword('Set Grid Server')
    def set_grid_server(self, port=4444, version='latest'):
        """
        Examples:
        | ${remote_url} | `Set Grid Server` | port=4444  | version=latest  | 
        | ${remote_url} | `Set Grid Server` | port=1234  | version=latest  |
        | ${remote_url} | `Set Grid Server` | port=4444  | version=gc:106.0.5249.61  |
        | ${remote_url} | `Set Grid Server` | port=4444  | version=ff:latest  |
        """
        try:
            requests.request("GET", 'http://localhost:%s/status' %(port), allow_redirects=True)
            server = 'http://localhost:%s/wd/hub'  %(port)
            return server
        except requests.exceptions.ConnectionError as e:
            if 'gc' in version:
                wdm.ChromeDriverManager(link_path=current_path).download_and_install(version=version[3:])
            elif 'ff' in version:
                wdm.GeckoDriverManager(link_path=current_path).download_and_install(version=version[3:])
            else:
                wdm.ChromeDriverManager(link_path=current_path).download_and_install()
                wdm.GeckoDriverManager(link_path=current_path).download_and_install()

            download_url = jdk.get_download_url('18', jre=True)
            responseJdk = requests.request("GET", download_url, allow_redirects=True)
            open('%s/OpenJDK.zip' %(current_path), 'wb').write(responseJdk.content)
            with zipfile.ZipFile('%s/OpenJDK.zip' %(current_path), 'r') as zip_ref:
                zip_ref.extractall(current_path)
            print('Dowlnload Completed')
            os.remove('%s/OpenJDK.zip' %(current_path))
            url = "https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.3.0/selenium-server-4.3.0.jar"
            response = requests.request("GET", url, allow_redirects=True)
            open('%s/selenium-server.jar' %(current_path), 'wb').write(response.content)
            check_file = glob.glob('%s/jdk*/bin' %(current_path))
            runserver = '%s/java -jar selenium-server.jar standalone --port %s' %(check_file[0].replace('\\', '/'), port)
            print(runserver)
            os.popen('cd %s && %s' %(current_path, runserver))
            while True:
                selenium_server_run = requests.request("GET", 'http://localhost:%s/status' %(port), allow_redirects=True)
                if selenium_server_run.status_code == 200:
                    server = 'http://localhost:%s/wd/hub'  %(port)
                    return server

    @keyword('Stop Grid Server')
    def stop_grid_server(self):
        """
        Stop by chromedriver, geckodriver, java(Selenium-Grid)
        """
        for process in psutil.process_iter():
            if 'chromedriver' in process.name() or 'geckodriver' in process.name() or 'java' in process.name():
                process.kill()

    @keyword('Clear Grid Server')
    def clear_grid_server(self):
        """
        remove by chromedriver, geckodriver, java(Selenium-Grid) for SeleniumGridServer
        """
        srt = glob.glob('%s/*' %(current_path))
        for i in srt:
            path_file = i.replace('\\', '/')
            if 'jdk-' in path_file or '__pycache__' in path_file:
                shutil.rmtree(path_file)  
            elif not '__init__.py' in path_file:
                os.remove(path_file)

