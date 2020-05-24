#coding:utf8

import time
import thread

def req_IO(callback):
    def fun(cb):
        print("start_IO")
        time.sleep(5)
        print("IO_end")
        cb("io result")
    thread.start_new_thread(fun,(callback,))
def on_finish(ret):
    print("start_finish")
    print("ret: %s" % ret)
    print("end_finish")
def req_a():
    print("start_A")
    req_IO(on_finish)
    print("A_end")

def req_b():
    print("start_B")
    print("end_B")

def main():
    #模拟tornado框架
    req_a()
    req_b()
    while 1:
        pass

if __name__ == "__main__":
    main()
