## CORNER DETECTION Using Harris Corner Method

# importing the necessary libraries
import numpy as np
import cv2 as cv

# Reading the image
img = cv.imread('left03.jpg')
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Applying harris Corner
pr = np.float32(grey)
# The cv.cornerharris function works with float 32 images.
Harris_corner  = cv.cornerHarris(pr, 2, 3, 0.02)
dial = cv.dilate(Harris_corner, None)
# Highlighting the corners detected with red color
img[dial> 0.01*dial.max()] = (0,0,255)

# Displaying the Image
cv.imshow('Harris corners', img)

if cv.waitKey(0) & 0xff ==27:
    cv.destroyAllWindows()


