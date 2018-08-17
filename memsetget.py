#!/usr/bin/env python3
# coding:utf8
import memcache

# 链接
mc = memcache.Client(['106.3.44.26:11211'], debug=True)
# 读取
ret = mc.get('57a39686f32b02aa344132121ba1ecac')
print(ret)
