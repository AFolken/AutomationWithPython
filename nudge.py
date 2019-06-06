import pyautogui, time

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get the mouse coordinates.
        x, y = pyautogui.position()
        # move mouse 3 pixles up
        pyautogui.moveTo(x, y-3, duration=0.25)
        pyautogui.moveTo(x, y+3, duration=0.25)
        # wait time before moving again
        time.sleep(5)#300 for 5 min

except KeyboardInterrupt:
    print('\nDone.')

# use the following command to run the script
# exec(open("H:\\My Documents\\Python Learning\\automate_online-materials\\nudge.py").read())
