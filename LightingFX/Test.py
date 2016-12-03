from cue_sdk import *
import time
import readchar
from msvcrt import getch
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
Corsair = CUESDK(dir_path+"\\CUESDK\\bin\\x64\\CUESDK.x64_2015.dll")

algonumber = 100

def SetKeyboardColor(r, g, b):
    #Wait until key is pressed
    for x in range (1, 130):
        Corsair.set_led_colors(CorsairLedColor(x, r, g, b))

def SetKeyboardMood(algonumber):
    if algonumber >= 80 and algonumber <= 100: #Red to orange from 100-80
        SetKeyboardColor(255, int(-1.5*algonumber+150), 0)
    elif algonumber >= 60 and algonumber < 80: #Orange to yellow from 80-60
        SetKeyboardColor(255, int(-11.25*algonumber+930), 0)
    elif algonumber >= 40 and algonumber < 60: #Yellow to green from 60-40
        SetKeyboardColor(int(12.75*algonumber-510), 255, 0)
    elif algonumber >= 20 and algonumber < 40: #Green to blue from 40-20
        SetKeyboardColor(0, int(12.75*algonumber-255), int(-12.75*algonumber+510))
    elif algonumber >= 0 and algonumber < 20: #Blue to white from 20-0
        SetKeyboardColor(int(-12.75*algonumber+255), int(-12.75*algonumber+255),255)


def Propogate(algonumber):
    for i in range(1,70):
        Corsair.set_led_colors(CorsairLedColor(i, 255, int(-1.5 * algonumber + 150), 0))
        Corsair.set_led_colors(CorsairLedColor(121-i, 255, int(-1.5 * algonumber + 150), 0))
        time.sleep(0.02)



algo = input("What is the salt level?")
Propogate(algo)
time.sleep(1)
for i in reversed(range(0,algo)):
    SetKeyboardMood(i)
    time.sleep(0.1)
time.sleep(1)

