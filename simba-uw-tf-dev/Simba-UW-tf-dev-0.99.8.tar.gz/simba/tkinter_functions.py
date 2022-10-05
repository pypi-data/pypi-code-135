__author__ = "Simon Nilsson", "JJ Choong"

import subprocess
import numpy as np
import os
import cv2
from os import listdir
from os.path import isfile, join
import yaml
from PIL import Image
import glob
import pathlib
import csv
import shutil
from datetime import datetime
import glob
import pandas as pd
from simba.extract_frames_fast import *
from simba.drop_bp_cords import get_fn_ext
from simba.features_scripts.unit_tests import read_video_info_csv

def archive_all_csvs(inifile,archivename):
    csv_dir = os.path.join(os.path.dirname(inifile),'csv')
    csv_subdir = []
    for i in os.listdir(csv_dir):
        folder = os.path.join(csv_dir,i)
        if os.path.isdir(folder):
            csv_subdir.append(folder)

    for i in csv_subdir:
        listtemp = []
        for j in os.listdir(i):
            if j.endswith('.csv'):
                csv_temp = os.path.join(i,j)
                listtemp.append(csv_temp)

        # create new folder
        if len(listtemp) != 0:
            dest1 = os.path.join(i,archivename)
            if not os.path.exists(dest1):
                os.mkdir(dest1)
        else:
            print('No csv to archive in',i)
            pass

        for i in listtemp:
            shutil.move(i,dest1)
            print(i,'archived')

    logPath = os.path.join(os.path.dirname(inifile), 'logs')
    VidInfoPath = os.path.join(logPath, 'video_info.csv')
    logArchivePath = os.path.join(logPath, archivename)
    if not os.path.exists(logArchivePath):
        os.mkdir(logArchivePath)
    try:
        shutil.move(VidInfoPath, logArchivePath)
        print('Video_info.csv file archived in project_folder/logs/ ' + str(archivename))
    except FileNotFoundError:
        pass


    videoPath = os.path.join(os.path.dirname(inifile), 'videos')
    videoPathList = [f for f in listdir(videoPath) if isfile(join(videoPath, f))]
    videoPathList = [videoPath + '/' + s for s in videoPathList]
    videoArchivePath = os.path.join(videoPath, archivename)
    if not os.path.exists(videoArchivePath):
        os.mkdir(videoArchivePath)
    for video in videoPathList:
        shutil.move(video, videoArchivePath)
    print('Video files archived in project_folder/videos/' + str(archivename))

    print('Archive completed.')


def batch_convert_videoformat(directory,format1,format2):
    filesFound = []
    format1 = '.'+format1
    for i in os.listdir(directory):
        if str(format1) in i:
            filesFound.append(i)

    def execute(command):
        subprocess.call(command, shell=True, stdout=subprocess.PIPE)

    ########### DEFINE COMMAND ###########
    for i in filesFound:
        currentFile = i
        outFile = currentFile.replace(format1, '.'+format2)
        outFile = str(outFile)
        output = os.path.basename(outFile)
        print('Converting video...')
        command = (str('ffmpeg -y -i ') + '"' + str(os.path.join(directory, currentFile) + '"' + ' -c:v libx264 -crf 5 -preset medium -c:a libmp3lame -b:a 320k '+'"' + str(os.path.join(directory, outFile) +'"')))

        execute(command)
        print('Video converted! ',output, ' created.')



def generategif(filename,starttime,duration,size):
    if starttime =='' or duration =='' or size =='':
        print('Please make sure all the boxes are filled before continue')
    elif filename != '' and filename != 'No file selected':
        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '.gif'
        output = os.path.basename(outFile)

        command = 'ffmpeg -ss ' + str(starttime) + ' -t ' + str(duration) + ' -i ' +'"'+ str(filename) +'"'+ ' -filter_complex "[0:v] fps=15,scale=w=' + str(size) + ':h=-1,split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" ' +'"'+ str(outFile)+'"'
        file = pathlib.Path(outFile)
        if file.exists():
            print(output,'already exist')
        else:
            print('Generating gif...')
            execute(command)
            print('Gif ', output, ' created.')
        return output

    else:
        print('Please select a video to start')


