import cv2
cap=cv2.VideoCapture(0);
out=cv2.VideoWriter_fourcc(*'XVID')
vid=cv2.VideoWriter('vid2.avi',out,20,(640,480));


while(cap.isOpened()):
    ret, frame=cap.read();
    if ret==True:
        vid.write(frame)
        cv2.imshow('live stream',frame)
        if cv2.waitKey(20) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
vid.release()
cv2.destroyAllWindows()
