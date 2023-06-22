import cv2
from test import test


cam=cv2.VideoCapture(0)
while True:
    status,frame=cam.read()
    cv2.imshow("original",frame)
    print(frame.shape)#480/640
    y1,y2=0,480
    x1,x2=140,500
    frame=frame[y1:y2,x1:x2]
    ki=test(frame,"./resources/anti_spoof_models",0)
    print(ki)
    cv2.imshow("box",frame)
    key=cv2.waitKey(0)
    if key==27:
        break
    
cam.release()
cv2.destroyAllWindows()