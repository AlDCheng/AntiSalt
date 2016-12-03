"""---------------------------------------------------------------------
 SentiBoard Main Script:

 Author: Alan Cheng
 Email: adcheng@mit.edu
 Date: 12/3/2016

 Description:
 Main script for SentiBoard Hackathon Project. Uses multithreading
 with simple UI. Windows shown:
 	- Dummy chat log. Responses show sentiment value
 	- Sentiment value. This value directly effects keyboard backlighting
 	- Camera video source
 	- Cropped face (from video). Also overlays recognized emotion text

 SentiBoard Team: Alan Cheng, Jueun Lee, Israel Macias, Jesse Widner
---------------------------------------------------------------------"""

import sys, os, time
import cv2
import msvcrt
import numpy

from ctypes import c_int
from multiprocessing import Process, Manager, Pool, Value, Lock
from time import sleep

# Import project files
from face_detection import face_detect_main as fd
from NLP import NLK_sentiment as sc
from LightingFX import Spiral as sp
from LightingFX import mood_lighting as ml
from Music import music as mu
from Tkinter import *

# Training data for facial recognition using Haar
facecascade = cv2.CascadeClassifier("face_detection\\haarcascade_frontalface_default.xml")

# Thread 1: Video stream and processing
def video_stream(val, lock):
	print 'video_stream: starting'

	# Delay to wait for text sentiment recognition to initialize
	time.sleep(5)

	video_capture = cv2.VideoCapture(0)

	# Emotions being recognized. Can be adjusted based-off training data
	emotions = ["anger", "happy", "sadness", "neutral"]

	# Initialize FisherFace for facial emotion recognition
	fishface = cv2.createFisherFaceRecognizer()
	fishface.load("face_detection\\trained_emoclassifier.xml")

	# Image processing loop
	while(True):
		# Set signal to break all threads
		if(val.value == 666):
			break

		clahe_image = fd.grab_webcamframe(video_capture)

		# Haar detection returns all faces
		face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)

		# If there exists a face
		if len(face) > 0: 
			faceslice = fd.crop_face(clahe_image, face)

			# Emotion recognition returned as pred.
			# Pred values: 0 (anger), 1 (happy), 2(sadness), 3 (neutral)
			# These value are defined by the order in variable 'emotions'
			pred, conf = fishface.predict(faceslice)

			cv2.putText(faceslice,emotions[pred],(100,330), cv2.FONT_HERSHEY_SIMPLEX, 1,255,2)
			cv2.imshow('face',faceslice)
			
			# Changing sentiment value variable
			inc_val = 0
			if(pred == 0): #anger
				inc_val = 0.7
			elif(pred == 1): #happy
				inc_val = -0.5
			elif(pred == 2): #sadness
				inc_val = 0.3
			else: #neutral
				inc_val = -0.2
		else:
			# Gradually lower sentiment value if no face. Mostly for demonstration
			inc_val = -0.01
 
		with lock:
			val.value += inc_val
			if(val.value < 0):
				val.value = 0
			elif(val.value > 100):
				val.value = 100

		cv2.imshow('frame',clahe_image)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()
	print 'video_stream: finishing'

	# Tell other threads to terminate
	with lock:
		val.value = 666

# Thread 2: Dummy chat log + NLP
def text_stream(val, lock):
	print 'text_stream: starting'

	# Force NLP to initialize (takes around 5 seconds)
	sc.classify_sentence("initializing")

	# Crude UI implementation. On-hit function for "Enter"
	def Enter_pressed(event):
		input_get = input_field.get()

		# Classify text sentiment here
		sent_stats = sc.classify_sentence(input_get)

		# Adjust sentiment value
		with lock:
			val.value += int(sent_stats)
			if (val.value < 0):
				val.value = 0
			elif(val.value > 100):
				val.value = 100

		cur_time = time.strftime("%I")+":"+time.strftime("%M")+time.strftime("%p")+": "
		
		T.configure(state='normal')
		T.insert(END, cur_time+input_get+"\n")
		T.insert(END, "> " + str(sent_stats) + "\n")
		T.configure(state='disabled')
		T.see("end")
		input_field.delete(0, END)

	# Tkinter UI stuff here

	root = Tk()
	root.minsize(width=200, height=600)
	frame1 = Frame(root)
	frame2 = Frame(root)
	frame1.pack(side="top", fill="x", pady=(0, 10))
	frame2.pack(side="bottom", fill="x")

	S = Scrollbar(frame1)
	T = Text(frame1, height=40, width=50)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set, state = DISABLED)
	#T.insert(END, quote)

	input_user = StringVar()
	input_field = Entry(frame2, text=input_user)
	input_field.pack(fill="x")
	input_field.bind("<Return>", Enter_pressed)

	root.mainloop()

	# Terminate all threads
	print 'text_stream: finishing'
	with lock:
		val.value = 666

#Thread 3: Change keyboard backlighting + music playback (disabled as default)
def read_console(val, lock):
	print 'read_console: starting'

	# Uncommenting code here allows music playback

	past_val = 0
	#play = False
	while True:
		if(val.value == 666):
			break

		"""if val.value > 90 and not play:
			play = True
			mu.play_music("BobMarley.mp3", play)
		elif play and val.value < 50:
			play = False
			mu.play_music("BobMarley.mp3", play)"""
			
		cur_val = val.value

		# This function accesses Corsair API to change backlighting
		ml.Transition2(cur_val,past_val)
		past_val = cur_val 

	# Terminate all threads
	print 'read_console: finishing'
	with lock:
		val.value = 666

# Thread 4: Display sentiment value for debugging purposes
def disp_alt(val, lock):
	master = Tk()

	def task():
		salt_val.set(val.value)
		if(val.value != 666):
			master.after(10, task)  # reschedule event in 2 seconds

	salt_val = StringVar()
	salt = Label(master, textvariable=salt_val)
	salt.pack(fill="x")

	master.after(10, task)
	master.mainloop()

# Main function: handles muilthreading
if __name__ == '__main__':
	v = Value('f', 0)
	lock = Lock()

	p4 = Process(target=disp_alt, args=(v, lock))
	p3 = Process(target=read_console, args=(v, lock))
	p2 = Process(target=text_stream, args=(v, lock))
	p1 = Process(target=video_stream, args=(v, lock))

	p4.start()
	p3.start()
	p2.start()
	p1.start()

	p1.join()
	p2.join()
	p3.join()
	p4.join()