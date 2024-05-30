# ONly for single video
from pytube import YouTube

link = input("Enter the links of video: ")
youtube_1 = YouTube(link)     # gets all the information of video

# print(youtube_1.title)  
# print(youtube_1.thumbnail_url)
# video = youtube_1.streams.all()   # All format
# video = youtube_1.streams.filter(only_audio=True)  # only for audio

video = youtube_1.streams.filter(progressive=True)  #both audio and video

vid = list(enumerate(video))   # gives with index number
for i in vid:
    print(i)

print()
strm = int(input("Enter the number which you want to download: "))
video[strm].download()
print("Successffully Downloaded!!!")


#   *******Download all playlist videos*****
# from pytube import Playlist
# playlistLink = input("Enter the playlist link: ")
# py = Playlist(playlistLink)

# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()

