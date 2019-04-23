from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_fuc(selecter):
    print("car_fuc", soup.select_one(selecter).string)

car_fuc("#gr")
