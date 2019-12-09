#! usr/bin/env python3
# -*- conding:utf-8 -*-
#参考链接：https://segmentfault.com/a/1190000013959213?utm_source=channel-hottest

import struct

a=b'hello'
b=b'world!'
c=2
d=45.123
bytes = struct.pack('5s6sif',a,b,c,d) 
print(struct.unpack('5s6sif',bytes))

'''
数据格式
名字  职业   年
muyu  coder 2018
'''

name = b'muyu'
job = b'coder'
year = 2018


file = open(r'backup\2.txt', 'wb+')

file.write(struct.pack('4s5si', name, job, year))
file.flush()

file.seek(0)

strBin = file.read()
print(strBin) # b'muyucoder\x00\x00\x00\xe2\x07\x00\x00'

content = struct.unpack('4s5si', strBin)
print(content) # (b'muyu', b'coder', 2018)