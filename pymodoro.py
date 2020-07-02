import time
import winsound


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t -= 1

def pomo():
    counter = 0
    while counter < 4:
        print("work time!")
        winsound.PlaySound("*", winsound.SND_ALIAS)
        countdown(1500)
        print("break time!")
        winsound.PlaySound("*", winsound.SND_ALIAS)
        countdown(300)
        counter += 1
    print("long break time!")
    winsound.PlaySound("*", winsound.SND_ALIAS)
    countdown(600)
    counter = 0