def downsamplevideo(width,height,filename):
    if width =='' or height == '':
        print('Please enter width and height to continue')
    elif filename != '' and filename !='No file selected':
        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile,fileformat = currentFile.split('.')
        outFile = str(outFile) + '_downsampled.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ')+'"' + str(currentFile)+'"' + ' -vf scale='+str(width)+':'+ str(height) + ' ' +'"'+ outFile +'"'+ ' -hide_banner')
        file = pathlib.Path(outFile)
        if file.exists():
            print(output,'already exist')
        else:
            print('Downsampling video...')
            execute(command)
            print('Video downsampled! ',output, 'created')
        return output

    else:
        print('Please select a video to downsample')

# def colorized(filename):
#
#     def execute(command):
#         print(command)
#         subprocess.call(command, shell=True, stdout = subprocess.PIPE)
#
#     ########### DEFINE COMMAND ###########
#
#     currentFile = filename
#     outFile = currentFile.replace('.mp4', '')
#     outFile = str(outFile) + '_colorized.mp4'
#     command = (str('python bw2color_video3.py --prototxt colorization_deploy_v2.prototxt --model colorization_release_v2.caffemodel --points pts_in_hull.npy --input ' )+ str(currentFile))
#     execute(command)

def shortenvideos1(filename,starttime,endtime):
    if starttime =='' or endtime =='':
        print('Please enter the time')

    elif filename != '' and filename != 'No file selected':

        def execute(command):
            subprocess.call(command, shell=True, stdout = subprocess.PIPE)

        ########### DEFINE COMMAND ###########

        currentFile = filename
        outFile, fileformat = currentFile.split('.')
        outFile = str(outFile) + '_clipped.mp4'
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ') +'"'+ str(currentFile) +'"'+ ' -ss ' + starttime + ' -to ' + endtime + ' -async 1 '+'"'+ outFile+'"')

        file = pathlib.Path(outFile)
        if file.exists():
            print(output, 'already exist')
        else:
            print('Clipping video....')
            execute(command)
            print(output,' generated!')
        return output


    else:
        print('Please select a video to trim')

def splitvideos(filename,varlist):

    def execute(command):
        subprocess.call(command, shell=True, stdout = subprocess.PIPE)

    startlist,stoplist = varlist[0],varlist[1]

    for i in range(len(startlist)):
        starttime = startlist[i].get()
        endtime = stoplist[i].get()

        currentFile = filename
        dir, outFile, fileformat = get_fn_ext(currentFile)
        outFile = os.path.join(dir,(str(outFile) + '_clip_' +str(i+1)+ '_' + '.mp4'))
        output = os.path.basename(outFile)

        command = (str('ffmpeg -i ') +'"'+ str(currentFile) +'"'+ ' -ss ' + starttime + ' -to ' + endtime + ' -async 1 '+'"'+ outFile+'"')

        file = pathlib.Path(outFile)

        if file.exists():
            print(output, 'already exist')
        else:
            print('Clipping video....')
            execute(command)
            print(output,' generated!')



def extract_allframescommand(filename):
    if filename:
        pathDir = str(filename[:-4])
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)
        video_to_frames(filename, pathDir, overwrite=True, every=1, chunk_size=1000)
        print('Frame extraction for ' + os.path.basename(filename) + ' complete')
        print('All frames are extracted!')
    else:
        print('Please select a video to convert')

def batch_extract_allframes(dir):
    curdir = os.listdir(dir)
    vid, vidEnding = [], []
    for i in curdir:
        if i.endswith(('.avi','.mp4')):
            vid.append(i)
            if i.endswith('.mp4'):
                vidEnding.append('mp4')
            if i.endswith('.avi'):
                vidEnding.append('avi')
    for index,i in enumerate(vid):
        vid[index]=os.path.join(dir,i)
    for videoName, videoFiletype in zip(vid, vidEnding):
        frames_dir = os.path.join(dir, os.path.basename(videoName).replace(videoFiletype, ''))
        if not os.path.exists(frames_dir):
            os.makedirs(frames_dir)
        video_to_frames(videoName, frames_dir, overwrite=True, every=1, chunk_size=1000)
        print('Frame extraction for ' + os.path.basename(videoName) + ' complete')
    print('All frames are extracted!')

