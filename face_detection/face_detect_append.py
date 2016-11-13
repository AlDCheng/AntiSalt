import cv2
import cv2.cv as cv
import numpy as np
import argparse
import time
import glob
import os
import Update_Model
import msvcrt as m

video_capture = cv2.VideoCapture(0)
video_capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
fishface = cv2.createFisherFaceRecognizer()
try:
    fishface.load("trained_emoclassifier.xml")
except:
    print("no xml found")

facedict = {}
emotions = ["anger", "happy", "sadness", "neutral"]

def crop_face(clahe_image, face):
    for (x, y, w, h) in face:
        faceslice = clahe_image[y:y+h, x:x+w]
        faceslice = cv2.resize(faceslice, (350, 350))
    facedict["face%s" %(len(facedict)+1)] = faceslice
    return faceslice

def update_model(emotions):
    print("Model update mode active")
    check_folders(emotions)
    for i in range(0, len(emotions)):
        print("collected images, looking good! Now updating model...")
        save_face(emotions[i])
    #print("collected images, looking good! Now updating model...")
    Update_Model.update(emotions)
    print("Done!")

def check_folders(emotions): #check if folder infrastructure is there, create if absent
    for x in emotions:
        if os.path.exists("dataset\\%s" %x):
            pass
        else:
            os.makedirs("dataset\\%s" %x)

def save_face(emotion):
    print("\n\nplease look " + emotion + " when the timer expires and keep the expression stable until instructed otherwise.\nPress any key to continue")
    m.getch()
    for i in range(0,5):#Timer to give you time to read what emotion to express
        print(5-i)
        time.sleep(1)
    while len(facedict.keys()) < 16: #Grab 15 images for each emotion
        detect_face()
    for x in facedict.keys(): #save contents of dictionary to files
        print(emotion, "dataset\\%s\\user_%s.jpg" %(emotion, len(glob.glob("dataset\\%s\\*" %emotion))))
        cv2.imwrite("dataset\\%s\\user_%s.jpg" %(emotion, len(glob.glob("dataset\\%s\\*" %emotion))), facedict[x])
    facedict.clear() #clear dictionary so that the next emotion can be stored

def grab_webcamframe():
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    return clahe_image

def detect_face():
    clahe_image = grab_webcamframe()
    face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(face) == 1: 
        faceslice = crop_face(clahe_image, face)
        return faceslice
    else:
        print("no/multiple faces detected, passing over frame")

update_model(emotions)