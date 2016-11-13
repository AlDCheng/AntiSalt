def Transition(algonumber1, algonumber2):
    algonumber = algonumber1
    delta = abs(algonumber2 - algonumber1)
    interval = ?

    while (algonumber2 > algonumber):
        SetKeyboardMood(algonumber)
        algonumber += 1
        time.sleep(interval/delta)
    while (algonumber2 < algonumber):
        SetKeyboardMood(algonumber)
        algonumber -= 1
        time.sleep(interval/delta)
