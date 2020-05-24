#coding:utf8
li = [20,15,10,15,10,5]
class h(object):
    def __init__(self,num,Q,q,l=None,t=None,child=None):
        self.num = num
        self.Q = Q-q
        self.q = q
        self.l = l
        self.t = t
        if self.l and self.t:
            self.l = self.Q/2
            self.t = self.Q/2
            if child:
                self.change(child)
            while self.l <= 0:
                self.l += 2
                self.t -= 2
            while self.t <= 0:
                self.t += 2
                self.l -= 2
        elif self.l:
            self.l = self.Q
        elif self.t:
            self.t = self.Q
    def getnum(self):
        print(self.num,'点流量为：')
        if self.l and self.t:
            print('l分配流量:',self.l)
            print('t分配流量:',self.t)
        elif self.l:
            print('l分配流量:',self.l)
        elif self.t:
            print('t分配流量:',self.t)
            print('节点流量:',self.q)
    def change(self,child):
        for k,v in child.items():
            if k=='t':
                tmin = sum([li[x] for x in v['c']])
                tmax = tmin + sum([li[x] for x in v['a']])
                while self.t <= tmin:
                    self.t += 5
                    self.l -= 5
                while self.t > tmax:
                    self.t -= 5
                    self.l += 5
            elif k=='l':
                lmin = sum([li[x] for x in v['c']])
                lmax = lmin + sum([li[x] for x in v['a']])
                while self.l <= lmin:
                    self.l += 5
                    self.t -= 5
                while self.l > lmax:
                    self.l -= 5
                    self.t += 5
def two():
    d1 = {
        't':{'c':[1,2],'a':[5,]},
        'l':{'c':[3],'a':[4,5]}
        }
    d2 = {
        't':{'c':[2,],'a':[5,]},
             }
    h1 = h(0,75,20,True,True,d1)
    h2 = h(1,h1.t,15,True,True,d2)
    h3 = h(2,h2.t,10,True)
    h4 = h(3,h1.l,15,t=True)
    h5 = h(4,h2.l+h4.t,10,t=True)

    h1.getnum()
    print('\n')
    h2.getnum()
    print('\n')
    h3.getnum()
    print('\n')
    h4.getnum()
    print('\n')
    h5.getnum()
if __name__=='__main__':
    two()
