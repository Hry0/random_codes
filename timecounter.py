import time
from playsound import playsound
t=int(input("How many secs"))
while t:
    mins=t//60
    secs=t%60
    timer="{:02d}:{:02d}".format(mins,secs)
    print(timer,end=" ")
    time.sleep(1)
    t-=1
playsound("C:\\Users\\acer\\Music\\Arcade.mp3")

