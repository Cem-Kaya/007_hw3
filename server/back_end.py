# Authored by Cem Kaya & Emre can eski
import threading
import json
import codecs
from time import strptime
import requests as req
from flask import send_file
from flask_cors import CORS
from flask import Flask, render_template, request, send_from_directory, send_file
import torch 
import torchvision
import cv2
import numpy as np
import base64
from matplotlib import pyplot as plt

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


@app.route('/end_point_1a', methods=['POST'], strict_slashes=False  )
def end_point_1a():
    global picture_index
    file = request.files['image']
    picture_index=picture_index+1

    this_img_name= 'pics/tmp'+str(picture_index)+'.jpg'
    file.save(this_img_name)
   
    img = mpimg.imread(this_img_name)  
    res = yolo_model(img)
    
    #results.save()
    
    
    results = res.pandas().xyxy[0].to_dict(orient="records")
    if len(res) == 0:
        cv2.imwrite(this_img_name, img)
    else:
        for result in results:
            print(result['class'])
            con = result['confidence']
            cs = result['class']
            x1 = int(result['xmin'])
            y1 = int(result['ymin'])
            x2 = int(result['xmax'])
            y2 = int(result['ymax'])
            imagee = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 50 )
            cv2.imwrite(this_img_name, img)
    

    print("type", type(results))
    #results.save(this_img_name)
    # Reading an image in default mode
    #src = cv2.imread('tmp.jpg')
	  #Window name in which image is displayed
    #window_name = 'Image'
    plt.ion()
    #img = mpimg.imread('tmp.png')
    img = mpimg.imread(this_img_name)  
    imgplot = plt.imshow(img)
    plt.show()
    
	# Using cv2.flip() method
	# Use Flip code 0 to flip vertically
   # image = cv2.flip(src, 0)
    #cv2.imshow(window_name, image)
    #cv2.waitKey()
    #byte_image=bytearray(img)
   # x=codecs.img.encode()
    #print("x is",type(x))
    
    return send_file(this_img_name) #render_template("success.html", data= req.post(data = json.dumps(myobj)).text )    



@app.route('/end_point_1b', methods=['POST'], strict_slashes=False  )
def tesend_point_1bt():
    file = request.files['image']
    img = mpimg.imread(file) 
    results = yolo_model(img)
    result=results_parser(results)
    result=result.split(" ")
    is_exists_human=next((i for i, x in enumerate(result) if( x=="person," or x=="persons,")), None)
    number_of_person=0
    
    #find("person")
    print("resuls ",result)
    
    if(is_exists_human!=None):
       number_of_person=int(result[is_exists_human-1])

        
        
    print("numbers is: ",number_of_person)
    return str(number_of_person) #render_template("success.html", data= req.post(data = json.dumps(myobj)).text )    

# do class parsing here 
@app.route('/end_point_2', methods=['POST'], strict_slashes=False  )
def end_point_2():
    class_id_str = request.json['class']
    
    #print("class :", class_id, scores, bbox)
    print("sssss")
    if(class_id_str=="none"):
      print("number is zero")
      return "0"
    print("xxx")
    class_ids= class_id_str.split(',')#check right split !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  
    number_of_person=0
    for class_id in class_ids:
      #(x, y, w, h) = bbox
      #cv2.rectangle(frame, (x, y), (x + w, y + h), (200,0,50), 3)
      class_name = classes[int(class_id)]
      if(class_name =="person"):
          number_of_person+=1
    print("number of",number_of_person)
    return str(number_of_person) #render_template("success.html", data= req.post(data = json.dumps(myobj)).text )    
      #cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200,0,50), 2)
@app.route('/end_point_3', methods=['POST'], strict_slashes=False  )
def end_point_3():
  file = request.files['sound']
  this_sound_name= 'sound'+'.wav'
  file.save(this_sound_name)
  
  print("accepted")
  return "accepted"
  
  
    
    
    






#################################################
if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
    classes = []
    picture_index=0
    with open("classes.txt", "r") as file_object:
      for class_name in file_object.readlines():
        #print(class_name)
        class_name = class_name.strip()  # satır arası  için

        classes.append(class_name)
    imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
    yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  
    results = yolo_model(imgs)
    img = mpimg.imread('tmp.jpg')
    plt.imshow(img)
    plt.axis([-50,50,0,10000])
    plt.ion()
    plt.show()
    # Results
    plt.draw()
    results.print()
    #results.show()  # or .show()
    app.run(debug=False , host="172.22.5.242")