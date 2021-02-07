import pyautogui
import time

time.sleep(5)
f = open('spam_text', 'r')

for word in f:
    while True:
        pyautogui.write(word)
        pyautogui.press('enter')