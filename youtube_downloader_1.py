import pytube
import os
import subprocess


yt = pytube.YouTube("https://www.youtube.com/watch?v=2a5zTTYaNl8")

videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)):
    print (i , ' , ' , videos[i])

cNum =  int(input("다운 받을 화질은? 0~21 입력"))

down_dir = "/Users/Apple/youtube"
videos[cNum].download(down_dir)

newFileName = input("변환할 mp3 파일 이름은")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])

print ("동영상 다운로드 및 mp3 변환 완료!!! ")