def mergemovieffmpeg(directory,framespersec,vidformat,bit,imgformat):
    currDir = directory
    fps = str(framespersec)
    fileformat = str('.'+vidformat)
    bitrate = str(bit)
    imageformat = str(imgformat)

    currentDir = directory
    fileOut = str(directory)+ str(fileformat)
    currentDirPath = directory
    currentFileList = [f for f in listdir(currentDirPath) if isfile(join(currentDirPath, f))]
    imgPath = os.path.join(currentDirPath, currentFileList[0])
    img = cv2.imread(imgPath)
    print(imgPath)
    ffmpegFileName = os.path.join(currentDirPath, '%d.' + str(imageformat))
    imgShape = img.shape
    height = imgShape[0]
    width = imgShape[1]
    command = str('ffmpeg -r ' + str(fps) + str(' -f image2 -s ') + str(height) + 'x' + str(width) + ' -i ' +'"'+ str(ffmpegFileName)+'"' + ' -vcodec libx264 -b ' + str(bitrate) + 'k ' +'"'+ str(fileOut)+'"')
    print(command)
    subprocess.call(command, shell=True)

def mergemovebatch(dir,framespersec,vidformat,bit,imgformat):
    currDir = os.listdir(dir)
    fps = str(framespersec)
    fileformat = str('.' + vidformat)
    bitrate = str(bit)
    imageformat = str(imgformat)

    for i in currDir:
        directory = os.path.join(dir,i)
        fileOut = str(directory) + str(fileformat)
        currentDirPath = directory
        currentFileList = [f for f in listdir(currentDirPath) if isfile(join(currentDirPath, f))]
        imgPath = os.path.join(currentDirPath, currentFileList[0])
        img = cv2.imread(imgPath)
        print(imgPath)
        ffmpegFileName = os.path.join(currentDirPath, '%d.' + str(imageformat))
        imgShape = img.shape
        height = imgShape[0]
        width = imgShape[1]
        command = str('ffmpeg -r ' + str(fps) + str(' -f image2 -s ') + str(height) + 'x' + str(width) + ' -i ' +'"'+ str(
            ffmpegFileName) +'"'+ ' -vcodec libx264 -b ' + str(bitrate) + 'k ' +'"'+ str(fileOut)+'"')
        print(command)
        subprocess.call(command, shell=True)


# def rename(dir):
#     filename = os.listdir(dir)
#
#     os.chdir(dir)
#
#     for i in filename:
#         os.rename(i,i[2:])


def cropvid(filenames):
    if filenames:

        #extract one frame
        currentDir = str(os.path.dirname(filenames))
        videoName = str(os.path.basename(filenames))
        os.chdir(currentDir)
        cap = cv2.VideoCapture(videoName)
        cap.set(1, 0)
        ret, frame = cap.read()
        fileName = str(0) + str('.bmp')
        filePath = os.path.join(currentDir, fileName)
        cv2.imwrite(filePath, frame)
        #find ROI

        img = cv2.imread(filePath)
        cv2.namedWindow('Select ROI', cv2.WINDOW_NORMAL)
        ROI = cv2.selectROI("Select ROI", img)
        width = abs(ROI[0] - (ROI[2] + ROI[0]))
        height = abs(ROI[2] - (ROI[3] + ROI[2]))
        topLeftX = ROI[0]
        topLeftY = ROI[1]
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #crop video with ffmpeg
        fileOut, fileType = videoName.split(".", 2)
        fileOutName = str(fileOut) + str('_cropped.mp4')
        command = str('ffmpeg -i ') +'"'+ str(videoName) +'"'+ str(' -vf ') + str('"crop=') + str(width) + ':' + str(
            height) + ':' + str(topLeftX) + ':' + str(topLeftY) + '" ' + str('-c:v libx264 -crf 21 -c:a copy ') +'"'+ str(
            fileOutName)+'"'
        total = width + height + topLeftX + topLeftY

        file = pathlib.Path(fileOutName)
        if file.exists():
            print(os.path.basename(fileOutName), 'already exist')
        else:
            if width==0 and height ==0:
                print('Video not cropped')
            elif total != 0:
                print('Cropping video...')
                print(command)
                subprocess.call(command, shell=True)
                os.remove(filePath)
                print('Cropped video saved!')
                return fileOutName
            elif total ==0:
                print('Video not cropped')

        os.remove(filePath)

    else:
        print('Please select a video to crop')

