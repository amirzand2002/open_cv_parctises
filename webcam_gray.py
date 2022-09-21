import cv2
print(cv2.__version__)
width=480
height=180
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my Gray WEBcam', gray)
    cv2.imshow('my WEBcam', frame)
    
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break
cam.release()