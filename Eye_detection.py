import cv2

# PreTrained classifier that are found in the data of opencv repository.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0) # This is for the video through the webcam. you can enter the video file name thats there in the path. 

while cap.isopened():
    _, img = cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,0,255),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_img=img[y:y+h,x:x+w]
        eyes =eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
