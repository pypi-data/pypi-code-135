# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import pyautogui

from Lshengpackage.simulate.pc.find_pic import screen_shot, find_image

pyautogui.FAILSAFE = True  # 设置自动防故障功能（将鼠标移动到左上角将停止程序）
pyautogui.PAUSE = 1


# 加载
def load(img):
    while True:
        screen_shot()
        iocn = find_image(img)
        if iocn is not None:
            return iocn
            


def load_click(img):
    while True:
        screen_shot()
        iocn = find_image(img)
        if iocn is not None:
            print(iocn)
            pyautogui.click(iocn[0], iocn[1])
            break


