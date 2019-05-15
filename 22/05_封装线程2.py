#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

class MyThread(threading.Thread):
    '''封装多线程库'''

    def task(self, num):
        print('执行任务', num)

    def run(self):
        for i in range(3):
            self.task(i)
            time.sleep(1)

if __name__ == '__main__':
    t = MyThread()
    t.start()
    t.start()
