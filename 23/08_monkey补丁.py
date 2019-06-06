#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import gevent
from gevent import monkey

monkey.patch_all()

def create(n):
    print(n)
    time.sleep(0.5)

while True:
    g1 = gevent.spawn(create, 1)
    g2 = gevent.spawn(create, 2)
    g3 = gevent.spawn(create, 3)

    g1.join()
    g2.join()
    g3.join()
