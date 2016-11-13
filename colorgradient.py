def SetKeyboardMood2(algonumber):
    if algonumber >= 75 and algonumber <= 100: #Red to yellow from 100-75
        SetKeyboardColor(255, int(-10.2*algonumber+1020), 0)
    elif algonumber >= 50 and algonumber < 75: #Yellow to white from 75-50
        SetKeyboardColor(255, 255, int(-10.2*algonumber+765))
    elif algonumber >= 25 and algonumber < 50: #White to green from 50-25
        SetKeyboardColor(int(10.2*algonumber-255), 255, int(10.2*algonumber-255))
    elif algonumber >= 0 and algonumber < 25: #Green to blue from 25-0
        SetKeyboardColor(0, int(10.2*algonumber), int(-10.2*algonumber+255))
