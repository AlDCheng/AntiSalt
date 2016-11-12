import numpy as np
import glob
import random
import cv2
import cv2.cv as cv

def video_init():
    cap = cv2.VideoCapture(0)
    cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 320)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    return cap, face_cascade

def get_files(emotion): #Define function to get file list, randomly shuffle it and split 80/20
    files = glob.glob("dataset/%s/*" %emotion)
    return files

def CK_training(emotions):
    fishface = cv2.createFisherFaceRecognizer() #Initialize fisher face classifier
    training_data = []
    training_labels = []
    for emotion in emotions:
        training = get_files(emotion)
        #Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item) #open image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
            training_data.append(gray) #append image array to training data list
            training_labels.append(emotions.index(emotion))

    fishface.train(training_data, np.asarray(training_labels))

    return fishface

def main():
    cap, face_cascade = video_init()

    #emotions = ["neutral", "anger", "disgust", "happy", "surprise"]
    emotions = ["neutral", "anger", "happy"]
    #fishface = CK_training(emotions)
    fishface = cv2.createFisherFaceRecognizer()
    fishface.load("fisherface_params_nah.xml")

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        #print "Found "+str(len(faces))+" face(s)"
        face = gray
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            #face = gray[int(0.8*y):y+int(1.2*h), int(0.8*x):x+int(1.2*h)]
            face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (350,350))

        pred, conf = fishface.predict(face)
        print(emotions[pred])

        # Display the resulting frame
        cv2.imshow('frame',gray)
        cv2.imshow('faces',frame)
        cv2.imshow('face',face)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

main()