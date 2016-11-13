from pygame import mixer,time
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#only compatile with mp3, filepath is a string
def play_music(filepath, play):
	mixer.init()
	mixer.music.load(dir_path+"//"+filepath)
	#while mixer.music.get_busy():
		#time.Clock().tick(10)
	if(play):
		mixer.music.play()
	else:
		mixer.music.stop()

#play_music('calm_music/nuviole_bianche.mp3')
