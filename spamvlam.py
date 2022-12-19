import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()


def init():
    with pyautogui.hold('command'):
        pyautogui.press('tab')

def spam():
    i = 0
    while i<1000:
        pyautogui.write('VIHAAN LOOKS LIKE TERRANCE')
        pyautogui.press('enter')
        pyautogui.write('IMMA TAKE SPAN 2 OVER EL VERANO')
        pyautogui.press('enter')
        i+=1

def go():
    init()
    time.sleep(10)
    spam()

go()