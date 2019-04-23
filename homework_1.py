import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl1 = "https://ssl.pstatic.net/tveta/libs/1224/1224991/80c8dcf25bdb64b7aa56_20190314153543828.jpg"

htmlURL1 = "https://ssl.pstatic.net/tveta/libs/1231/1231533/660d6437ee1c0e7bec67_20190306145015915.jpg"

savePath1 = "/Users/Apple/section2/zzz/test1.jpg"
savePath2 = "/Users/Apple/section2/zzz/index2.jpg"

f =dw.urlopen(imgUrl1).read()
f2 =dw.urlopen(htmlURL1).read()

saveFile1 = open(savePath1,'wb') #w:write r:read a:add
saveFile1.write(f)
saveFile1.close()


with open(savePath2 ,'wb') as saveFile2:
    saveFile2.write(f2)

print ("다운로드 완료")
