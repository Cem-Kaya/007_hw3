import cv2
import matplotlib.image as mpimg
import time
from PIL import Image
"""from PIL import Image
image = Image.open('Sample.png')
 
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)"""


# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)


# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        #print(class_name)
        class_name = class_name.strip()  # satır arası boşluklar için

        classes.append(class_name)



# Initialize camera
frame = cv2.imread('b.jpg')



#ret, frame = cap.read()



    # Object Detection
(class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
print(class_ids)
number_of_person=0
print("class_ids: ", type(class_ids), " scores: ", type(scores), "bboxes: ", type(bboxes) )
for class_id, score, bbox in zip(class_ids, scores, bboxes):
    (x, y, w, h) = bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), (200,0,50), 3)
    class_name = classes[class_id]
    if(class_name =="person"):
        number_of_person+=1

    cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200,0,50), 2)
print("number of people ")
print( number_of_person)
im = Image.fromarray(frame)
im.save("your_fal.jpg")
#cv2.imshow("Frame", im)
#print("x2")
#time.sleep(10)


#cv2.destroyAllWindows()

