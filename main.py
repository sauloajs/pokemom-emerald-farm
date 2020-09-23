import pyautogui
import pydirectinput

def move():
    pyautogui.PAUSE = 1.5
    pydirectinput.press('left', presses=1)
    pydirectinput.press('right', presses=1)
    checkEncounter()

def checkEncounter():
    pyautogui.PAUSE = 2.5
    encounter = pyautogui.locateOnScreen('./encounter.PNG', grayscale=True, confidence=0.5)
    if(encounter):
        pydirectinput.press('x', presses=10, interval=0.5)
        move()
    else:
        move()

move()
