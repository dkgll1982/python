#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 16:29
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 编码
# @Software: PyCharm

import  chardet;

print(chardet.detect(b'Hello, world!'))
data='天王盖地虎,小鸡炖蘑菇'.encode('GBK')
print(data,chardet.detect(data))
#{'language': 'Chinese', 'confidence': 0.7407407407407407, 'encoding': 'GB2312'}
data='天王盖地虎の'.encode('utf-8')
print(data,chardet.detect(data))
#{'language': None, 'confidence': 0.0, 'encoding': None}

data = '最新の主要ニュース'.encode('euc-jp')
print(data.decode((chardet.detect(data))['encoding']))