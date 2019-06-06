#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

def th():
    while True:
        pass

if __name__ == '__main__':
    t1 = threading.Thread(target=th)
    t1.start()
    t2 = threading.Thread(target=th)
    t2.start()
