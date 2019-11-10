from pytube import YouTube
yt = YouTube('')
print('downloading...', yt.title)
print(yt.streams.all())
video = yt.streams.first()
video.download()
print('download completed')