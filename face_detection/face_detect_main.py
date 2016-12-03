"""---------------------------------------------------------------------
 OpenCV helper functions:

 Author: Alan Cheng
 Email: adcheng@mit.edu
 Date: 12/3/2016

 Description:
 Majority of code moved to main script. Leftover helper functions found
 in here.

 SentiBoard Team: Alan Cheng, Jueun Lee, Israel Macias, Jesse Widner
---------------------------------------------------------------------"""

import numpy as np
import glob
import random
import cv2
import cv2.cv as cv
import os

script_dir = os.path.dirname(__file__)
facecascade = cv2.CascadeClassifier(script_dir + "\\haarcascade_frontalface_default.xml")

def grab_webcamframe(video_capture):
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