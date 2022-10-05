import cv2
import numpy as np

from face.src.face_detection import RetinaFace
from face.src.face_embedding import ArcFace
from face.src.landmark import Landmark
from tracking.src.byte_tracker import BYTETracker

retina = RetinaFace()
arc = ArcFace()
lan = Landmark()
bt = BYTETracker()

# img = cv2.imread('/media/vti/SSD/VTI/FaceMask/face_recognize_v2/5.png')
# boxes, kpss = retina.detect(img)

# for b,k in zip(boxes, kpss):
#     emb = arc.get(img, k)
#     print(emb)
#     l = lan.get(img, b)
#     print(l)

cap = cv2.VideoCapture('/home/vti/Downloads/v1.mp4')

while True:
    _, frame = cap.read()
    boxes,_ = retina.detect(frame)
    # boxes, ids = bt.predict(frame, boxes)
    for b in boxes:
        l = lan.get(frame, b)
        ag = lan.get_face_angle(frame, l)
        b = b[:4].astype(int)
        cv2.rectangle(frame, (b[0],b[1]), (b[2],b[3]), (0,255,0),thickness=2)
        cv2.putText(frame, '{:0.3f}'.format(ag), (b[0],b[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('asd', frame)
    cv2.waitKey(1)

    





