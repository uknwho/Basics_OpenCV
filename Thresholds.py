# In Thresholding, every pixcel of the image is compared with a threshold value and converted to 0 and 1. It is a sementation technique to seperate an object as foreground and backgrounding the other unimportant spaces.
# Thresholding is done only for grayscale images. In this code, different Thresholding methods are employed on a single image and the output is saved in "Thresholds.png" to understand each method.
#! usr/bin/env python


import cv2
from matplotlib import pyplot as plt

img = cv2.imread('LANE.png',0)
_, thres1 =cv2.threshold(img, 127, 250, cv2.THRESH_BINARY)
_, thres2 =cv2.threshold(img, 127, 250, cv2.THRESH_BINARY_INV)
_, thres3 =cv2.threshold(img, 127, 250, cv2.THRESH_TRUNC)
_, thres4 =cv2.threshold(img, 127, 250, cv2.THRESH_TOZERO)
_, thres5 =cv2.threshold(img, 127, 250, cv2.THRESH_TOZERO_INV)
images = [img, thres1, thres2, thres3, thres4, thres5]
title = ['Original', 'Binary', 'Binary INV', 'Trunc', 'Tozero', 'Tozero INV']
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], 'gray');
    plt.title(title[i]);

plt.show()
