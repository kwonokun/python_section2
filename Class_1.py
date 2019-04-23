import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("ggggg")

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("----------------")
        print("Name:   " + self.name)
        print("Phone:   " + self.phone)
        print("----------------")

    def __del__(self):
        print("delete!!")

user1 = UserInfo("kim","010-2323-3333")
user2 = UserInfo("kwon","010-2323-4444")

print(id(user1)) #4476371688
print(id(user2)) #4476371744

#user1.set_info("kim","112123")
#user2.set_info("park","9889877")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
