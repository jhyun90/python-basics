import time


def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(min, sec)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1


countdown(63)
exit()
