#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 16:16
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : pillow
# @Software: PyCharm

import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn = cx_Oracle.connect('cigproxy/cigproxy@127.0.0.1/orcl')
cursor = conn.cursor()

cursor.execute("SELECT * FROM User_Tab_Comments where comments is not null and table_type='TABLE' AND rownum<20")
rows = cursor.fetchall()  # 得到所有数据集
for row in rows:
    print("%s, %s, %s" % (row[0], row[1], row[2]))

print("Number of rows returned: %d" % cursor.rowcount)

cursor.execute("SELECT * FROM user_tables where rownum<20")
while (True):
    row = cursor.fetchone()  # 逐行得到数据集
    if row == None:
        break
    print("%s, %s, %s, %s" % (row[0], row[1], row[2], row[3]))

print("Number of rows returned: %d" % cursor.rowcount)

cursor.close()
conn.close()