import eyed3
track = eyed3.load("C:\\Users\\acer\\Music\\Badshah, Nikhita Gandhi - Jugnu.mp3")
tag = track.tag
artist = tag.artist
lyrics = tag.lyrics[0].text
print(artist)
print(lyrics)