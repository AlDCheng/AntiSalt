import sys, os, time
from Tkinter import *
from time import sleep

from NLP import swnclassify as sc

def main():
	sc.classify_sentence("initializing")

	def Enter_pressed(event):
		input_get = input_field.get()
		sent_stats = sc.classify_sentence(input_get)
		#print(input_get)
		print(sent_stats)

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
	frame3 = Frame(root)
	frame1.pack(side="top", fill="x", pady=(0, 10))
	frame2.pack(fill="x")
	frame3.pack(side="bottom", fill="x")

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

	"""
	salt_val = StringVar()
	salt = Label(frame3, textvariable=salt_val)
	salt_val.set(str(0))
	salt.pack(fill="x")

	root.mainloop()

	salt_num = 0
	while True:
		#sleep(1)
		salt_num += 1
		salt_val.set(str(salt_num))
		root.update_idletasks()"""

main()