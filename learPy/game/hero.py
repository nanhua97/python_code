
import sys

class Hero(object):
    def __init__(self,usr,pwd):
        self.name = usr
        self.pwd = pwd
        self.hp = 100
    def change_Pwd(self):
        while True:
            old_Pwd = input('please input old password:')
            if old_Pwd != self.pwd:
                print('Your password is wrong and please try again')
            else:
                new_Pwd = input('Please input new password:') 
                self.pwd = new_Pwd
                return False
