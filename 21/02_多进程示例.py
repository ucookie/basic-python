#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process

p = Process(target=note)
p = Process(target=listen)
p.start()