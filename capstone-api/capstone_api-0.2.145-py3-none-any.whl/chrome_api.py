import re
import subprocess
import time
from configparser import ConfigParser
from pathlib import Path
from rich import print
from bs4 import BeautifulSoup
import re


class ChromeAPI(object):
    """Wrapper for chrome-cli"""

    def __init__(self, delay=0):
        """Configs"""
        if delay:
            self.delay = int(delay)
        else:
            capstone_api_ini = Path(Path.home(), '.config/capstone_api.ini')
            if capstone_api_ini.exists():
                config = ConfigParser()
                config.read(capstone_api_ini)
                chrome = dict(config["chrome"].items())
                self.delay = chrome["delay"]
            else:
                self.delay = 0

    def openTab(self, url):
        """Open url in new tab"""
        cmd = f'chrome-cli open "{url}"'
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        time.sleep(2)
        tab_info = {
            "tab_id": re.search(r'Id: (?P<tab_id>\d+)', out).groupdict().get('tab_id')
        }
        info.update(self.getInfo(tab_id=tab_id))
        return tab_info

    def getInfo(self, tab_id):
        """Get info of tab"""
        cmd = f"chrome-cli info -t {tab_id}"
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        info = {}
        for match in re.finditer(r"(?P<key>.+): (?P<val>.+)\n", out):
            key = match.groupdict().get("key")
            val = match.groupdict().get("val")
            if key == 'Id':
                info["tab_id"] = val
            if key == 'Window id':
                info["window_id"] = val
            if key == 'Url':
                info["url"] = val
            if key == 'Title':
                info["title"] = val
        return info

    def getSource(self, tab_id):
        """Get tab source"""
        cmd = f'chrome-cli source -t {tab_id}'
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        return BeautifulSoup(out, 'html5lib')

    def execJS(self, js, tab_id):
        """Execute JavaScript"""
        cmd = f'chrome-cli execute \'{js}\' -t {tab_id}'
        subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        # c.print(out)
        return

    def getTab(self, tab_id='', title=''):
        """Get a tab by ID or TITLE"""
        if tab_id:
            return self.getInfo(tab_id=tab_id)
        if title:
            tabs = self.getTabs()
            if isinstance(tabs, list):
                return next(filter(lambda x: x.get('title') == title, [tab for tab in tabs]), [])
            return next(filter(lambda x: x.get('title') == title, [tabs]), [])

    def getTabs(self):
        """Get all tabs"""
        cmd = f"chrome-cli list tabs"
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        tabs = []
        regex = rf'\[(\d+:)*(?P<tab_id>\d+)\] (?P<title>.*)'
        for match in re.finditer(regex, out):
            tab_id = match.groupdict().get("tab_id")
            # title = match.groupdict().get("title")
            tabs.append(self.getInfo(tab_id=tab_id))
        if len(tabs) == 1:
            return tabs[0]
        return tabs

    def findTabs(self, name="xTeVe"):
        """Find all tabs ending with keyword (name)"""
        cmd = f"chrome-cli list tabs"
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()

        # -- find open tabs showing xTeVe
        tabs = []
        regex = rf'\[(\d+:)*(?P<tab_id>\d+)\] (?:{name})'
        for match in re.finditer(regex, out):
            tab_id = match.groupdict().get("tab_id")
            tabs.append(self.getInfo(tab_id=tab_id)) # 3
        return tabs
