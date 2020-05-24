#coding:utf8

import time

def req_IO():
    print("start_IO")
    time.sleep(5)
    print("IO_end")
    return "IOisEnd"

def req_a():
    print("start_A")
    ret = req_IO()
    print("ret:%s" % ret)
    print("A_end")

def req_b():
    print("start_B")
    print("end_B")

def main():
    #模拟tornado框架
    req_a()
    req_b()

if __name__ == "__main__":
    main()
