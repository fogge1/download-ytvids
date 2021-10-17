# need to install pytube with pip
from pytube import YouTube

url = input("url: ")
yt = YouTube(url)

formats = yt.streams.all()

video = list(enumerate(formats))

for i in video:
    print(i)

option = int(input("Choose the format: "))

dl = formats[option]
dl.download()