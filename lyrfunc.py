def Lyrical(song):
    from lyrics_extractor import SongLyrics
    # pass the GCS_API_KEY, GCS_ENGINE_ID
    extract_lyrics = SongLyrics("AIzaSyD3dqOHjGHdYbZh8MFUkQ5Oe1LDMypJLLY","a4f659f57c0948701")
    text=extract_lyrics.get_lyrics(song)
    lyrics=text.get("lyrics")
    return lyrics
if __name__=="main":
    import glob
    import os
    cd=('C:\\Users\\acer\\Music')
    List_songs=glob.glob("C://users//acer//music/*.mp3")
    for song in List_songs:
        x=os.path.basename(song)
        name=x[:-4]
        print(name)
        text=Lyrical(name)
        print(text)
        print("-"*69)

            