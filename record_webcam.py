from fileinput import filename
import os
from turtle import width 
import cv2
from datetime import datetime

# saving file configuration
resolution = '480p'
filename = datetime.now().strftime("%d-%I-%M-%S-")+str(resolution)+(".mp4")
frames_per_seconds = 24

def change_res(cam , width, height):
    cam.set(3,width)
    cam.set(4,height)

STD_DIMENSIONS = {
    "480p": (640,480),
    "720p": (1280,720),
    "360p": (480,360),
    "1080p":(1920,1080),
}
VIDEO_TYPE = {
    'mp4':cv2.VideoWriter_fourcc(*'XVID'),
    'avi':cv2.VideoWriter_fourcc(*'XVID'),
    'mpeg':cv2.VideoWriter_fourcc(*'MPEG'),
}

def get_dims(cam, res):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cam, width=width, height= height)
    return width, height

def get_video_type(filename):
    filename , ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['mp4']


#setting opencv configuration
cam=cv2.VideoCapture(0)
dims = get_dims(cam, res=resolution)
video_type_cv = get_video_type(filename=filename)
out = cv2.VideoWriter(filename, video_type_cv, frames_per_seconds, dims)
#cam.set(cv2.CAP_PROP_FPS, 30)
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))



while True:
    ignore,  frame = cam.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('my WEBcam', frame)
    
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()
