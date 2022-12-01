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
import base64
# py -3.10 .\back_end.py # to run the server
# py -3.10 -m pip freeze > requirements.txt # to create requirements.txt
# py -3.10 -m pip install -r requirements.txt # to install requirements.txt 


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/post_test', methods=['POST'], strict_slashes=False  )
def test():
    myobj = {'img': request.form['img']  }
    print (myobj )
    image = base64.decodestring(json.dumps(data)['image'])
    print (image)
    print(myobj['img'] .dtype )
    return "test" #render_template("success.html", data= req.post(data = json.dumps(myobj)).text )    









#################################################
if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
    imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
    yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  
    results = yolo_model(imgs)
    # Results
    results.print()
    #results.show()  # or .show()
    app.run(debug=True , host="0.0.0.0")