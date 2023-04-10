import random
import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed("q") == False:
    # region=(585,435,750,535)
    # center colour: (255, 219, 195)

    ss = pyautogui.screenshot(region=(585,435,750,535)) 
    width, height = ss.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r,g,b = ss.getpixel((x,y))

            if b == 195:
                print("clik")
                click(x+585, y+435)
                #time.sleep(0.1)
                break
