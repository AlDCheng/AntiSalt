import numpy as np
import cv2
import cv2.cv as cv

cap = cv2.VideoCapture(0)
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 320)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image = np.zeros((480,640,3), np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    #print "Found "+str(len(faces))+" face(s)"
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imshow('faces',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()