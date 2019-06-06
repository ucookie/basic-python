#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing

def pr():
    while True:
        pass

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=pr)
    t1.start()
    t2 = multiprocessing.Process(target=pr)
    t2.start()
