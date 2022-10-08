# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadH8.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import os
import sys
import datetime
import time

from lb_toolkits.tools import ftppro
from lb_toolkits.tools import writejson

# /jma/netcdf/202103/30
# NC_H08_20210330_0210_R21_FLDK.02401_02401.nc
# NC_H08_20210330_0200_R21_FLDK.06001_06001.nc
FTPHOST='ftp.ptree.jaxa.jp'

class downh8file(object):

    def __init__(self, username, password):

        self.ftp = ftppro(FTPHOST, username, password)


    def download_ahi8_l1_netcdf(self, nowdate, dstpath, okpath=None, pattern=['02401','06001'], skip=False):
        '''
        下载葵花8号卫星L1 NetCDF数据文件
        # Available Himawari  L1 Gridded Data

        ## Full-disk
         Projection: EQR
         Observation area: 60S-60N, 80E-160W
         Temporal resolution: 10-minutes
         Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)
                             2km (Pixel number: 6001, Line number: 6001)
         Data: albedo(reflectance*cos(SOZ) of band01~band06)
               Brightness temperature of band07~band16
               satellite zenith angle, satellite azimuth angle,
               solar zenith angle, solar azimuth angle, observation hours (UT)

        ## Japan Area
         Projection: EQR
         Observation area: 24N-50N, 123E-150E
         Temporal resolution: 10-minutes
         Spatial resolution: 1km (Pixel number: 2701, Line number: 2601)
         Data: albedo(reflectance*cos(SOZ) of band01~band06)
               Brightness temperature of band07, 14, 15
               satellite zenith angle, satellite azimuth angle,
               solar zenith angle, solar azimuth angle, observation hours (UT)

        Parameters
        ----------
        nowdate : datetime
            下载所需数据的时间
        dstpath: str
            输出路径
        okpath: str, optional
            OK文件输出路径，是否输出下载完成标志OK文件
        pattern: list, optional
            模糊匹配参数
        Returns
        -------
            list
            下载的文件列表
        '''

        # 拼接H8 ftp 目录
        sourceRoot = os.path.join('/jma/netcdf', nowdate.strftime("%Y%m"), nowdate.strftime("%d"))
        sourceRoot = sourceRoot.replace('\\','/')

        return self._download_ahi8_l1(nowdate, sourceRoot, dstpath, okpath, pattern, skip=skip)

    def download_ahi8_l1_hsd(self, nowdate, dstpath, okpath=None, pattern=None, skip=False):
        '''
        # Available Himawari Standard Data

        ## Full-disk
         Observation area: Full-disk
         Temporal resolution: 10-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Japan Area
         Observation area: Japan area (Region 1 & 2)
         Temporal resolution: 2.5-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Target Area
         Observation area: Target area (Region 3)
         Temporal resolution: 2.5-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Color Image Data
         png images of Full-disk, Japan area and Target area, compositing three visible
         bands (blue: 0.47 micron; green: 0.51 micron; red: 0.64 micron).
        :param nowdate: datetime, 文件名中的时间（UTC）
        :param dstpath: 存储数据文件目录
        :param okpath: 输出OK文件路径
        :param pattern: 模糊匹配文件名
        :return:
        '''
        # 拼接H8 ftp 目录
        '''
        # Structure of FTP Directories

         /jma/hsd
               +---/[YYYYMM]
                      +---/[DD]
                             +---/[hh]
        
         where YYYY: 4-digit year of observation start time (timeline);
               MM: 2-digit month of timeline;
               DD: 2-digit day of timeline; and
               hh: 2-digit hour of timeline.
        '''
        sourceRoot = os.path.join('/jma/hsd',
                                  nowdate.strftime("%Y%m"),
                                  nowdate.strftime("%d"),
                                  nowdate.strftime("%H"))
        sourceRoot = sourceRoot.replace('\\','/')

        return self._download_ahi8_l1(nowdate, sourceRoot, dstpath, okpath, pattern, skip=skip)

    def _download_ahi8_l1(self, nowdate, sourceRoot, dstpath, okpath=None, pattern=None, skip=False):
        """通过ftp接口下载H8 L1数据文件"""
        dstfilelist = []

        # 获取文件列表
        self.files = self.GetFileList(nowdate, sourceRoot, pattern)
        if len(self.files) == 0 :
            print('Not Match the file')
            return dstfilelist

        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
            print('create dir <{0}> success !'.format(dstpath))

        if okpath is not None :
            if not os.path.exists(okpath) :
                os.makedirs(okpath)
                print('create dir <{0}> success !'.format(okpath))

        count = len(self.files)
        for srcname in self.files:
            print('='*100)
            count -= 1
            basename = os.path.basename(srcname)
            dstname = os.path.join(dstpath, basename)

            dstfilelist.append(dstname)
            if skip :
                continue
            # if os.path.isfile(dstname) :
            #     print('%s is exist, will continue...' %(dstname))
            #     continue

            downinfo = {}

            downinfo['srcname'] = srcname
            downinfo['dstname'] = dstname

            stime = time.time()
            print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                  '开始下载文件【%d】: %s'%(count, srcname))

            downinfo['starttime'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            if self.ftp.downloadFile(srcname, dstpath):
                downinfo['endtime'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                downinfo['status'] = 0

                if okpath is not None :
                    okname = os.path.join(okpath, basename + '.OK')
                    downinfo['okname'] = okname
                    self.writeok(okname, downinfo)
                print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                      '成功下载文件【%s】:%s' %(count, dstname))

            etime = time.time()
            print('cost %.2f sec...' %(etime - stime))

        return dstfilelist

    def GetFileList(self, nowdate, srcpath, pattern=None):
        '''
        根据输入时间，匹配获取H8 L1数据文件名
        Parameters
        ----------
        nowdate
        srcpath
        pattern

        Returns
        -------

        '''
        downfiles = []

        srcpath = srcpath.replace('\\', '/')

        files = self.ftp.listdir(srcpath)
        files.sort()
        for file in files :
            strtime = nowdate.strftime('%Y%m%d_%H')
            downflag = True
            if not strtime in file :        # 匹配对应时间，精确到小时级
                continue

            # 根据传入的匹配参数，匹配文件名中是否包含相应的字符串
            if pattern is not None :
                if isinstance(pattern, list) :
                    for item in pattern :
                        if item in file :
                            downflag = True
                            break
                        else:
                            downflag = False
                elif isinstance(pattern, str) :
                    if item in file :
                        downflag = True
                    else:
                        downflag = False

            if downflag :
                srcname = os.path.join(srcpath, file)
                srcname = srcname.replace('\\','/')

                downfiles.append(srcname)

        return downfiles

    def writeok(self, okname, info):

        writejson(okname, info)

    def _download(self, srcfile, dstfile, blocksize=5*1024, skip=True):
        ftp = self.ftp.connect()
        if ftp is None :
            return False

        srcsize = ftp.size(srcfile)
        if skip :
            if os.path.isfile(dstfile) :
                dstsize = os.path.getsize(dstfile)
        else:
            dstsize = 0

        if srcsize <= dstsize :
            return

        conn = ftp.transfercmd('RETR ' + srcfile, srcsize)

        with open(dstfile, 'ab') as fp :
            while True :
                data = conn.recv(blocksize)
                if not data :
                    break

                fp.write(data)

        self.ftp.close(ftp)

