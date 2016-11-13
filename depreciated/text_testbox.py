import sys, os, time
import Tkinter as tk
from multiprocessing import Process, Manager, Pool, Value, Lock

from NLP import swnclassify as sc

def text_stream(val, lock):

class AS_UI:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.frameL = tk.Frame(self.frame)
		self.frameR = tk.Frame(self.frame)
		self.frameL.pack(side="left", fill="y")
		self.frameR.pack(side="right", fill="y")

		self.frameLT = tk.Frame(self.frameL)
		self.frameLB = tk.Frame(self.frameL)
		self.frameLB1 = tk.Frame(self.frameL)
		self.frameLB2 = tk.Frame(self.frameL)
		self.frameLT.pack(side="top", fill="x")
		self.frameLB.pack(fill="x")
		self.frameLB1.pack(fill="x")
		self.frameLB2.pack(side="bottom", fill="x")

		#Left Panel
		self.leftScroll = tk.Scrollbar(self.frameLT)
		self.leftTextBox = tk.Text(self.frameLT, height=40, width=50)
		self.leftScroll.pack(side="right", fill="y")
		self.leftTextBox .pack(side="left", fill="y")
		self.leftScroll.config(command=self.leftTextBox.yview)
		self.leftTextBox.config(yscrollcommand=self.leftScroll.set, state = "disabled")
		self.inputUser = tk.StringVar()
		self.inputField = tk.Entry(self.frameLB, text=self.inputUser)
		self.inputField.pack(fill="x")
		self.inputField.bind("<Return>", self.Enter_pressed)

		#Right Panel
		self.emotion_val = tk.StringVar()
		self.emotion = tk.Label(self.frameLB1, textvariable=self.emotion_val)
		self.emotion.pack(fill="x")
		self.emotion_val.set("Neutral")
		self.salt_val = tk.StringVar()
		self.salt = tk.Label(self.frameLB2, textvariable=self.salt_val)
		self.salt_val.set(str(0))
		self.salt.pack(fill="x")

		self.frame.pack()

	def Enter_pressed(self, event):
		input_get = self.inputField.get()
		sent_stats = sc.classify_sentence(input_get)
		with lock:
			val.value += int(sent_stats)
			if (val.value < 0):
				val.value = 0

		cur_time = time.strftime("%I")+":"+time.strftime("%M")+time.strftime("%p")+": "
		
		self.leftTextBox.configure(state='normal')
		self.leftTextBox.insert(END, cur_time+input_get+"\n")
		self.leftTextBox.insert(END, "> " + str(sent_stats) + "\n")
		self.leftTextBox.configure(state='disabled')

		self.inputField.delete(0, END)



def main(): 
	root = tk.Tk()
	app = AS_UI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
	v = Value('i', 0)
	lock = Lock()
	p2 = Process(target=text_stream, args=(v, lock))
	p2.start()
	p2.join()