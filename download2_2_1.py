import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120317_88/myson8089_1331951685563u2mS8_JPEG/cute-dog.jpghttp://blogfiles.naver.net/20120317_88/myson8089_1331951685563u2mS8_JPEG/cute-dog.jpg"
htmlURL = "http://google.com"

savePath1 = "/Users/Apple/section2/zzz/test1.jpg"
savePath2 = "/Users/Apple/section2/zzz/index.html"

dw.urlretrieve (imgUrl,savePath1)
dw.urlretrieve (htmlURL,savePath2)

print ("다운로드 완료")
#저장->open('r')->변수할당->파싱->저장 [그냥 여러 data를 한번에 다운받겠다]
