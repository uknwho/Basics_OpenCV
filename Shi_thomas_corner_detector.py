#! usr/bin/env python

# importing the Libraries
import numpy as np
import cv2

# Read the image and convert to Grayscale
img  = cv2.imread('IMAGE')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# goodFeaturesToTrack is based on HarrisCorner detector with difference in the calculation of R
# This function takes 4 inputs the first being the grayscale image, second being max number of corners, third min quality level and the last min distances between the corners. 
shi_corner = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
# The detected corners then are converted to integers
shi_corner = np.int0(shi_corner)

# The corners are then marked.  
for c in shi_corner:
    x, y = c.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

# Display the image
cv2.imshow('Corners', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
