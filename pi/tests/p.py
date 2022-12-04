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

import matplotlib.image as mpimg
import time
from PIL import Image


# Opencv DNN


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
        #print( re.post("http://"+ip+":5000/end_point_2", json={'class': id2}) )

           
    except Exception as e :
        print("Network Error",e) 
    


picam2.close()