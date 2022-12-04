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
def tiny(img):
    frame = cv2.imread(img)
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    

    class_ids_strin=','.join(str(x) for x in class_ids)
    if(class_ids_strin==""):
        return "none"
    return class_ids_strin

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
picture_index=0
time.sleep(2)
while True:    
    picam2.capture_file("tmp.jpg")
    time.sleep(5) 
    id2=tiny("tmp.jpg")
    #do tiny yolo py

    
    

    try:    

        time.sleep(2)   
        returned_img= re.post("http://"+ip+":5000/end_point_1a", files={'image': open('tmp.jpg', 'rb')}) 
        this_img_name= 'pics/tmps'+str(picture_index)+'.jpg'
        with open(this_img_name, 'wb') as f:
            f.write(returned_img.content)
        picture_index+=1
        """rimg = base64.b64decode(returned_img.text)
        this_img_name= 'pics/tmp'+str(picture_index)+'.jpg'
        rimg.save(this_img_name)"""
        picture_index=picture_index+1
        print( re.post("http://"+ip+":5000/end_point_1b", files={'image': open('tmp.jpg', 'rb')}) ) 
        print( re.post("http://"+ip+":5000/end_point_2", json={'class': id2}) )

           
    except Exception as e :
        print("Network Error",e) 
    


picam2.close()