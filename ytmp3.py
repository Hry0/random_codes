from __future__ import print_function
from cgi import print_arguments
import imp
from pytube import YouTube
import os
print("\n Youtybe video to mp3")
URL=input("Enter the URL")
yt=YouTube(URL)
try:
    print("\nDownloading..")
    video=yt.streams.filter(only_audio=True).first()
    out_file=video.download()
    base, ext=os.path.splittext(out_file)
    new_file = base+".mp3"
    os.rename(out_file, new_file)
    print("\nsuccessfully downloaded")
except:
    print("something went wrong!")

    