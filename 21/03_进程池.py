#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import multiprocessing

# 全局队列
QUEUE = multiprocessing.Manager().Queue()

def listen():
    global QUEUE
    for i in range(3):
        print('认真听课')
        QUEUE.put('课程内容%d' % i)
        time.sleep(1)

def note():
    global QUEUE
    while True:
        print('笔记:', QUEUE.get())
        time.sleep(0.1)

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    pool.apply_async(listen)
    pool.apply_async(note)
    pool.close()
    pool.join()
