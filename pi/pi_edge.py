#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time
import requests as re
import json 
import base64
import numpy as np
from picamera2 import Picamera2, Preview
import yaml
import cv2
import matplotlib.image as mpimg
import time
from PIL import Image


# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

with open("ip.txt", "r") as text_file:
    ip = text_file.read()
    print(ip)

#ip = "159.20.86.26"
#ip = "127.0.0.1"
picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()
time.sleep(2)
while True:    
    picam2.capture_file("tmp.jpg")
    time.sleep(0.2) 
    frame = cv2.imread('tmp.jpg')
    #do tiny yolo py

    print(np.fromstring(ts))
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)

    t_ids = class_ids.tostring()
    t_scores=scores.tostring()
    t_bboxes=bboxes.tostring()
    class_ids_string=np.fromstring(t_ids)
    scores_string=np.fromstring(t_scores)
    bboxes_string=np.fromstring(t_bboxes)
    print("is string :  ",type(class_ids_string))

    try:    
        print( re.post("http://"+ip+":5000/post_test", files={'image': open('tmp.jpg', 'rb')}) )    
        print( re.post("http://"+ip+":5000/post_test", files={'image': open('tmp.jpg', 'rb')}) )   
    except:
        print("Network Error") 
    


picam2.close()