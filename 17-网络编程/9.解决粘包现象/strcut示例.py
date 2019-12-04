#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-26 10:17
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : strcut示例.py
# @Software: PyCharm

import struct
 
bit = struct.pack('q', 1020040099)
print(bit,len(bit),hex(1020040099))
 

res = struct.pack('4s5si',b'muyu',b'hello',1234)
print(struct.calcsize('4s5si'),res, type(res), len(res)) 

res = struct.pack('2si',b'qw', 123)
print(res, type(res), len(res))  # b'{\x00\x00\x00' <class 'bytes'> 4 封装一个4个字节的包

res1 = struct.pack('q', 11122232323)
print(res1, type(res1), len(res1))  # b'\x03\xcc\xef\x96\x02\x00\x00\x00' <class 'bytes'> 8 封装一个8个字节的包

#print(struct.unpack('i', res)[0])  # 拆包
print(struct.unpack('q', res1)[0])  #

str = struct.pack('4s',b'asds')
print(str,type(str),len(str))