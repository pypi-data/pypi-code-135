#!/usr/bin/env python3

import glob
import os
import sys
from typing import Tuple
from typing import Union


import matplotlib.pyplot as plt  # matplotlib.pyplot module for plotting
import matplotlib.figure as figure
import numpy as np
import pandas as pd

def test():
    """print 'ok' to console (to check if file is included correctly).
    """
    print('ok')


def print_to_txt(list: list):
    """writing list to file 'output.txt'.

    Args:
        list (list): values to be written in txt file.
    """
    fullpath = r'programs/output.txt'
    with open(fullpath, "w") as f:
        for i in list:
            f.writelines(f"%s\n" % i)


def linearFunction(x: Union[float,list[float]], slope: float, intercept: float) -> Union[float,list[float]]:
    """get solution for function: a*x + b.

    Args:
        x (Union[float,list[float]]): input for function as value or list.
        slope (float): slope of function (value a).
        intercept (float): intercept of function (value b).

    Returns:
        Union[float,list[float]]: solution of function.
    """
    return slope * x + intercept


def read_lookup(folder: list[str]) -> list[float]:
    """get delta of Force for measurements of specific day/folder.

    Args:
        folder (list[str]): folder which contains measurement files.

    Returns:
        list[float]: delta of force in list.
    """
    lookupTable = pd.read_csv(os.path.abspath('data/deltaF_lookupTable.csv'), sep=',', header=None) 
    deltaF = []
    for i in folder:
        temp = False
        for j in range(len(lookupTable[0])):
            if i == lookupTable[0][j]:
                deltaF.append(lookupTable[1][j])
                temp = True
        if temp != True:
            deltaF.append(0)
    return deltaF


def getFiles(folder: str) -> Tuple[list[str],list[str]]:
    """get all file locations and their names in specified folder.

    Args:
        folder (str): folder where files are (not the path).

    Returns:
        Tuple[list[str],list[str]]: path of files and filenames.
    """
    file_names = []
    temp = 'data/' + folder + '/*.csv'
    location = os.path.abspath(temp)
    files = (glob.glob(location))
    for file in files:
        start = file.find(folder)
        if os.name == 'posix':
            start = start + len(folder)+2
        elif os.name == 'nt':
            start = start + len(folder)+2
        end = file[start:].find("'")+start
        file_names.append(file[start:end])
    return files, file_names


def primeData(data: pd.DataFrame, deltaF: float=0) -> pd.DataFrame:
    """prime data for later calculations.
    name columns.
    remove data with idx=-1.
    adding delta of Force.<
    
    Args:
        data (pd.DataFrame): pandas DataFrame to prime.
        deltaF (float, optional): delta of force to add to data. Defaults to 0.

    Returns:
        pd.DataFrame: primed pandas DataFrame.
    """
    temp = data.copy()
    temp.columns = ['idx', 'x', 'y', 'F', 'z', 'debug1', 'debug2']
    temp = temp[temp['idx'] != -1.0]
    temp['F'] = temp.F + deltaF
    temp.reset_index(drop=True, inplace=True)
    return temp


def prepData_old(data: pd.DataFrame) -> pd.DataFrame:
    """prepare data recorded with old software fore later calculations.
    remove all data with positive z.
    change all z from negative to positive.
    scaling up F-values to compensate sensor error.
    
    Args:
        data (pd.DataFrame): pandas DataFrame to prepare.

    Returns:
        pd.DataFrame: prepared pandas DataFrame.
    """
    temp = data.copy()
    temp = primeData(temp)
    temp = temp[temp['z'] <= 0]
    temp.reset_index(drop=True, inplace=True)
    temp['z'] = temp.z * -1
    temp['F'] = temp.F * 1.109               #scaling up F-values to compensate sensor error
    return temp


