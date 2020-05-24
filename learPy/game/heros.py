#! usr/bin/env python3
# -*-coding:utf-8-*-
'heros-1.0'
__author__='nanhua'
import random
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
    def mes(self):
        print([self.name,self.hp])
    def apple(self):
        self.hp += 10
        self.mes()
account = input('Do you have a account?')
if account == 'no':
    username = input('Please input your name:')
    password = input('Please input your password:')
    username = username if username else 'player01'
    password = password if password else '123456'
    mes = Hero(username,password)
    f=open('player01','w')
    f.write('%s\n%s'%(username,password))
    f.close()
elif account == 'yes':
    username = input('Please input your name:')
    password = input('Please input your password:')
    mes = Hero(username,password)
    f=open('player01','w')
    f = open('player01','r')
    k = f.read().split('\n')
    f.close()
    if username == k[0] and password == k[1]:
        pass
    if username != k[0]:
        print('user not found')
        quit()
    if password != k[1]:
        print('password is wrong')
        quit()
world = (
	[(0,0),(0,1),(0,2)],
	[(1,0),(1,1),(1,2)],
	[(2,0),(2,1),(2,2)]
	)
a = 0
b = 0
mes.mes()
print(world[a][b])
while True:
    oper = input('Please input your operating:')
    if oper == 'q':
        break
    elif oper == 'w':
        a = a if a-1<0 else a-1
    elif oper == 's':
        a = a if a+1>2 else a+1
    elif oper == 'a':
        b = b if b-1<0 else b-1
    elif oper == 'd':
        b = b if b+1>2 else b+1
    appA = random.randint(0,2)
    appB = random.randint(0,2)
    if a == appA and b == appB:
        mes.apple()
    print(world[a][b])
