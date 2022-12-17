# Authored by Cem Kaya & ...
import threading
import json
from time import strptime
import requests as req
from flask_cors import CORS
from flask import Flask, render_template, request, send_from_directory, send_file
import torch 
import torchvision
import cv2
import numpy as np
import base64
from matplotlib import pyplot as plt2

# Program for converting bytes to string using decode()
 
# import required module
import codecs
import matplotlib.image as mpimg

# py -3.10 .\back_end.py # to run the server
# py -3.10 -m pip freeze > requirements.txt # to create requirements.txt
# py -3.10 -m pip install -r requirements.txt # to install requirements.txt 

def results_parser(results):
  s = ""
  if results.pred[0].shape[0]:
    for c in results.pred[0][:, -1].unique():
      n = (results.pred[0][:, -1] == c).sum()  # detections per class
      s += f"{n} {results.names[int(c)]}{'s' * (n > 1)}, "  # add to string
  return s
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/post_test', methods=['POST'], strict_slashes=False  )
def test():
    global picture_index

    file = request.files['image'] 

    this_img_name= 'pics/tmp'+str(picture_index)+'.jpg'
    file.save(this_img_name)
    picture_index=picture_index+1

    # Reading an image in default mode
    #src = cv2.imread('tmp.jpg')
   
	# Window name in which image is displayed
    #window_name = 'Image'
    #plt2.switch_backend('agg')
 
    plt2.ion()
    img = mpimg.imread(this_img_name)
  
    imgplot = plt2.imshow(img)
    
    
    results = yolo_model(img)
    result=results_parser(results)
    result=result.split(" ")
    #results.print()
    
    
    is_exists_human=next((i for i, x in enumerate(result) if( x=="person," or x=="persons,")), None)
    number_of_person=0

    #find("person")
    print("resuls ",result)
  
    if(is_exists_human!=None):
       number_of_person=int(result[is_exists_human-1])

        
        
    print(number_of_person)
         
    
    results.show() 
	# Using cv2.flip() method
	# Use Flip code 0 to flip vertically
   # image = cv2.flip(src, 0)
    #cv2.imshow(window_name, image)
    #cv2.waitKey()
    img.save(this_img_name)
    #resmi byte cevirip at
    #byte_image=bytearray(img)
    x=codecs.img.encode()
    print("x is",type(x))
    return "x" #render_template("success.html", data= req.post(data = json.dumps(myobj)).text )    










#################################################
if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
    imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
    picture_index=0
    print("sssssssssssssssssssjkddms")
    #img = mpimg.imread('tmp.jpg')
    #plt2.axis([-50,50,0,10000])
 
   
    
    yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  
    results = yolo_model(imgs)
    plt2.pause(0.5)
    # Results
    plt2.draw()
    
    #results.print()
    #results.show()  # or .show()
    app.run(debug=True , host="0.0.0.0")