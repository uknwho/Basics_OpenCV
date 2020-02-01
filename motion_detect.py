import cv2
import numpy as np

cap=cv2.VideoCapture('vtest.avi')

ret, frame1=cap.read()
ret, frame2= cap.read()
while cap.isOpened():
    diff=cv2.absdiff(frame1, frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.blur(gray,(5,5),0)
    _, thresh=cv2.threshold(gray,27,255,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.imshow('thresh',gray)

    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)

        if cv2.contourArea(contour)< 700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Frame', frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(50) == 27:
        break
cv2.destroyAllWindows()
cap.release()