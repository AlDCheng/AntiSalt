from cue_sdk import *
from Spiral import *
import time
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

Corsair = CUESDK(dir_path+"\\CUESDK\\bin\\x64\\CUESDK.x64_2015.dll")

def Transition(algonumber1, algonumber2):
    algonumber = algonumber1
    delta = abs(algonumber2 - algonumber1)
    interval = 0.01

    while (algonumber2 > algonumber):
        SetKeyboardMood(algonumber)
        algonumber += 1
        time.sleep(interval/delta)
    while (algonumber2 < algonumber):
        SetKeyboardMood(algonumber)
        algonumber -= 1
        time.sleep(interval/delta)

def Transition2(algonumber1, algonumber2):
    algonumber = algonumber1
    delta = abs(algonumber2 - algonumber1)
    interval = 0.01

    while (algonumber2 > algonumber):
        SetKeyboardMood2(algonumber)
        algonumber += 1
        time.sleep(interval/delta)
    while (algonumber2 < algonumber):
        SetKeyboardMood2(algonumber)
        algonumber -= 1
        time.sleep(interval/delta)

#from nltk_sentiment import *

#Corsair.RequestControl(CAM.ExclusiveLightingControl)
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

def SetKeyboardMood2(algonumber):
    if algonumber >= 75 and algonumber <= 100: #Red to yellow from 100-75
        SetKeyboardColor(255, int(-10.2*algonumber+1020), 0)
    elif algonumber >= 50 and algonumber < 75: #Yellow to white from 75-50
        SetKeyboardColor(255, 255, int(-10.2*algonumber+765))
    elif algonumber >= 25 and algonumber < 50: #White to green from 50-25
        SetKeyboardColor(int(10.2*algonumber-255), 255, int(10.2*algonumber-255))
    elif algonumber >= 0 and algonumber < 25: #Green to blue from 25-0
        SetKeyboardColor(0, int(10.2*algonumber), int(-10.2*algonumber+255))

def SideProp(algonumber):
    wave1 = [CLK.Escape, CLK.LeftGui, CLK.GraveAccentAndTilde,CLK.Tab, CLK.CapsLock, CLK.LeftShift,CLK.LeftCtrl, CLK.KeypadMinus, CLK.KeypadPlus, CLK.KeypadEnter, CLK.ScanNextTrack]
    wave2 = [CLK.Z,CLK.A,CLK.Q,14,CLK.KeypadAsterisk, CLK.Keypad9,CLK.Keypad6,CLK.Keypad3,CLK.KeypadPeriodAndDelete,CLK.LeftAlt, CLK.PlayPause]
    wave3 = [CLK.F1,15,CLK.W,CLK.S,CLK.X,CLK.KeypadSlash,CLK.Keypad8,CLK.Keypad5,CLK.Keypad2,CLK.Keypad0,CLK.Mute, CLK.ScanPreviousTrack]
    wave4 = [CLK.F2, 16, CLK.E, CLK.D,CLK.C,CLK.NumLock,CLK.Keypad7,CLK.Keypad4,CLK.Keypad1, CLK.Stop]
    wave5 = [CLK.F3, 17, CLK.R, CLK.F, CLK.V, CLK.PauseBreak,CLK.PageUp,CLK.PageDown,CLK.RightArrow]
    wave6 = [CLK.F4, 18, CLK.T,CLK.G, CLK.B, CLK.Space, CLK.ScrollLock,CLK.Home, CLK.End, CLK.UpArrow, CLK.WinLock,CLK.DownArrow]
    wave7 = [19, CLK.Y, CLK.H, CLK.N,CLK.PrintScreen, CLK.Insert,CLK.Delete, CLK.LeftArrow]
    wave8 = [CLK.F5, 20, CLK.U, CLK.J, CLK.M, CLK.F12, CLK.Backspace, CLK.Backslash, CLK.Enter, CLK.RightShift,CLK.RightCtrl, CLK.Brightness, CLK.Application]
    wave9 = [CLK.F6, 21, CLK.I, CLK.K, CLK.CommaAndLessThan,CLK.BracketRight, CLK.ApostropheAndDoubleQuote, CLK.SlashAndQuestionMark, CLK.RightGui]
    wave10 = [CLK.F7, 22, CLK.O, CLK.L, CLK.PeriodAndBiggerThan, CLK.RightAlt, CLK.F11, CLK.EqualsAndPlus, CLK.BracketLeft, CLK.SemicolonAndColon]
    wave11 = [CLK.F8,23, CLK.P, CLK.F10, CLK.MinusAndUnderscore]
    wave12 = [CLK.F9]
    waves = [wave1,wave2,wave3,wave4,wave5,wave6,wave7,wave8,wave9,wave10,wave11,wave12]
    for j in waves:
        for i in j:
            if algonumber >= 80 and algonumber <= 100:
                Corsair.set_led_colors(CorsairLedColor(i, 255, int(-1.5 * algonumber + 150), 0))
            elif algonumber >= 60 and algonumber < 80:
                Corsair.set_led_colors(CorsairLedColor(i,255, int(-11.25 * algonumber + 930), 0))
            elif algonumber >= 40 and algonumber < 60:
                Corsair.set_led_colors(CorsairLedColor(i,int(12.75 * algonumber - 510), 255, 0))
            elif algonumber >= 20 and algonumber < 40:
                Corsair.set_led_colors(CorsairLedColor(i,0, int(12.75*algonumber-255), int(-12.75*algonumber+510)))
            elif algonumber >= 0 and algonumber < 20:
                Corsair.set_led_colors(CorsairLedColor(i,int(-12.75*algonumber+255), int(-12.75*algonumber+255),255))
            time.sleep(0.01)
"""
def _main_():
        while True:

            algo = int(get_nltk_algonumber())
            algo = 70
            Spiral(algo)
            time.sleep(1)
            for i in reversed(range(50,algo)):
                print i
                SetKeyboardMood(i)
                time.sleep(0.01)
_main_()
"""