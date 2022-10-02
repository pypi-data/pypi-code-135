# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:41:01 2022
图片来自萌娘百科
@author: Jinqk
"""
import requests
from PIL import Image
from io import BytesIO
import PySimpleGUI as sg
import time


def endpop():
    response = requests.get('https://pic1.imgdb.cn/item/63357deb16f2c2beb16d81ef.png')
    image = Image.open(BytesIO(response.content))
    image.save('./2.png')
    title = '安冬妮娜小助手'
    sg.popup_ok('已经算完了哦，可以下班了吧', title=title, keep_on_top=True, grab_anywhere=True, image='./2.png')


def stpop(mod=0):
    title = '安冬妮娜小助手'
    if mod == 1:
        # 银装初上
        response = requests.get('https://pic1.imgdb.cn/item/63392d7016f2c2beb1ccf22f.png')
        image = Image.open(BytesIO(response.content))
        image.save('./chris.png')
        sg.popup_ok('圣诞快乐，有什么事都可以来找安冬妮娜...什么的', title=title, keep_on_top=True, grab_anywhere=True,
                    image='./chris.png')
    elif mod == 2:
        # 最初口令
        response = requests.get('https://pic1.imgdb.cn/item/63395c7916f2c2beb103a238.png')
        image = Image.open(BytesIO(response.content))
        image.save('./start.png')
        sg.popup_ok('有什么事随时来找我，您的网络安全助手安冬妮娜竭诚为您服务~', title=title, keep_on_top=True,
                    grab_anywhere=True, image='./start.png')
    else:
        response = requests.get('https://pic1.imgdb.cn/item/63357deb16f2c2beb16d81f3.png')
        image = Image.open(BytesIO(response.content))
        image.save('./1.png')
        sg.popup_ok('又要上班了吗？', title=title, keep_on_top=True, grab_anywhere=True, image='./1.png')

def timestart():
    start = time.perf_counter()
    print("执行开始".center(50 // 2, "-"))
    dur = time.perf_counter() - start
    hour = dur // 3600
    minute = (dur - hour * 3600) // 60
    second = dur - hour * 3600 - minute * 60
    print("\r 安东尼娜小助手提醒您，总运行时间为{}h  {} min  {:.2f}s".format(hour, minute, second), end="")
    return start

def timedur(start,i=0,len = 0):
    dur = time.perf_counter() - start
    hour = dur // 3600
    minute = (dur - hour * 3600) // 60
    second = dur - hour * 3600 - minute * 60
    percent = (i+1)/len*100
    print("\r 安东尼娜小助手提醒您，目前已循环{}次，进度为{}%,总运行时间为{}h  {} min  {:.2f}s".format(i+1,percent,hour, minute, second), end="")
# if __name__ == '__main__':
#     main()
