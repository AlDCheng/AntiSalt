import sys, os, time
import cv2
import msvcrt
from ctypes import c_int
from Tkinter import *
from multiprocessing import Process, Manager, Pool, Value, Lock
from time import sleep

#import text_testbox as tb
from face_detection import face_detect_main as fd
#from NLP import swnclassify as sc
from NLP import NLK_sentiment as sc
from LightingFX import Spiral as sp
from LightingFX import mood_lighting as ml
from Music import music as mu
facecascade = cv2.CascadeClassifier("face_detection\\haarcascade_frontalface_default.xml")

def video_stream(val, lock):
	print 'video_stream: starting'
	time.sleep(5)
	video_capture = cv2.VideoCapture(0)
	emotions = ["anger", "happy", "sadness", "neutral"]

	fishface = cv2.createFisherFaceRecognizer()
	fishface.load("face_detection\\trained_emoclassifier.xml")

	while(True):
		if(val.value == 666):
			break
		clahe_image = fd.grab_webcamframe(video_capture)
		face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)

		if len(face) == 1: 
			faceslice = fd.crop_face(clahe_image, face)
			pred, conf = fishface.predict(faceslice)
			cv2.putText(faceslice,emotions[pred],(100,330), cv2.FONT_HERSHEY_SIMPLEX, 1,255,2)
			cv2.imshow('face',faceslice)
			
			#print(emotions[pred])
			inc_val = 0
			if(pred == 0): #anger
				inc_val = 0.7
			elif(pred == 1): #happy
				inc_val = -0.5
			elif(pred == 2): #sadness
				inc_val = 0.3
			else:
				inc_val = -0.2

			with lock:
				val.value += inc_val
				if(val.value < 0):
					val.value = 0
				elif(val.value > 100):
					val.value = 100

			#shared_list.append(emotions[pred])

		cv2.imshow('frame',clahe_image)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()
	print 'video_stream: finishing'
	with lock:
		val.value = 666

def text_stream(val, lock):
	print 'text_stream: starting'
	sc.classify_sentence("initializing")
	#print(sc.get_nltk_algonumber("initializing"))

	def Enter_pressed(event):
		input_get = input_field.get()
		sent_stats = sc.classify_sentence(input_get)
		#sent_stats = sc.get_nltk_algonumber(input_get)
		#xprint(sent_stats)
		#shared_list.append(sent_stats)
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

	print 'text_stream: finishing'
	with lock:
		val.value = 666

def read_console(val, lock):
	print 'read_console: starting'

	past_val = 0
	play = False
	while True:
		if(val.value == 666):
			break

		if val.value > 90 and not play:
			play = True
			mu.play_music("BobMarley.mp3", play)
		elif play and val.value < 50:
			play = False
			mu.play_music("BobMarley.mp3", play)
			
		cur_val = val.value
		ml.Transition2(cur_val,past_val)
		past_val = cur_val 

	print 'read_console: finishing'
	with lock:
		val.value = 666

#Main function

def disp_alt(val, lock):
	master = Tk()

	def task():
		#print("hello")
		salt_val.set(val.value)
		if(val.value != 666):
			master.after(10, task)  # reschedule event in 2 seconds

	salt_val = StringVar()
	salt = Label(master, textvariable=salt_val)
	salt.pack(fill="x")

	master.after(10, task)
	master.mainloop()

	"""
	def update_val():
		salt_val.set(val.value)	
		master.after(500, update_val)

	master = Tk()
	salt_val = StringVar()
	salt = Label(master, textvariable=salt_val)
	salt_val.set(val.value)
	salt.pack(fill="x")
	master.after(0, update_val) 
	master.mainloop()
	"""

if __name__ == '__main__':
	#manager = Manager()
	#shared_list = manager.list()
	#salt_val = manager.integer()
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