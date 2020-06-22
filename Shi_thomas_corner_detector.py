import numpy as np
import cv2

img  = cv2.imread('shapes.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

shi_corner = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)

shi_corner = np.int0(shi_corner)

for c in shi_corner:
    x, y = c.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Corners', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()