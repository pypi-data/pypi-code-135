import cv2
import numpy as np
import time

def find_detections(image, outputs, threshold=.85):
    bbox = []
    hT, wT, cT = image.shape
    for output in outputs:
        for box in output:
            # coco label 19 is cow, so we need index 24
            # because first five are bbox parameters
            score = box[24]
            if score >= threshold:
                w,h = int(box[2]*wT), int(box[3]*hT)
                x,y = int(box[0]*wT - w/2), int(box[1]*hT - h/2)
                bbox.append([x,y,w,h])
    return bbox

VIDEO_PATH = "Koeien - 44022.mp4"
IMAGE_PATH = "images/"
EXTENSION = ".jpg"
FREQUENCY = 1   # how often to take a snapshot in seconds
width, height = 320, 320

yolo = cv2.dnn.readNetFromDarknet("yolov3-spp.cfg", "yolov3-spp.weights")
yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


cap = cv2.VideoCapture(VIDEO_PATH)
while True: 
    #frame = cv2.imread("images/Koeien - 44022_0.jpg")
    ret, frame = cap.read()
    if not ret: break
    blob = cv2.dnn.blobFromImage(frame, 1/255, (width,height), [0,0,0], 1, crop=False)
    yolo.setInput(blob)

    layerNames = yolo.getLayerNames()
    outputNames = [layerNames[(i-1)] for i in yolo.getUnconnectedOutLayers()]
    
    outputs = yolo.forward(outputNames)
    detections = find_detections(frame, outputs)
    for box in detections:
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,255), 2)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cap.release()