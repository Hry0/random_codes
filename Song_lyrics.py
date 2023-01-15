from lyrics_extractor import SongLyrics
 
# pass the GCS_API_KEY, GCS_ENGINE_ID
extract_lyrics = SongLyrics("AIzaSyD3dqOHjGHdYbZh8MFUkQ5Oe1LDMypJLLY","a4f659f57c0948701")
song=input("Enter tye name of the song you want to get lyrics:")
a=extract_lyrics.get_lyrics(song)
title=a.get("title")
lyrics=a.get("lyrics")
print("="*25,title,"="*25)
print(lyrics)
f=input("Name the file to which you want to save the lyrics to:")
with open(f,"w+",errors='ignore') as fl:
    fl.write("\t"*5+title)
    fl.write("\n\n"+lyrics)
    fl.close()