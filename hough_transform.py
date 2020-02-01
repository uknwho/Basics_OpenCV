import cv2
import numpy as np

img=cv2.imread('lines.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,50,150, apertureSize=3)
cv2.imshow('edges', edge)

lines=cv2.HoughLines(edge,1,np.pi/180,200)

for l in lines:
    rho, theta=l[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0= a* rho
    y0= b* rho
    x1= int(x0+1000*(-b))
    x2=int(x0-1000*(-b))
    y1=int(y0 + 1000*(a))
    y2=int(y0- 100*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()