# This script will simulate a mouse click on a screen location selected
# by the user on a recurring basis.
# Select the preferred number of minutes in the period by changing the variable 'period'.
# Requirements: pynput, pyautogui

# Begin User Definition Area
ENABLE_MOUSE_CLICK_SIMULATOR = True
mouse_click_period = 1 # Number of minutes between mouse clicks
#period = 60 # number of minutes between mouse clicks

# End User Definition Area
 
from pynput import mouse
import pyautogui as pg
import time

def on_click(x, y, button, pressed):
    global xvar
    global yvar
    if button == mouse.Button.left:
        xvar = x
        yvar = y
        return False

# Declare global variables
xvar = 1
yvar = 1
previous_mouse_click_time = time.time()


if ENABLE_MOUSE_CLICK_SIMULATOR:
# Display alert screen
    pg.alert('Click OK, then click the desired mouse click location on the screen.')

# Start listener for mouse clicks
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()

# Start mouse click timer operation
    while True:
        if time.time() > (mouse_click_period * 60) + previous_mouse_click_time:
            pg.click(xvar, yvar)
            t = time.localtime()
            current_time = time.strftime("%c", t)
            print('Mouse click at:', current_time)
            print('Next mouse click in '+ str(mouse_click_period) + ' minute(s).')
            previous_mouse_click_time = time.time()
