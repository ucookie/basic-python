#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

def listen():
    for i in range(6):
        print('---认真听课')

def note():
    for i in range(3):
        print('>>>做笔记')

if __name__ == '__main__':
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=note)
    t1.start()
    # 控制线程执行顺序
    # time.sleep(1)

    t2.start()
    # time.sleep(1)

    print(threading.enumerate())
