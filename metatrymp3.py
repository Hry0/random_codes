import eyed3
import glob
import os
import lyrfunc
cd=('C:\\Users\\acer\\Music')
List_songs=glob.glob("C://users//acer//music/*.mp3")
for song in List_songs:
     x=os.path.basename(song)
     name=x[:-4]
     track = eyed3.load(song)
     tag = track.tag
     try:
          lyrics = tag.lyrics[0].text
          print("ya got it")
     except IndexError:
          lyric=lyrfunc.Lyrical(name)
          track.tag.lyrics = lyric
          track.tag.save()
          print('-'*78)


     
     

