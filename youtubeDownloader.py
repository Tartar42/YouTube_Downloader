from pytube import YouTube
from sys import argv

#way we are going to access the link from the command line in a python code is using this:
link = argv[0]
# argv takes all the things you input in the command line when you are running this programm. The first argument is
# allways the name of the programm ( argv[0] ). argv[1] = first command  line in an argument which we give when we
# are on this programm
yt = YouTube(link)
# creates YouTube-Object from this link 

print("Title: " + yt.title)
print("Views: " + str(yt.views))
print("Views: " + str(yt.views))

# tipp: when you run python3 youtubeDownloader.py yt."(link)", make sure of the "yt"!!

# Problem solved: 

yd = yt.streams.get_highest_resolution()

yd.download("C:\\Users\\tarsi\\Downloads\\YoutTubeDownloads")

# sources:

# YouTube Video with the tutorial
# https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=4&t=552s
# 
# Problems solved: python -m pip install --upgrade pytube (on terminal)
# https://stackoverflow.com/questions/68956373/i-was-making-a-youtube-video-downloader-but-pytube-is-giving-error



# where u stopped: tempCodeRunnerFile keeps apearing. how to remove? -> please google