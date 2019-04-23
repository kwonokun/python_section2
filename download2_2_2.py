import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120317_88/myson8089_1331951685563u2mS8_JPEG/cute-dog.jpghttp://blogfiles.naver.net/20120317_88/myson8089_1331951685563u2mS8_JPEG/cute-dog.jpg"
htmlURL = "http://google.com"

savePath1 = "/Users/Apple/section2/zzz/test1.jpg"
savePath2 = "/Users/Apple/section2/zzz/index.html"

f =dw.urlopen(imgUrl).read()
f2 =dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') #w:write r:read a:add
saveFile1.write(f)
saveFile1.close()


with open(savePath2 ,'wb') as saveFile2:
    saveFile2.write(f2)

print ("다운로드 완료")
