#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def note():
    for i in range(3):
        print('做笔记')
        time.sleep(1)

def listen():
    for i in range(3):
        print('认真听课')
        time.sleep(1)

if __name__ == '__main__':
    begin_time = time.time()
    note()
    listen()
    print('执行时间:%.4f' % (time.time() - begin_time))
