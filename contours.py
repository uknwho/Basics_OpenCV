import cv2 as cv2
import numpy as np

img=cv2.imread('opencv-logo.png')
imggray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh= cv2.threshold(imggray, 127, 255, 0)
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (127, 120, 120), 3)
print(contours[1])
cv2.imshow('Ori', imggray)
cv2.imshow('con',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
