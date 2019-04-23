import pytube


yt = pytube.YouTube("https://www.youtube.com/watch?v=NBOcb-sDCs0")

videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)):
    print (i , ' , ' , videos[i])

down_dir = "/Users/Apple/youtube"
videos[0].download(down_dir)
