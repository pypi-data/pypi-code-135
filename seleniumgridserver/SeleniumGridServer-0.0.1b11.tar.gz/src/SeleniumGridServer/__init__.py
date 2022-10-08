# encoding: utf-8
import os
import psutil
import logging
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
    def set_grid_server(self, browser=None, version='latest'):
        """
        Examples:
        | ${remote_url} | `Set Grid Server` | browser=chrome or gc  | version=latest  | 
        | ${remote_url} | `Set Grid Server` | browser=firefox or ff   | version=106.0.5249.61  |
        | ${remote_url} | `Set Grid Server` | browser=edge   | version=106.0.1370.37  |
        | ${remote_url} | `Set Grid Server` | browser=safari   | version=latest  |
        """
        for process in psutil.process_iter():
            if 'chromedriver' in process.name() or 'geckodriver' in process.name() or 'msedgedrive' in process.name():
                process.kill()
        if browser != None:
            list_googlechrome = ['googlechrome', 'gc', 'chrome', 'headlesschrome']
            list_firefox = ['firefox', 'ff', 'headlessfirefox']
            list_edge = ['edge']
            list_safari= ['safari']
            if browser.lower() in list_googlechrome:
                wdm.ChromeDriverManager(link_path=current_path).download_and_install(version=version)
                os.environ['PATH'] += current_path        
                return current_path
            if browser.lower() in list_firefox:
                wdm.GeckoDriverManager(link_path=current_path).download_and_install(version=version)
                os.environ['PATH'] += current_path        
                return current_path
            if browser.lower() in list_edge:
                wdm.EdgeChromiumDriverManager(link_path=current_path).download_and_install(version=version)
                os.environ['PATH'] += current_path        
                return '%s/msedgedriver' %(current_path)
            if browser.lower() in list_safari:
                os.system('safaridriver --enable')
