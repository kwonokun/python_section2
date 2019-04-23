
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("Users/Apple/food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")


a = soup.select("ul#fd-list" > h1)
print(a) #각 li 태그 그룹의 4번째 요소 선택
