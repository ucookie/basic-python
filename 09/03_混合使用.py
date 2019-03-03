#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mix(param, *args, default='end', **kwargs):
    print(param)
    print(default)
    print(args)
    print(kwargs)

mix(1,2,3,4,index=5, lenth=6)
