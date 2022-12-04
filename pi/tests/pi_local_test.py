#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time
import requests as re
import json 
import base64
#from picamera2 import Picamera2, Preview
import yaml

with open("conf.yml", "r") as stream:
    try:
        ips =yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
    
print(ips)

ip = "127.0.0.1"

#picam2 = Picamera2()

#preview_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
#picam2.configure(preview_config)

#picam2.start_preview(Preview.QTGL)

#picam2.start()
time.sleep(2)
while True:    
    #picam2.capture_file("tmp.jpg")
    time.sleep(2) 


    try:    
        print( re.post("http://"+ip+":5000/post_test", files={'image': open('odin_chan_cat_person.jpg', 'rb')}) ) 
        time.sleep(2) 
        print( re.post("http://"+ip+":5000/post_test", files={'image': open('doritos_man.jpg', 'rb')}) )   
        time.sleep(2)  
        print( re.post("http://"+ip+":5000/post_test", files={'image': open('tmp.jpg', 'rb')}) )  
        
        print(np.fromstring(ts))
        (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)

        t_ids = class_ids.tostring()
        t_scores=scores.tostring()
        t_bboxes=bboxes.tostring()
        class_ids_string=np.fromstring(t_ids)
        scores_string=np.fromstring(t_scores)
        bboxes_string=np.fromstring(t_bboxes)
        print("is string :  ",type(class_ids_string))


    except Exception as e:
        print("Network Error: ",e) 
        
    


picam2.close()