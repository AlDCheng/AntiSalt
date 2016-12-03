"""---------------------------------------------------------------------
 Train facial emotion classifier
 Adapted from: http://www.paulvangent.com/2016/04/01/emotion-recognition-with-python-opencv-and-a-face-dataset/
 (Mostly unchanged from source)

 Modifications by: Alan Cheng
 Email: adcheng@mit.edu
 Date: 12/3/2016

 Description:
 Trains classifier on training images stored in \dataset

 SentiBoard Team: Alan Cheng, Jueun Lee, Israel Macias, Jesse Widner
---------------------------------------------------------------------"""

import cv2
import glob
import random
import numpy as np

fishface = cv2.createFisherFaceRecognizer()

data = {}

def make_sets(emotions):
    training_data = []
    training_labels = []

    for emotion in emotions:
        training = training = glob.glob("dataset\\%s\\*" %emotion)
        for item in training:
            image = cv2.imread(item) 
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            training_data.append(gray)
            training_labels.append(emotions.index(emotion))

    return training_data, training_labels

def run_recognizer(emotions):
    training_data, training_labels = make_sets(emotions)
    
    print("training fisher face classifier")
    print("size of training set is: " + str(len(training_labels)) + " images")
    fishface.train(training_data, np.asarray(training_labels))

def update(emotions):
    run_recognizer(emotions)
    print("saving model")
    fishface.save("trained_emoclassifier.xml")
    print("model saved!")

def main():
    emotions = ["anger", "happy", "sadness", "neutral"]
    make_sets(emotions)
    update(emotions)