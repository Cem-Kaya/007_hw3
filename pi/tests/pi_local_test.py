#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.
import numpy as np
import time
import requests as re
import json 
import base64
import matplotlib.image as mpimg
import time

from PIL import Image
#from picamera2 import Picamera2, Preview
import yaml
import cv2
# Opencv DNN
def tiny(img):
    frame = cv2.imread(img)
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    

    class_ids_strin=','.join(str(x) for x in class_ids)
    if(class_ids_strin==""):
        return "none"
    return class_ids_strin
    
def convertTuple(tup):
        # initialize an empty string
    str = ''
    print("tup is", tup)
    a=tup.astype(str)
    for count,item in enumerate(a):
     
        print("item is : ",type(item))
        str = str + str(item)
    return str
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

"""with open("conf.yml", "r") as stream:
    try:
        ips =yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)"""
    


ip = "127.0.0.1"

#picam2 = Picamera2()

#preview_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
#picam2.configure(preview_config)

#picam2.start_preview(Preview.QTGL)

#picam2.start()
time.sleep(2)
picture_index=0
while True:    
    #picam2.capture_file("tmp.jpg")
    time.sleep(2) 
    frame = cv2.imread('doritos_man.jpg')
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    f = open("file_tiny.txt", "r")

    class_ids_string=','.join(str(x) for x in class_ids)
    print(type(class_ids_string), class_ids_string)
    #class_ids_string=convertTuple(class_ids)
    #scores_string=convertTuple(scores)
    #bboxes_string=convertTuple(bboxes)
    #print("is string :  ",type(class_ids_string),class_ids_string,"scores ", scores," scores string ",scores_string)
    id2=tiny("people.jpg")
    id3=tiny("tmp.jpg")
    print("id3", id3=="none",id3)

    try:    
        print( re.post("http://"+ip+":5000/end_point_1b", files={'image': open('odin_chan_cat_person.jpg', 'rb')}) ) 
        time.sleep(2) 
        print( re.post("http://"+ip+":5000/end_point_1b", files={'image': open('doritos_man.jpg', 'rb')}) )     
        returned_img= re.post("http://"+ip+":5000/end_point_1a", files={'image': open('tmp.jpg', 'rb')}) 
        """  file = open('encode.bin', 'rb')
        byte = file.read()
        file.close()
  
        decodeit = open(returned_img, 'wb')
        decodeit.write(base64.b64decode((byte)))
        decodeit.close()"""
        """  this_img_name= 'pics/tmp'+str(picture_index)+'.jpg'
        rimg.save(this_img_name)
        picture_index=picture_index+1"""
        print(type(returned_img.text),returned_img)
        
        #imgdata = base64.b64decode(returned_img.text)
        this_img_name= 'pics/tmps'+str(picture_index)+'.jpg'
        with open(this_img_name, 'wb') as f:
            f.write(returned_img.content)
        picture_index+=1
        print( re.post("http://"+ip+":5000/end_point_1b", files={'image': open('tmp.jpg', 'rb')}) ) 
        print( re.post("http://"+ip+":5000/end_point_2", json={'class': class_ids_string}) )
        print( re.post("http://"+ip+":5000/end_point_2", json={'class': id2}) )
        print( re.post("http://"+ip+":5000/end_point_2", json={'class': id3}) )
        """t_ids = class_ids.tostring()
        t_scores=scores.tostring()
        t_bboxes=bboxes.tostring()
        class_ids_string=np.fromstring(t_ids)
        scores_string=np.fromstring(t_scores)
        bboxes_string=np.fromstring(t_bboxes)
        print("is string :  ",type(class_ids_string))"""
        

    except Exception as e:
        print("Network Error: ",e) 
        
    


picam2.close()