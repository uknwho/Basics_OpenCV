import cv2 as cv2
from matplotlib import pyplot as plt

img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB  )
cany=cv2.Canny(img,100,200)

titles=['Image','Canny']
images=[img,cany]

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()