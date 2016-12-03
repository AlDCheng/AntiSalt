"""
Purpose:
    To test LED changes for a spiraling effect. Not used in final application but is available for use if another lighting effect 
    is desired. Available also for reference. Main LED effects and explanation of functions found in moodlighting.py
    
Created by:
    Israel Macias (irmacias@mit.edu) and Jesse Widner (jwidner@mit.edu)
SentiBoard Team:
    Alan Cheng, Jesse Widner, Jueun Lee, Israel Macias
    
"""

from cue_sdk import *
from Spiral import *
import time
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

Corsair = CUESDK(dir_path+"\\CUESDK\\bin\\x64\\CUESDK.x64_2015.dll")

def MoodColor(algonumber):
    '''
    :param algonumber:
    :returns tuple of (r, g, b):
    '''
    if algonumber >= 80 and algonumber <= 100: #Red to orange from 100-80
        r = 255
        g = int(-1.5*algonumber+150)
        b = 0
    elif algonumber >= 60 and algonumber < 80: #Orange to yellow from 80-60
        r = 255
        g = int(-11.25*algonumber+930)
        b = 0
    elif algonumber >= 40 and algonumber < 60: #Yellow to green from 60-40
        r =int(12.75*algonumber-510)
        g = 255
        b = 0
    elif algonumber >= 20 and algonumber < 40: #Green to blue from 40-20
        r = 0
        g = int(12.75*algonumber-255)
        b = int(-12.75*algonumber+510)
    elif algonumber >= 0 and algonumber < 20: #Blue to white from 20-0
        r = int(-12.75*algonumber+255)
        g = int(-12.75*algonumber+255)
        b = 255
    return (r, g, b)

#Lighting Effect for use in main application
def Spiral(algonumber):
    r = MoodColor(algonumber)[0]
    g = MoodColor(algonumber)[1]
    b = MoodColor(algonumber)[2]
    #Sleep interval between lighting
    interval = 0.025

    for x in range(1, 13):
        Corsair.set_led_colors(CorsairLedColor(x, r, g, b))
        time.sleep(interval)
    #Lights each individual key in a spiraling order and sleeps after each individual
    #key press to obtain desired effect.
    Corsair.set_led_colors(CorsairLedColor(CLK.F12, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PrintScreen, r, g, b))
    Corsair.set_led_colors(CorsairLedColor(CLK.Brightness, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.ScrollLock, r, g, b))
    Corsair.set_led_colors(CorsairLedColor(CLK.WinLock, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PauseBreak, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Stop, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.ScanPreviousTrack, r, g, b))
    Corsair.set_led_colors(CorsairLedColor(CLK.Mute, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PlayPause, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadMinus, r, g, b))
    Corsair.set_led_colors(CorsairLedColor(CLK.ScanNextTrack, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadPlus, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadEnter, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadPeriodAndDelete, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad0, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.RightArrow, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.DownArrow, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.LeftArrow, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.RightCtrl, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Application, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.RightGui, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.RightAlt, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Space, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.LeftAlt, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.LeftGui, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.LeftCtrl, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.LeftShift, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.CapsLock, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Tab, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.GraveAccentAndTilde, r, g, b))
    time.sleep(interval)

    for x in range(14, 24):
        Corsair.set_led_colors(CorsairLedColor(x, r, g, b))
        time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.MinusAndUnderscore, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.EqualsAndPlus, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Backspace, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Insert, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Home, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PageUp, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.NumLock, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadSlash, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.KeypadAsterisk, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad9, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad6, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad3, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad2, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad1, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.UpArrow, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.RightShift, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.SlashAndQuestionMark, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PeriodAndBiggerThan, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.CommaAndLessThan, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.M, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.N, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.B, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.V, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.C, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.X, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Z, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.A, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Q, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.W, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.E, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.R, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.T, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Y, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.U, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.I, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.O, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.P, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.BracketLeft, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.BracketRight, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Backslash, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Delete, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.End, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.PageDown, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Stop, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad7, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad8, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad5, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Keypad4, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.Enter, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.ApostropheAndDoubleQuote, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.SemicolonAndColon, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.L, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.K, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.J, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.H, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.G, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.F, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.D, r, g, b))
    time.sleep(interval)

    Corsair.set_led_colors(CorsairLedColor(CLK.S, r, g, b))
    time.sleep(interval)
