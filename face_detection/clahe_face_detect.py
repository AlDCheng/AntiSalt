import numpy as np
import glob
import random
import cv2
import cv2.cv as cv

video_capture = cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def grab_webcamframe():
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    return clahe_image

def crop_face(clahe_image, face):
    for (x, y, w, h) in face:
        faceslice = clahe_image[y:y+h, x:x+w]
        faceslice = cv2.resize(faceslice, (350, 350))
    return faceslice

def main():
    emotions = ["anger", "happy", "sadness", "neutral"]

    fishface = cv2.createFisherFaceRecognizer()
    fishface.load("trained_emoclassifier.xml")

    while(True):
        clahe_image = grab_webcamframe()
        face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
        if len(face) == 1: 
            faceslice = crop_face(clahe_image, face)
            cv2.imshow('face',faceslice)
            pred, conf = fishface.predict(faceslice)
            print(emotions[pred])

        else:
            print("no/multiple faces detected, passing over frame")

        # Display the resulting frame
        cv2.imshow('frame',clahe_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

main()