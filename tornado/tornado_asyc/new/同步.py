#coding:utf8

def req_a():
    print("start_A")
    print("A_end")

def req_b():
    print("start_B")
    print("B_end")

def main():
    #模拟tornado框架
    req_a()
    req_b()

if __name__ == "__main__":
    main()
