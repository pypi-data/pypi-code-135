# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadOCO.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import datetime
import os
import platform
import sys
import re
import numpy as np
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

LOGIN_URL = 'https://urs.earthdata.nasa.gov/home'

URL_ROOT = 'https://oco2.gesdisc.eosdis.nasa.gov/data'


from lb_toolkits import bin
exedir = os.path.abspath(list(bin.__path__)[0])

WGET = os.path.join(exedir, 'wget.exe')
if not os.path.isfile(WGET) :
    raise Exception('wget is not command')

class downloadOCO():

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.session = requests.Session()
        # self.login(username, password)

    def login(self, username, password):
        """Login to Earth Explorer."""
        rsp = self.session.get(LOGIN_URL)

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
        rsp = self.session.post(LOGIN_URL, data=payload, allow_redirects=True)

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

    def searchfile(self, starttime, endtime=None, satid='OCO2_DATA',
                   prodversion='OCO2_L2_Standard.10r', pattern='.h5'):
        '''

        Parameters
        ----------
        starttime
        endtime
        satid
        prodversion

        Returns
        -------

        '''

        nowdate = starttime

        if endtime is None :
            endtime = starttime

        filelist = []
        while nowdate <= endtime :

            # https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Standard.10r/2021/
            url = os.path.join(URL_ROOT, satid, prodversion,
                               nowdate.strftime('%Y'), nowdate.strftime('%j'))
            nowdate += datetime.timedelta(days=1)
            url = url.replace('\\', '/')
            print(url)
            res = self.session.get(url)

            soup = BeautifulSoup(res.text, 'lxml')
            r = soup.find_all(href=re.compile(pattern))

            for name in r :
                if name.get_text().endswith(pattern) :
                    filelist.append(url + '/' + name.get_text())
        # print(filelist)

        return filelist

    def download(self, output_dir, url, timeout=5*60, skip=False):
        '''
        根据输入url下载相应的文件

        Args:
            output_dir: str, 输出路径
            url: str, 下载链接
            timeout: int
                时间限制
            skip: bool
                是否不做数据下载，直接返回文件名。默认是FALSE，下载文件。

        Returns: str
            下载数据的文件名
        '''
        if not  os.path.isdir(output_dir) :
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

        #  暂未实现爬虫方式下载，只能通过wget方式下载文件
        download_url = url
        try:
            with self.session.get(
                    download_url, stream=True, allow_redirects=True, timeout=timeout
            ) as r:
                headers = r.headers

                file_size = int(r.headers.get("Content-Length"))
                with tqdm(
                        total=file_size, unit_scale=True, unit="B", unit_divisor=1024
                ) as pbar:
                    local_filename = os.path.basename(download_url)
                    local_filename = os.path.join(output_dir, local_filename)
                    if skip:
                        return local_filename
                    with open(local_filename, "wb") as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                                pbar.update(chunk_size)
        except requests.exceptions.Timeout:
            raise Exception(
                "Connection timeout after {} seconds.".format(timeout)
            )
        print('download 【%s】 success...' %(local_filename))

        return local_filename