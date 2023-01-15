from pytube import YouTube
url=input("Enter the URL:")
my_vid=YouTube(url)
print(my_vid.title)
print(my_vid.thumbnail_url)
my_vid = my_vid.streams.get_highest_resolution()
# my_vid=my_vid.streams.first()
# for stream in my_vid.streams:
#     print(stream)
my_vid.download()
