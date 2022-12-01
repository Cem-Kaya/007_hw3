#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time
import requests as re
import json 
import base64
from picamera2 import Picamera2, Preview
import yaml

with open("conf.yml", "r") as stream:
    try:
        ips =yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
    
print(ips)

ip = "159.20.86.26"

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()
time.sleep(2)
while True:    
    jpeg_buffer = picam2.capture_buffer()
    data = {}   
    
    data['img'] = base64.encodebytes(jpeg_buffer).decode('utf-8')
    time.sleep(0.2)
    re.post("http://"+ip+":5000/post_test", data)


picam2.close()