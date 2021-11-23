from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for i in range(0, 500):
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.shift)
    keyboard.tap("n")

keyboard.release(Key.ctrl_l)
