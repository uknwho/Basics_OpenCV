#Detecting Shapes using findContours
import cv2
import numpy as np

img=cv2.imread('shapes.jpg')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


_, thresh=cv2.threshold(imggray, 244,255,cv2.THRESH_BINARY)
contours, _= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for c in contours:
    approx=cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),5)

    font= cv2.FONT_HERSHEY_COMPLEX
    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)== 3: #Triangle
        cv2.putText(img,"triangle",(x,y),font,0.5,(0,0,0),3)
    elif len(approx)== 4: #Rectabgle
        cv2.putText(img,"rectangle",(x,y),font,0.5,(0,0,0),3)
    elif len(approx)== 5: #Pentagon
        cv2.putText(img,"Pentagon",(x,y),font,0.5,(0,0,0),3)
    elif len(approx)== 10: #Decagon
        cv2.putText(img,"Decagon",(x,y),font,0.5,(0,0,0),3)
    else :
        cv2.putText(img,"Circle",(x,y),font,0.5,(0,0,0),3)

cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
