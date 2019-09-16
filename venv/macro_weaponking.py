import numpy as np
import random
import time
import cv2
import mss
import pyautogui as pag

pag.PAUSE = 0.08

fail_limit = 10
initial_delay = 0.08

# BlueStacks

# left_icon_pos = {
#     'left': 92.5,
#     'top': 553,
#     'width': 85,
#     'height': 85
# }
#
# right_icon_pos = {
#     'left': 244.5,
#     'top': 553,
#     'width': 85,
#     'height': 85
# }

left_icon_pos = {
    'left': 100,
    'top': 560,
    'width': 70,
    'height': 70
}

right_icon_pos = {
    'left': 250,
    'top': 560,
    'width': 70,
    'height': 70
}

leftButton = [70, 680]

rightButton = [355, 680]


# with mss.mss() as sct:
#     leftImage = np.array(sct.grab(left_icon_pos))[:, :, :3]
#     rightImage = np.array(sct.grab(right_icon_pos))[:, :, :3]
#
#     cv2.imshow('left_img', leftImage)
#     cv2.imshow('right_img', rightImage)
#     cv2.waitKey(0)

def compute_icon_type(img):

    result = None

    mean = np.mean(img, axis=(0, 1))

    if mean[0] > 50 and mean[0] < 55 and mean[1] > 50 and mean[1] < 55 and mean[2] > 50 and mean[2] < 55:
        result = 'BOMB'
    elif mean[0] > 250 and mean[1] > 85 and mean[1] < 110 and mean[2] > 250:
        result = 'SWORD'
    elif mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
        result = 'POISON'
    elif mean[0] > 210 and mean[0] < 230 and mean[1] > 200 and mean[1] < 225 and mean[2] > 120 and mean[2] < 135:
        result = 'JEWEL'

    return result


def click(coords):
    # pag.moveTo(x=coords[0], y=coords[1], duration=0.0)
    # pag.moveDown()
    # pag.moveUp()
    pag.click(x=coords[0], y=coords[1], interval=random.uniform(0.05001, 0.08001))


if __name__ == "__main__":
    # countdown(3)
    n_fail = 0
    n_frame = 0
    fever = False
    last_fever = time.time()
    last_icons = []

    while True:
        n_frame += 1

        if fever and time.time() - last_fever > 10:
            print('############### FEVER ################')
            click(leftButton)

            if time.time() - fever > 5:
                fever = False
                last_fever = time.time()
            else:
                continue

        with mss.mss() as sct:
            leftImage = np.array(sct.grab(left_icon_pos))[:, :, :3]
            rightImage = np.array(sct.grab(right_icon_pos))[:, :, :3]

            # cv2.imshow('leftImage', leftImage)
            # cv2.imshow('rightImage', rightImage)
            # cv2.waitKey(0)

            leftIcon = compute_icon_type(leftImage)
            rightIcon = compute_icon_type(rightImage)

            if leftIcon == 'SWORD' and (rightIcon == 'BOMB' or rightIcon == 'POISON'):
                print('LEFT CLICK!')
                click(leftButton)
                n_fail = 0
            elif rightIcon == 'SWORD' and (leftIcon == 'BOMB' or leftIcon == 'POISON'):
                print('RIGHT CLICK!')
                click(rightButton)
                n_fail = 0
            elif leftIcon == 'JEWEL' and rightIcon == 'JEWEL':
                print('##########FEVER##########')
                click(leftButton)
                # click_jewel(rightButton)
                n_fail = 0
                fever = time.time()
            else:
                # print('FAIL')
                n_fail += 1
                if n_fail > fail_limit:
                    print('failed %s times, terminate!' % (fail_limit))
                    break

            time.sleep(initial_delay)
'''
while True:
    # x, y = pag.position()
    # positionStr = 'X:' + str(x) + ", Y: " + str(y)
    # print(positionStr)

    with mss.mss() as sct:
        leftImage = np.array(sct.grab(left_icon_pos))[:, :, :3]
        rightImage = np.array(sct.grab(right_icon_pos))[:, :, :3]

        # cv2.imshow('leftImage', leftImage)
        # cv2.imshow('rightImage', rightImage)
        # cv2.waitKey(0)

        leftIcon = compute_icon_type(leftImage)
        rightIcon = compute_icon_type(rightImage)

        if leftIcon == 'SWORD':  # and (rightIcon == 'BOMB' or rightIcon == 'POISON'):
            print('LEFT CLICK!')
            click(leftButton)
        elif rightIcon == 'SWORD':  # and (leftIcon == 'BOMB' or leftIcon == 'POISON'):
            print('RIGHT CLICK!')
            click(rightButton)
        elif leftIcon == 'JEWEL' and rightIcon == 'JEWEL':
            print('FEVER!')
            click(leftButton)
            click(rightButton)
        else:
            print('FAIL')
'''
