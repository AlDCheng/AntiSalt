"""

Purpose:
    To test LED changes. Not used in final application. Mainly used for initial testing. Available for testing.
    
Created by:
    Israel Macias (irmacias@mit.edu) and Jesse Widner (jwidner@mit.edu)

SentiBoard Team:
    Alan Cheng, Jesse Widner, Jueun Lee, Israel Macias

"""




from cue_sdk import *
import time
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
Corsair = CUESDK(dir_path+"\\CUESDK\\bin\\x64\\CUESDK.x64_2015.dll")

algonumber = 100 #Number that defines the current color of a specific key that is made proportional to the RGB values.

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

def SideProp(algonumber):
    #Wave lighting effect that propagates from left to right and right to left simultaneously.
    #Was used for initial testing but later left unused. Code is available for use if desired.
    #Not used in final application.
    wave1 = [CLK.Escape, CLK.LeftGui, CLK.GraveAccentAndTilde,CLK.Tab, CLK.CapsLock, CLK.LeftShift,CLK.LeftCtrl, CLK.KeypadMinus, CLK.KeypadPlus, CLK.KeypadEnter]
    wave2 = [CLK.Z,CLK.A,CLK.Q,14,CLK.KeypadAsterisk, CLK.Keypad9,CLK.Keypad6,CLK.Keypad3,CLK.KeypadPeriodAndDelete,CLK.LeftAlt]
    wave3 = [CLK.F1,15,CLK.W,CLK.S,CLK.X,CLK.KeypadSlash,CLK.Keypad8,CLK.Keypad5,CLK.Keypad2,CLK.Keypad0]
    wave4 = [CLK.F2, 16, CLK.E, CLK.D,CLK.C,CLK.NumLock,CLK.Keypad7,CLK.Keypad4,CLK.Keypad1]
    wave5 = [CLK.F3, 17, CLK.R, CLK.F, CLK.V, CLK.PauseBreak,CLK.PageUp,CLK.PageDown,CLK.RightArrow]
    wave6 = [CLK.F4, 18, CLK.T,CLK.G, CLK.B, CLK.Space, CLK.ScrollLock,CLK.Home, CLK.End, CLK.UpArrow, CLK.DownArrow]
    wave7 = [19, CLK.Y, CLK.H, CLK.N,CLK.PrintScreen, CLK.Insert,CLK.Delete, CLK.LeftArrow]
    wave8 = [CLK.F5, 20, CLK.U, CLK.J, CLK.M, CLK.F12, CLK.Backspace, CLK.Backslash, CLK.Enter, CLK.RightShift,CLK.RightCtrl, CLK.Application]
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
            
