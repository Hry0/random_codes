from bdb import Breakpoint
from rich import print
import glob
import random
import vlc
import random
import sys
from tinytag import TinyTag
print("Program to play your favourite song:")
folder="C://users//acer//music"
import glob
Path=glob.glob("C://users//acer//music/*.mp3")
Names=[]
for x in Path:
    x=x.split("\\")[1][:-4]
    Names.append(x)
l=len(Names)
for i in range(1,l+1):
    print(i,"|",Names[i-1])
nL=[]
h=0
ply=vlc.MediaPlayer()
while True:
    nL=[]
    z=input("Enter the number to play the song or enter 'S' to create a shuffled playlist or 'Q' to quit:")
    ply.stop()
    if z.isdigit() and int(z)<=len(Names):
        n=int(z)
        x=Path[n-1]
        ply=vlc.MediaPlayer(x)
        ply.play()
    elif z=='s' or z=='S':
        Shuffled_playlist=Path
        random.shuffle(Shuffled_playlist)
        i=1
        while i<=len(Shuffled_playlist):
            print("-"*78)
            print("Playing:",Shuffled_playlist[i-1].split("\\")[1])
            print("="*78)
            print("The next three songs are:")
            add=0
            for k in range(3):
                print("\t",k+1,Shuffled_playlist[i+add].split("\\")[1])
                add+=1
            print("="*78)
            ply=vlc.MediaPlayer(Shuffled_playlist[i-1])
            ply.play()
            next_song=input("Enter '>' to play nxt songs or 'q' to quit:")
            if next_song==">" or "`":
                ply.stop()
            else:
                break
            i+=1
    elif z=='q' or z=="Q":
        break
    else:
        print("Invalid Input!!!!")
    h+=1


    
