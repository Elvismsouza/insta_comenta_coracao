import pyautogui
from time import sleep

pyautogui.moveTo(1034,281,duration=2)
for i in range(100):
    sleep(0.5)
    pyautogui.click()
