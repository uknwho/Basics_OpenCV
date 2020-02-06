import cv2

# PreTrained classifier for face, this can be obtained in the opencv repository.
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread() # Use the Image, on which you want to detect the faces.
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray,1.1,minNeighbors=4)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)

cv2.imshow('img',img)
cv2.waitKey(0)
