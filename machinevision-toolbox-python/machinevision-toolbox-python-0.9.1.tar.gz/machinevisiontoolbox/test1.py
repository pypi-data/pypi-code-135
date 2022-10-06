import numpy as np
from machinevisiontoolbox import *
import cv2
from pathlib import Path

# path = '/Users/corkep/Dropbox/code/machinevision-toolbox-python/machinevisiontoolbox/images/traffic_sequence.mpg'
# cap = cv2.VideoCapture(path)

# while(cap.isOpened()):
#     ret, frame = cap.read()

#     if not ret:
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# # When everything done, release the capture
# # print(dir(cap))

# cap.release()
# cv2.destroyAllWindows()



img = Image.Read('monalisa.png', grey=False)
print(img)

img.disp()

# # INTER_AREA for shrinking, specify cubic,linear,area but choose default for
# # shrink/reduce
res = cv2.resize(img.image,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# cols = img.width
# rows = img.height

# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,2)
# res = cv2.warpAffine(img.image,M,(cols,rows))

im2 = Image(res, colororder=img.colororder)

im2.disp(block=True)

# o=np.ones((2,2))                                                                                                                                

# a=np.dstack((o, 2*o, 3*o))
# a.reshape((-1,3))

# from matplotlib import pyplot as plt
  
  
# # find frequency of pixels in range 0-255
# histr = cv2.calcHist([img.image],[0],None,[256],[0,256])
# print(type(histr), histr.shape)
# # show the plotting graph of an image
# plt.plot(histr)
# plt.show(block=True)