def prepData(data: pd.DataFrame) -> pd.DataFrame:
    """prepare data recorded with new software fore later calculations.
    change start of data => F=0 is on z=0 to ignore plastic deformation.
    remove all negative z values.
    scaling up F-values to compensate sensor error.
    
    Args:
        data (pd.DataFrame): pandas DataFrame to prepare.

    Returns:
        pd.DataFrame: prepared pandas DataFrame.
    """
    temp = data.copy()
    start = temp[temp.F>=0].index.values
    for i in start:
        if i < 5: continue
        elif temp.F[i-5] <temp.F[i]:
            start = i
            break
    start = temp.z[start]
    temp['z'] = (temp.z -start) *(-1)
    #temp['z'] = temp.z*(-1)
    temp['F'] = temp.F * 1.109               #scaling up F-values to compensate sensor error
    temp = temp[temp.z >= 0]
    temp.reset_index(drop=True, inplace=True)
    return temp


def split_data(data: pd.DataFrame, version: str='new') -> list[pd.DataFrame]:
    """split data into single measurements.
    extracted by idx in DataFrame, so at least two measured points needed in each file.
    
    Args:
        data (pd.DataFrame): pandas DataFrame to split.
        version (str, optional): version of software with which data das recorded. Defaults to 'new'.

    Returns:
        list[pd.DataFrame]: list of individual pandas DataFrames for for each measurement.
    """
    firstItem = 0   #to remember where data was split
    df = [] #list for splitted DataFrames
    for i in range(len(data)):  #split data into one dataFrame per measurement
        if i+1 == len(data):
            temp = data[firstItem:].copy()
            temp.reset_index(drop=True, inplace=True)
            df.append(temp)
        elif data['idx'][i+1] != data['idx'][i]:
            temp = data[firstItem:i+1].copy()
            temp.reset_index(drop=True, inplace=True)
            df.append(temp)
            firstItem = i+1
    data = df
    df = []
    for i in data:
        if version == 'old': df.append(prepData_old(i))
        else: df.append(prepData(i))
    return df


def reduce_size(data: list[pd.DataFrame], samples: int=100) -> np.ndarray:
    """reduce size of lists of pandas DataFrame and return only force.

    Args:
        data (list[pd.DataFrame]): list of pandas DataFrames.
        samples (int, optional): size to reduce data to. Defaults to 100.

    Returns:
        np.ndarray: Force in n samples
    """
    F = np.zeros((len(data),samples))
    for i in range(len(data)):
        idx = 0
        for j in range(samples):
            temp = []
            while data[i]['z'][idx] < j/(samples/10) and not idx == len(data[i])-1:
                temp.append(data[i]['F'][idx])
                idx +=1
            if not len(temp) == 0:
                F[i,j] = np.mean(temp)
    return F


def get_spring_force(F: np.ndarray[float]) -> Tuple[float,float]:
    """calculate mean and standard deviation of given force.

    Args:
        F (np.ndarray[float]): given force.

    Returns:
        Tuple[float,float]: mean and standard deviation of force.
    """
    mean = np.mean(F,axis=0)
    std = np.std(F,axis=0)
    return mean, std


def get_spring_rate(F: np.ndarray[float]) -> Tuple[float,float]:
    """calculate spring rate mean and standard deviation of given force.

    Args:
        F (np.ndarray[float]): given force.

    Returns:
        Tuple[float,float]: mean and standard deviation of spring rate.
    """
    R = np.zeros(F.shape[0])
    step = int(F.shape[1]/10)
    s1 = 1
    s2 = 9
    for i in range(R.size):
        F1 = F[i,s1*step]
        F2 = F[i,s2*step]
        R[i] = (F2-F1) / (s2-s1)
    mean = np.mean(R)
    std = np.std(R)
    return mean, std


