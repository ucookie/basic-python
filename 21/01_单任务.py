#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def note():
    for i range(3):
        print('做笔记')
        time.sleep(1)

def listen():
    for i range(3):
        print('认真听课')
        time.sleep(1)

def main():
    note()
    listen()

if __name__ == '__main__':
    main()