import sys, os, time
import cv2
from multiprocessing import Process

import text_testbox as tb
from face_detection import face_detect_main as fd

def video_stream():
    print 'video_stream: starting'
    time.sleep(5)
    video_capture = cv2.VideoCapture(0)
    fd.main(video_capture)

    print 'video_stream: finishing'

def text_stream():
	print 'text_stream: starting'

	tb.main()

	print 'text_stream: finishing'

if __name__ == '__main__':
	#sc.classify_sentence("initializing")
	p2 = Process(target=text_stream)
	p1 = Process(target=video_stream)
	p2.start()
	p1.start()
	p1.join()
	p2.join()