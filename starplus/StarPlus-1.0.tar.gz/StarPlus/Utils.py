import time
import cv2
import numpy as np
import requests

class Utils:
    """
    Some Functions you might need.
    """

    def __init__(self):
        self.pTime = time.time()

    def fps(self, img=None, pos=(20, 50), color=(255, 0, 0), scale=3, thickness=3):
        """
        
        :param img: Image to put FPS value on.(optional)
        :param pos: Position on the FPS on the image
        :param color: Color of the FPS Value displayed
        :param scale: Scale of the FPS Value displayed
        :param thickness: Thickness of the FPS Value displayed
        :return: FPS,Image(if passed in)
        """
        cTime = time.time()
        try:
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            if img is None:
                return fps
            else:
                cv2.putText(img, f'FPS: {int(fps)}', pos, cv2.FONT_HERSHEY_PLAIN,
                            scale, color, thickness)
                return fps, img
        except:
            return 0

    def GetVideoDuration(video):
        """Gets the duration of the given video
        :param video: can only be a video.

        """
        cap = cv2.VideoCapture(video)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps
        return duration%60
  

    



    def stackimages(img1,img2,mode):

        """stacks 2 images 
            img1 first image
            img2 second image
            :param mode: value 1 returns vertical img
            :param mode: value 0 returns horizontal img
            :param mode: value 2 returns vertical and horizontal img"""

            

        img1 = cv2.resize(img1,(640,480))
        img1 = cv2.resize(img1,(640,480))

        

        img1 = cv2.resize(img1,(0,0),None,0.5,0.5)
        img2 = cv2.resize(img2,(0,0),None,0.5,0.5)

        hor = np.hstack((img1,img2))
        ver = np.vstack((img1,img2))

        if mode == 1:
            return ver
        
        if mode == 0:
            return hor
        if mode == 2:
            return ver , hor
        

    def getfeed(ip):
        """Returns the camera from IPWebCam mobile app
        :param ip: ip and port from IPWebCam mobile app
        use in a while loop"""
        url = f"http://{ip}/shot.jpg"
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)

        return img
