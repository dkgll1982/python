#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-17 14:47
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : mydict
# @Software: PyCharm

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value