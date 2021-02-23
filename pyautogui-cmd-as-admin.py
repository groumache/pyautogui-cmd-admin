import pyautogui
import time

def try_click_admin():
    try:
        pyautogui.click('01-admin-cmd.PNG')
        return False
    except:
        return True

##########################
pyautogui.FAILSAFE = False
##########################

pyautogui.click('00-windows-search.PNG')
pyautogui.write('cmd')
while try_click_admin(): time.sleep(1)

# the following  does not work
# pyautogui.click('02-oui-button.PNG')

x, y = pyautogui.position()
print(f"position -- x = {x}, y = {y}")
x, y = pyautogui.size()
print(f"screen size -- x = {x}, y = {y}")

x = (x // 2) - 100
y = (y // 2) + 110

pyautogui.moveTo(x, y)

# the following doesn't work
# pyautogui.mouseDown()
# time.sleep(1)
# pyautogui.mouseUp()

# the following doesn't work
# time.sleep(1)
# pyautogui.click()

# the following doesn't work
time.sleep(1)
pyautogui.press('left')
pyautogui.press('enter')
