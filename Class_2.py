import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def funstion1():
        print("funtion1 called!!")

    def funstion2(self):
        print("funtion2 called!!")

f = SelfTest()
print(id(f))

f.funstion2()

print(SelfTest.funstion1())