def youOnlyCropOnce(inputdir,outputdir):
    filesFound=[]
    ########### FIND FILES ###########
    for i in os.listdir(inputdir):
        if i.endswith(('.avi', '.mp4', '.mov', 'flv')):
            filesFound.append(os.path.join(inputdir,i))
    filenames=filesFound[0]
    #extract one frame
    currentDir = str(os.path.dirname(filenames))
    videoName = str(os.path.basename(filenames))
    os.chdir(currentDir)
    cap = cv2.VideoCapture(videoName)
    cap.set(1, 0)
    ret, frame = cap.read()
    fileName = str(0) + str('.bmp')
    filePath = os.path.join(currentDir, fileName)
    cv2.imwrite(filePath, frame)
    #find ROI

    img = cv2.imread(filePath)
    cv2.namedWindow('Select ROI', cv2.WINDOW_NORMAL)
    ROI = cv2.selectROI("Select ROI", img)
    width = abs(ROI[0] - (ROI[2] + ROI[0]))
    height = abs(ROI[2] - (ROI[3] + ROI[2]))
    topLeftX = ROI[0]
    topLeftY = ROI[1]
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for i in filesFound:
        #crop video with ffmpeg
        fileOut, fileType = i.split(".", 2)
        fileOutName = os.path.join(outputdir, os.path.basename(str(fileOut)) + str('_cropped.') + str(fileType))


        command = str('ffmpeg -i ') +'"'+ str(i) +'"'+ str(' -vf ') + str('"crop=') + str(width) + ':' + str(
            height) + ':' + str(topLeftX) + ':' + str(topLeftY) + '" ' + str('-c:v libx264 -crf 21 -c:a copy ') +'"'+ str(
            fileOutName)+'"'
        total = width + height + topLeftX + topLeftY

        file = pathlib.Path(fileOutName)
        if file.exists():
            print(os.path.basename(fileOutName), 'already exist')
        else:
            if width==0 and height ==0:
                print('Video not cropped')
            elif total != 0:
                print('Cropping video...')
                print(command)
                subprocess.call(command, shell=True)
            elif total ==0:
                print('Video not cropped')

    os.remove(filePath)
    print('Process completed.')


def changedlc_config(config_path, bodyPartConfigFile):

    config_path = config_path

    if bodyPartConfigFile == 0:
        with open(config_path) as f:
            read_yaml = yaml.load(f)

        read_yaml["bodyparts"] = ['Ear_left_1',
                                  'Ear_right_1',
                                  'Nose_1',
                                  'Center_1',
                                  'Lateral_left_1',
                                  'Lateral_right_1',
                                  'Tail_base_1',
                                  'Tail_end_1',
                                  'Ear_left_2',
                                  'Ear_right_2',
                                  'Nose_2',
                                  'Center_2',
                                  'Lateral_left_2',
                                  'Lateral_right_2',
                                  'Tail_base_2',
                                  'Tail_end_2']

        with open(config_path, 'w') as outfile:
            yaml.dump(read_yaml, outfile, default_flow_style=False)

    if (type(bodyPartConfigFile) == str):
        if os.path.exists(bodyPartConfigFile):
            print(bodyPartConfigFile)
            with open(bodyPartConfigFile, "r", encoding='utf8') as f:
                cr = csv.reader(f, delimiter=",")  # , is default
                rows = list(cr)  # create a list of rows for instance
            rows = [i[0] for i in rows]
            print(rows)
            with open(config_path) as d:
                read_yaml = yaml.load(d)
            print(rows)
            read_yaml["bodyparts"] = rows
            with open(config_path, 'w') as outfile:
                yaml.dump(read_yaml, outfile, default_flow_style=False)
        else:
            print('Not a valid body part file')