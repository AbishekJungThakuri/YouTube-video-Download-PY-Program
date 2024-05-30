# ONly for single video

from pytube import YouTube

link = "https://www.youtube.com/watch?v=hWhyIwOXuGo"
youtube_1 = YouTube(link)     # gets all the information of video

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

video = youtube_1.streams.all()   # All format
# video = youtube_1.streams.filter(only_audio=True)  # only for audio

vid = list(enumerate(video))   # gives with index number
for i in vid:
    print(i)

print()
strm = int(input("Enter: "))
video[strm].download()
print("Successffully Downloaded!!!")


#   *******Download all playlist videos*****

# from pytube import Playlist

# py = Playlist("https://www.youtube.com/playlist?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12")

# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()

