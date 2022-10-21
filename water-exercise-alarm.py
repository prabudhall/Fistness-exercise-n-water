# program to drink water after every 30 minute and to eyes and physical exercise

from pygame import mixer
from datetime import datetime
from time import time

f = open("fitness.txt", "a")
f.close()


def log(str):
    with open("fitness.txt", "a") as f:
        f.write(f"{datetime.now()} : {str} done\n")


def playstop(mp3, stop):
    mixer.init()
    mixer.music.load(mp3)
    mixer.music.play()
    while True:
        st = input(f"Enter the {stop} to stop : ")
        if st == stop:
            mixer.music.stop()
            log(stop)
            break


wwt = time()
eet = time()
ppt = time()
wt = 5
et = 10
pt = 20
while True:
    if time() - wwt > wt:
        playstop("The War of the Worlds - BBC Dramatisation.mp3", "drink")
        wwt = time()

    if time() - eet > et:
        playstop("The War of the Worlds - BBC Dramatisation.mp3", "eyes")
        eet = time()

    if time() - ppt > pt:
        playstop("The War of the Worlds - BBC Dramatisation.mp3", "phy")
        ppt = time()
