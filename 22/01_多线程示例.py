#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

def listen():
    for i in range(3):
        print('认真听课')
        time.sleep(1)

def note():
    for i in range(3):
        print('做笔记')
        time.sleep(1)

if __name__ == '__main__':
    print('-----直接调用-----')
    listen()
    note()
    print('-----多线程执行-----')
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=note)
    t1.start()
    t2.start()
