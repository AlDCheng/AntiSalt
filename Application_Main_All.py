import sys, os, time
import cv2
from ctypes import c_int
from Tkinter import *
from multiprocessing import Process, Manager, Pool, Value, Lock

#import text_testbox as tb
from face_detection import face_detect_main as fd
from NLP import swnclassify as sc

facecascade = cv2.CascadeClassifier("face_detection\\haarcascade_frontalface_default.xml")

def video_stream(val, lock):
	print 'video_stream: starting'
	time.sleep(5)
	video_capture = cv2.VideoCapture(0)
	emotions = ["anger", "happy", "sadness", "neutral"]

	fishface = cv2.createFisherFaceRecognizer()
	fishface.load("face_detection\\trained_emoclassifier.xml")

	while(True):
		clahe_image = fd.grab_webcamframe(video_capture)
		face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)

		if len(face) == 1: 
			faceslice = fd.crop_face(clahe_image, face)
			cv2.putText(faceslice,'Hello World!',(10,500), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
			cv2.imshow('face',faceslice)
			pred, conf = fishface.predict(faceslice)
			print(emotions[pred])
			inc_val = 0
			if(pred == 0): #anger
				inc_val = 3
			elif(pred == 1): #happy
				inc_val = -1
			elif(pred == 1): #happy
				inc_val = 2
			else:
				inc_val = 0

			with lock:
				val.value += inc_val
				if(val.value < 0):
					val.vaue = 0

			#shared_list.append(emotions[pred])

		cv2.imshow('frame',clahe_image)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()
	print 'video_stream: finishing'

def text_stream(val, lock):
	print 'text_stream: starting'
	sc.classify_sentence("initializing")

	def Enter_pressed(event):
		input_get = input_field.get()
		sent_stats = sc.classify_sentence(input_get)
		print(sent_stats)
		#shared_list.append(sent_stats)
		with lock:
			val.value += int(-5*sent_stats)
			if (val.value < 0):
				val.value = 0

		cur_time = time.strftime("%I")+":"+time.strftime("%M")+time.strftime("%p")+": "
		
		T.configure(state='normal')
		T.insert(END, cur_time+input_get+"\n")
		T.insert(END, "> " + str(sent_stats) + "\n")
		T.configure(state='disabled')

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

def read_console(val, lock):
	print 'read_console: starting'

	while True:
		print val.value

	print 'read_console: finishing'

#Main function

if __name__ == '__main__':
	#manager = Manager()
	#shared_list = manager.list()
	#salt_val = manager.integer()
	v = Value('i', 0)
	lock = Lock()

	p3 = Process(target=read_console, args=(v, lock))
	p2 = Process(target=text_stream, args=(v, lock))
	p1 = Process(target=video_stream, args=(v, lock))

	p3.start()
	p2.start()
	p1.start()

	p1.join()
	p2.join()
	p3.join()