import py_compile
from tkinter import font
from turtle import color, width
import cv2
import pickle



Face_Cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
Eye_Cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_eye.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create() 
recognizer.read("trainer.yml")


labels ={}
with open("label.pickle",'rb') as f:
       rev_labels =  pickle.load(f)
       labels = {v:k for k,v in rev_labels.items()}

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = Face_Cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors= 5)
    for(x, y, w, h) in faces:
        #print(x, y, w, h)
        region_of_face_gray = gray[y: y+h, x: x+w]
        region_of_face_color = frame[y: y+h, x: x+w]
        id_ , conf = recognizer.predict(region_of_face_gray)
        if conf >= 60 :
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (0,0,255)
            stroke = 2
            cv2.putText(frame,name, (x-10,y-10), font, 1, color, stroke, cv2.LINE_AA)


        red_tape = (0,0,255)
        stroke=3
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame,(x, y), (end_x, end_y), red_tape, stroke)

        eyes = Eye_Cascade.detectMultiScale(region_of_face_color)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(region_of_face_color,(ex, ey), (ex+ew, ey+eh), (0,255,0), 2)





    cv2.imshow('my WEBcam', frame)
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break
cam.release()