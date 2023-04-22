from pytube import YouTube
from sys import argv

#way we are going to access the link from the command line in a python code is using this:
link = argv[0]
# argv takes all the things you input in the command line when you are running this programm. The first argument is
# allways the name of the programm ( argv[0] ). argv[1] = first command  line in an argument which we give when we
# are on this programm
yt = YouTube(link)
# creates YouTube-Object from this link 

print("Title: ", yt.title)

print("Views: ", yt.views)

# tipp: when you run python3 youtubeDownloader.py yt."(link)", make sure of the "yt"!!

yd = yt.streams.get_highest_resolution()

yd.download("C:\\Users\\tarsi\\Downloads\\YoutTubeDownloads")