def get_mean_std(folder: list,spring_list: list, samples: int) -> Tuple[list[float],list[float],list[float],list[float]]:
    """calculate mean and standard deviation of spring force and rate for measurements in list of springs that are located in specified folders.

    Args:
        folder (list): folders to look for files.
        spring_list (list): list of measurements for spring types to calculate.
        samples (int): n samples for compressing data.

    Returns:
        Tuple[list[float],list[float],list[float],list[float]]: mean and standard deviation of spring force and rate.
    """
    Force_mean=[]
    Force_std=[]
    Rate_mean =[]
    Rate_std = []
    version = []
    files = []
    file_names = []
    deltaF = read_lookup(folder)
    for i in folder:
        if i[:3] == 'old':
            version.append('old')
        else:
            version.append('new')
        temp1, temp2 = getFiles(i)
        files.append(temp1)
        file_names.append(temp2)
    for i in spring_list:
        data = []
        temp = True
        verify_version = []
        for f in range(len(files)):
            li = [k for k, x in enumerate(file_names[f]) if x == i]
            for k in li:
                tempDF = pd.read_csv(files[f][k], sep=',', header=None)
                tempDF = primeData(tempDF,deltaF[f])
                data.append(tempDF)
                verify_version.append(version[f])
        data = pd.concat(data)
        for i in range(len(verify_version)-1):
            if verify_version[i] != verify_version [i+1]:
                temp = False
        if temp == False:
            sys.exit('Versions do not match!')
        data = primeData(data)
        data = split_data(data, verify_version[0])
        data = reduce_size(data,samples)
        temp1,temp2 = get_spring_force(data)
        Force_mean.append(temp1)
        Force_std.append(temp2)
        temp1,temp2 = get_spring_rate(data)
        Rate_mean.append(temp1)
        Rate_std.append(temp2)
    return Force_mean, Force_std, Rate_mean, Rate_std


def getValues_from_namelist(list: list[str]) -> Tuple[list[float],list[float],list[float]]:
    """get Values from list of names.
    values to get: coil diameter D, coil number n, wire diameter d.
    
    Args:
        list (list[str]): list of names of springs to extract values from.

    Returns:
        Tuple[list[float],list[float],list[float]]: coil diameter D, coil number n, wire diameter d.
    """
    D = []
    n = []
    d = []
    for name in list:
        D.append(name[1:3])
        n.append(name[5:7])
        d.append(name[9:11])
    return D, n, d


'''
old functions:

def getFiles_old(folder: str|list[str]) -> Tuple[list,list]:
    folder = folder.copy()
    if type(folder) == type(' '): folder = [folder,'']
    else: folder.append('')
    folder_array = np.array(folder)
    files = []
    file_names = []
    for i in range(folder_array.size-1):
        name_of_file = []
        temp = 'data/' + folder_array[i] + '/*.csv'
        location = os.path.abspath(temp)
        file_list = (glob.glob(location))
        for file in file_list:
            start = file.find(folder_array[i])
            if os.name == 'posix':
                start = start + len(folder_array[i])+2
            elif os.name == 'nt':
                start = start + len(folder_array[i])+3
            end = file[start:].find("'")+start
            name_of_file.append(file[start:end])
        files.append([x for _,x in sorted(zip(name_of_file,file_list))])
        file_names = sorted(name_of_file)
        if i > 0:
            if len(files[i-1]) != len(files[i]):
                sys.exit('files not matching')
    if(len(files))==1:
        temp = []
        for i in files[0]:
            temp.append(i)
        files = temp
    return files, file_names

def createPlot(fig: figure.Figure,data: list[float] = -1,linReg: Tuple[float,float] = -1,**kwargs) -> figure.Figure:
    if not 'mode' in kwargs or kwargs.get('mode') == 'plot':
        if type(data[0]) == type([]):
            for i in range(len(data)):
                plt.plot(data[i][0],data[i][1],label=i+1)
        else: plt.plot(data[0],data[1])
    elif kwargs.get('mode') == 'scatter':
        if type(data[0]) == type([]):
            for i in range(len(data)):
                plt.scatter(data[i][0],data[i][1],label=i+1,linewidths=0, marker='.')
        else: plt.scatter(data[0],data[1],linewidths=0, marker='.')
    
    if linReg != -1:
        x = np.linspace(0,10)
        y = linearFunction(x,linReg[0],linReg[1])
        plt.plot(x,y,label='lin')
    if kwargs.get('legend') == True:
        plt.legend()
    plt.xlabel('z [mm]')
    plt.ylabel('F [N]')
    if 'name' in kwargs:
        plt.title(kwargs.get('name'))
    return fig
'''