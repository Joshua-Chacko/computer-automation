import pyautogui
import time

pyautogui.press('win')
pyautogui.hotkey('c','h','r','o','m','e')
pyautogui.press('enter')
with pyautogui.hold('ctrl'):
    with pyautogui.hold('shift'):
        pyautogui.press('t')