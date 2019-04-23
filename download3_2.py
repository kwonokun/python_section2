import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api.ipify.org"

values = {
   'format':'json'
}
print ('before', values)

parans = urlencode(values)
print('after',parans)

url = API +"?" +parans
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
