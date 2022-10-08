# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadMODIS.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
 https://wiki.earthdata.nasa.gov/display/EDSC/Earthdata+Search+URL+Parameters
 https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/
'''
import os
import platform
import sys
import re
import numpy as np
import requests
from bs4 import BeautifulSoup

URL_LOGIN = 'https://urs.earthdata.nasa.gov/home'

# URL_ROOT = 'https://e4ftl01.cr.usgs.gov/'
URL_ROOT = ' https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/'

from lb_toolkits import bin
exedir = os.path.abspath(list(bin.__path__)[0])

WGET = os.path.join(exedir, 'wget.exe')
if not os.path.isfile(WGET) :
    raise Exception('wget is not command')

class downloadMODIS():

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.session = requests.Session()
        # self.login(username, password)

    def login(self, username, password):
        """Login to Earth Explorer."""
        rsp = self.session.get(URL_LOGIN)

        token = self.get_tokens(rsp.text)
        # payload= {
        #     "commit": "Sign in",
        #     "utf8":"✓",
        #     "authenticity_token":token,
        #     "login":username,
        #     "password":password
        # }
        payload= {
            "action": "login",
            "authenticity_token":token,
            "username":username,
            "password":password
        }
        rsp = self.session.post(URL_LOGIN, data=payload, allow_redirects=True)

        self.cookie = rsp.cookies.get_dict()
        return rsp

    def get_tokens(self, html):
        '''
        处理登录后页面的html
        :param html:
        :return: 获取csrftoken
        '''
        soup = BeautifulSoup(html,'lxml')
        res = soup.find("input",attrs={"name":"authenticity_token"})
        token = res["value"]
        return token

    def searchfile(self, nowdate, satid='TERRA', instid='MODIS',
                         version='61', prodid='MOD06_L2'):
        '''

        :param nowdate:
        :return:
        '''

        url = os.path.join(URL_ROOT, version, prodid,
                           nowdate.strftime('%Y'), '%03d.json' %(int(nowdate.strftime('%j'))))
        url = url.replace('\\', '/')

        res = self.session.get(url)
        for name in res.json() :
            print(name.get("name"))
        exit()

        res = self.session.get(url)

        soup = BeautifulSoup(res.text, 'lxml')
        r = soup.find_all(href=re.compile('.h5'))
        filelist = []
        for name in r :
            if name.get_text().endswith('.h5') :
                filelist.append(url + '/' + name.get_text())
        # print(filelist)

        return filelist

    def download(self, output_dir, url, timeout=5*60, skip=False):

        os.makedirs(output_dir, exist_ok=True)

        filename = self._download(output_dir, url, timeout=timeout, skip=skip)

        return filename

    def _download(self, output_dir, url, timeout, chunk_size=1024, skip=False):
        local_filename = os.path.basename(url)
        local_filename = os.path.join(output_dir, local_filename)
        if skip :
            return local_filename

        if platform.system().lower() == 'windows' :
            cmd = f'{WGET} {url} --tries=3 ' \
                  f'--http-user={self.username} ' \
                  f'--http-passwd={self.password} ' \
                  f'--timeout={timeout}' \
                  f'  -P {output_dir}'
        else:
            cmd = f'wget {url} --tries=3 ' \
                  f'--http-user={self.username} ' \
                  f'--http-passwd={self.password} ' \
                  f'--timeout={timeout}' \
                  f'  -P {output_dir}'
        print('Command : [%s]' %(cmd))
        os.system(cmd)

        return local_filename



def createshell():
    cmd = '''
    #!/bin/bash

    GREP_OPTIONS=''

    cookiejar=$(mktemp cookies.XXXXXXXXXX)
    netrc=$(mktemp netrc.XXXXXXXXXX)
    chmod 0600 "$cookiejar" "$netrc"
    function finish {
      rm -rf "$cookiejar" "$netrc"
    }
    
    trap finish EXIT
    WGETRC="$wgetrc"
    
    prompt_credentials() {
        echo "Enter your Earthdata Login or other provider supplied credentials"
        read -p "Username (cuitao): " username
        username=${username:-cuitao}
        read -s -p "Password: " password
        echo "machine urs.earthdata.nasa.gov login $username password $password" >> $netrc
        echo
    }
    
    exit_with_error() {
        echo
        echo "Unable to Retrieve Data"
        echo
        echo $1
        echo
        echo "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/270/MYD05_L2.A2022270.1745.061.2022271152044.hdf"
        echo
        exit 1
    }
    
    prompt_credentials
      detect_app_approval() {
        approved=`curl -s -b "$cookiejar" -c "$cookiejar" -L --max-redirs 5 --netrc-file "$netrc" https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/270/MYD05_L2.A2022270.1745.061.2022271152044.hdf -w %{http_code} | tail  -1`
        if [ "$approved" -ne "302" ]; then
            # User didn't approve the app. Direct users to approve the app in URS
            exit_with_error "Please ensure that you have authorized the remote application by visiting the link below "
        fi
    }
    
    setup_auth_curl() {
        # Firstly, check if it require URS authentication
        status=$(curl -s -z "$(date)" -w %{http_code} https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/270/MYD05_L2.A2022270.1745.061.2022271152044.hdf | tail -1)
        if [[ "$status" -ne "200" && "$status" -ne "304" ]]; then
            # URS authentication is required. Now further check if the application/remote service is approved.
            detect_app_approval
        fi
    }
    
    setup_auth_wget() {
        # The safest way to auth via curl is netrc. Note: there's no checking or feedback
        # if login is unsuccessful
        touch ~/.netrc
        chmod 0600 ~/.netrc
        credentials=$(grep 'machine urs.earthdata.nasa.gov' ~/.netrc)
        if [ -z "$credentials" ]; then
            cat "$netrc" >> ~/.netrc
        fi
    }
    
    fetch_urls() {
      if command -v curl >/dev/null 2>&1; then
          setup_auth_curl
          while read -r line; do
            # Get everything after the last '/'
            filename="${line##*/}"
    
            # Strip everything after '?'
            stripped_query_params="${filename%%\?*}"
    
            curl -f -b "$cookiejar" -c "$cookiejar" -L --netrc-file "$netrc" -g -o $stripped_query_params -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
          done;
      elif command -v wget >/dev/null 2>&1; then
          # We can't use wget to poke provider server to get info whether or not URS was integrated without download at least one of the files.
          echo
          echo "WARNING: Can't find curl, use wget instead."
          echo "WARNING: Script may not correctly identify Earthdata Login integrations."
          echo
          setup_auth_wget
          while read -r line; do
            # Get everything after the last '/'
            filename="${line##*/}"
    
            # Strip everything after '?'
            stripped_query_params="${filename%%\?*}"
    
            wget --load-cookies "$cookiejar" --save-cookies "$cookiejar" --output-document $stripped_query_params --keep-session-cookies -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
          done;
      else
          exit_with_error "Error: Could not find a command-line downloader.  Please install curl or wget"
      fi
    }
    
    fetch_urls <<'EDSCEOF'
    https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/270/MYD05_L2.A2022270.1745.061.2022271152044.hdf
    https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/270/MYD05_L2.A2022270.1925.061.2022271152124.hdf
    https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/271/MYD05_L2.A2022271.0625.061.2022271193516.hdf
    https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2022/271/MYD05_L2.A2022271.0940.061.2022271193547.hdf
    EDSCEOF
    '''

    print(cmd)

# 获取下载的cookie
def get_cookie(username,password):

    Base_URL = "https://urs.earthdata.nasa.gov/home"
    Login_URL = "https://urs.earthdata.nasa.gov/login"

    '''
    这里用于获取登录页的html，以及cookie
    :param url: https://urs.earthdata.nasa.gov/home
    :return: 登录页面的HTML,以及第一次的cooke
    '''
    html = requests.get(Base_URL)
    first_cookie = html.cookies.get_dict()
    print("first_cookie:",first_cookie)
    #return response.text,first_cookie

    '''
    处理登录后页面的html
    :param html:
    :return: 获取csrftoken
    '''
    soup = BeautifulSoup(html.text,'html.parser')
    res = soup.find("input",attrs={"name":"authenticity_token"})
    token = res["value"]
    print("token:",token)
    #return token

    '''
    这个是用于登录
    :param url: https://urs.earthdata.nasa.gov/login
    :param token: csrftoken
    :param cookie: 第一次登录时候的cookie
    :return: 返回第一次和第二次合并后的cooke
    '''

    data= {
        "commit": "Log in",
        "utf8":"✓",
        "authenticity_token":token,
        "username":username,
        "password":password
    }
    response = requests.post(Login_URL,data=data,cookies=first_cookie)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    #这里注释的解释一下，是因为之前是通过将两次的cookie进行合并的
    #现在不用了可以直接获取就行
    # cookie.update(second_cookie)
    print("cookie:",cookie)
    return cookie

def get_download_list(username, password, download_wait, save_path):

    download_list=[]   # 生成完整的下载链接，保存在download_list 列表中
    url="https://e4ftl01.cr.usgs.gov/MOLT/"
    # 获取下载链接列表
    for i in download_wait:
        download_url=url+i
        print(download_url)
        download_list.append(download_url)
    print(download_list)

    # 登录网址，获取cookie
    cookie=get_cookie(username,password)

    # 开始下载
    for p in download_list:
        os.chdir(save_path)
        save_name=p.split("/")[-1]
        print("正在下载：",save_name)
        r=requests.get(p,cookies=cookie)
        with open(save_name,"wb") as f:
            f.write(r.content)
        f.close()
        print("下载完成：",save_name)
