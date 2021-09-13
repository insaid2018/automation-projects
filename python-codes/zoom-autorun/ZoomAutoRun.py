import time
import pyautogui

# Zoom's webinar ID; Example: https://us02web.zoom.us/j/82128916384
webinar_id = '82128916384'

# pyautogui.mouseInfo(); To check screen coordinates
pyautogui.click(x=70, y=750, duration=0.25)

time.sleep(2)
pyautogui.write(message='Zoom')

time.sleep(2)
pyautogui.press('Enter')

time.sleep(2)
pyautogui.getWindowsWithTitle(title='Zoom')[0].maximize()

time.sleep(2)
pyautogui.click(x=535, y=300, duration=0.25)

time.sleep(2)
pyautogui.click(x=570, y=330, duration=0.25)

time.sleep(4)
pyautogui.write(message=webinar_id)

time.sleep(2)
pyautogui.press('Enter')