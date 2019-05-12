#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

def listen():
    for i in range(9):
        print('---认真听课')
        time.sleep(1)

def note():
    for i in range(4):
        print('>>>做笔记')
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=note)
    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        length = len(threading.enumerate())
        if length <= 1:
            break
        time.sleep(0.5)