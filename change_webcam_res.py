from turtle import width
import cv2

#setting opencv configuration
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

# defining a function to choose a webcam resolution
def res(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation= cv2.INTER_AREA)


while True:
    ignore,  frame = cam.read()
    frame = res(frame=frame, percent=45)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my Gray WEBcam', gray)
    
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break
cam.release()