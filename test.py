import pyautogui
from time import sleep

sleep(5)
print("starting")
pyautogui.click(100, 100)
pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
print("theEnd")