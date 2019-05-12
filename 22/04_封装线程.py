#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)

if __name__ == '__main__':
    t = MyThread()
    t.start()
