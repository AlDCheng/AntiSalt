import sys
import os
import cv2
from multiprocessing import Process

from NLP import swnclassify as sc
from face_detection import face_detect_main as fd

def video_stream():
    print 'video_stream: starting'

    video_capture = cv2.VideoCapture(0)
    fd.main(video_capture)

    print 'video_stream: finishing'

if __name__ == '__main__':
    p1 = Process(target=video_stream)
    p1.start()
    p1.join()