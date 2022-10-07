from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui

class Screen:
    def __init__(self):
        self.name = 'Screen'
    def screenshot(self,filename=None):
        """Takes a screenshot of the screen when function is called.
        :param filename: Name of the file that screenshot should be written to (optional).
        
        :returns: screenshot"""
        myScreenshot = pyautogui.screenshot()
        if filename != None:
            
            myScreenshot.save(filename)

        return myScreenshot


    def Records(self,res:tuple = list(pyautogui.size())):
        
        width = res[0]
        height = res[1]
        
        img = ImageGrab.grab(bbox=(0,0,width,height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        return img_final
