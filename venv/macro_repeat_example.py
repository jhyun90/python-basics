import pyautogui as pag
import random
import time

button = {
    'top_left': {
        'x': 342,
        'y': 152
    },

    'bottom_right': {
        'x': 398,
        'y': 199
    }
}

while True:
    pag.moveTo(
        x=random.uniform(button['top_left']['x'], button['bottom_right']['x']),
        y=random.uniform(button['top_left']['y'], button['bottom_right']['y']),
        duration=random.uniform(0.5, 1.5)
    )

    pag.mouseDown()
    time.sleep(random.uniform(0.15000, 0.29888))
    pag.mouseUp()
    time.sleep(random.uniform(0.21000, 0.42990))

# while True:
#     x, y = pag.position()
#     print('x: %s, y: %s' % (x, y))
