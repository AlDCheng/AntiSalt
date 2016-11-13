from pygame import mixer,time
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#only compatile with mp3, filepath is a string
def play_music(filepath):
    mixer.init()
    mixer.music.load(dir_path+"//"+filepath)
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)

#play_music('calm_music/nuviole_bianche.mp3')
