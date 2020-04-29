#!/usr/bin/env pyhton

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask  =  cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kern = np.ones((3,3), np.uint8)

dilate = cv2.dilate(mask, kern)
erode = cv2.erode(mask, kern)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kern)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kern)
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kern)

titles = ['image', 'mask', 'dilate', 'erode', 'opening', 'closing', 'gradient', 'top_hat']
images = [img, mask, dilate, erode, opening, closing, gradient, top_hat]

for i in range(8):
    plt.subplot(2,4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks(), plt.yticks()

plt.show()