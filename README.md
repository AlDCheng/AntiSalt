# SentiBoard - Readme Documentation

## A Brief Description

SentiBoard uses chat logs and facial recognition data to carefully analyze the user’s mood. It then changes the color of the keyboard LEDs to display how the user is feeling as he/she is using it. Warm colors like red, orange, and yellow represent heightened sense of feeling such as anger, annoyance, and disgust while cool colors like green, blue, and purple represent mood associated with relaxation and happiness.

## Getting Started

This project was made for YHack 2016, so the coding is still rather rough. SentiBoard uses Python, OpenCV, NLTK, and the Corsair API (specifically with [this wrapper](https://pypi.python.org/pypi/cue_sdk/). The current files have only been tested on a Windows 10 machine, but the image processing and NLP portions were written in Linux (Ubuntu 16.04), and should work with the appropriate distros.

### Prerequisites

* [Python 2.7.12](https://www.python.org/) - 64 bit version - Libraries used: Tkinter, Numpy, OpenCV
* OpenCV 2.4.x (Latest is [2.4.13](http://opencv.org/downloads.html)) - Installation instructions can be found in OpenCV's extensive documentation
* [NLTK](http://www.nltk.org/) - We use the Movie Review Corpus in NLTK
* [Corsair API (CUE SDK)](http://www.corsair.com/en-us/support/downloads) with [python wrapper](https://pypi.python.org/pypi/cue_sdk/)

### Running

We don't have any executables readily availible, so the program must be run via the command line. The main program is Application_Main_All.py, and can be run as:

```
Python Application_Main_All.py
```

## Files Involved

Main Program:

[Application_Main_All.py](https://github.com/AlDCheng/AntiSalt/blob/master/Application_Main_All.py) - Main python script using multithreading to handle processing.
[face_detect_main.py](https://github.com/AlDCheng/AntiSalt/blob/master/face_detection/face_detect_main.py) - Extra OpenCV helper function. Most of image processing moved to Application_Main_All.py
[NLK_sentiment.py](https://github.com/AlDCheng/AntiSalt/blob/master/NLP/NLK_sentiment.py) - Final text parser used. Finds if text has positive or negative connotation, and assigns a random weight to it.
[mood_lighting.py](https://github.com/AlDCheng/AntiSalt/blob/master/LightingFX/mood_lighting.py) - Script to change Corsair Keyboard backlighting using Corsair API
[music.py](https://github.com/AlDCheng/AntiSalt/blob/master/Music/music.py) - Optional music playback

Face Recognition Training Functions (adapted from http://www.paulvangent.com/2016/04/01/emotion-recognition-with-python-opencv-and-a-face-dataset/):
[Update_Model.py](https://github.com/AlDCheng/AntiSalt/blob/master/face_detection/Update_Model.py) - Updates training xml data
[face_detect_append.py](https://github.com/AlDCheng/AntiSalt/blob/master/face_detection/face_detect_append.py) - Can be used to add own pictures to training data

## Authors

* **Alan Cheng** - *Project Lead/Worked on facial detection using OpenCV* - adcheng@mit.edu
* **Jueun Lee** - *Worked on NLTK* - jueunlee@mit.edu
* **Israel Macias** - *Worked on Corsair API/NLTK* - irmacias@mit.edu
* **Jesse Widner** - *Worked on Corsair API* - jwidner@mit.edu

## Acknowledgments/References

General:
* Corsair - Provided SDK and lent us Corsair K70 LUX keyboard to develop on

CK+ Facial Expression Detection:
* van Gent, P. (2016). Emotion Recognition With Python, OpenCV and a Face Dataset. A tech blog about fun things with Python and embedded electronics. Retrieved from: http://www.paulvangent.com/2016/04/01/emotion-recognition-with-python-opencv-and-a-face-dataset/
* Kanade, T., Cohn, J. F., & Tian, Y. (2000). Comprehensive database for facial expression analysis. Proceedings of the Fourth IEEE International Conference on Automatic Face and Gesture Recognition (FG'00), Grenoble, France, 46-53.
* Lucey, P., Cohn, J. F., Kanade, T., Saragih, J., Ambadar, Z., & Matthews, I. (2010). The Extended Cohn-Kanade Dataset (CK+): A complete expression dataset for action unit and emotion-specified expression. Proceedings of the Third International Workshop on CVPR for Human Communicative Behavior Analysis (CVPR4HB 2010), San Francisco, USA, 94-101.

JAFFE Facial Expression Detection:
* Michael J. Lyons, Shigeru Akemastu, Miyuki Kamachi, Jiro Gyoba. Coding Facial Expressions with Gabor Wavelets, 3rd IEEE International Conference on Automatic Face and Gesture Recognition, pp. 200-205 (1998).
