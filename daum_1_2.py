from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url= "http://finance.daum.net/domestic/market_cap"
res = req.urlopen(url).read() #.decode('euc-kr')
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("td.first")
print(top10)
