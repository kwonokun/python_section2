import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com/"

mem = req.urlopen(url)

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#print ("geturl", mem.geturl())
#print ("status", mem.status)#200(정상) 404(없음) 403(접속 거절) 500(서보에러)
#print("headers", mem.getheaders())
#print("info", mem.info())
#print("code",mem.getcode())
#print("read", mem.read(50).decode("utf-8"))
print(urlparse("https://www.naver.com/?test=test"))
