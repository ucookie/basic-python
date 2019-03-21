#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Model(object):

    @classmethod
    def test(cls):
        with open('data/id.csv', 'r') as f:
            print(f.read())