import sys
import os
import cv2
from multiprocessing import Process

from face_detection import face_detect_main as fd
facecascade = cv2.CascadeClassifier("face_detection\\haarcascade_frontalface_default.xml")

def main_process():
	video_capture = cv2.VideoCapture(0)

	emotions = ["anger", "happy", "sadness", "neutral"]

	fishface = cv2.createFisherFaceRecognizer()
	fishface.load("face_detection\\trained_emoclassifier.xml")

	while(True):
	    clahe_image = fd.grab_webcamframe(video_capture)
	    face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
	    if len(face) == 1: 
	        faceslice = fd.crop_face(clahe_image, face)
	        cv2.imshow('face',faceslice)
	        pred, conf = fishface.predict(faceslice)
	        print(emotions[pred])

	    #else:
	        #print("no/multiple faces detected, passing over frame")

	    # Display the resulting frame
	    cv2.imshow('frame',clahe_image)
	    
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	#cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main_process()
	#video_stream()
	p1 = Process(target=main_process)
	p1.start()
	p1.join()