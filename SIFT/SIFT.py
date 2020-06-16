#Importing Libraries
import cv2
import numpy as np

# Reading the Image
img = cv2.imread('aloeR.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying the SIFT feature
sift = cv2.xfeatures2d_SIFT.create()
kp = sift.detect(grey, None)

# Highlighting the Key Points
img = cv2.drawKeypoints(grey, kp,img)
cv2.imshow("SIFT", img)