#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 14:38:14 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 14:38:14 
# @Software: vscode 

# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名:memory:代表创建内存中的数据库
conn = sqlite3.connect('15-数据库编程/sqllite/first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where _id > ?', (2,))
print('查询返回的记录数:', c.rowcount)
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 获取一行记录，每行数据都是一个元组
    row = c.fetchone()
    # 如果抓取的row为None，退出循环
    if not row :
        break
    print(row)
    print(row[1] + '-->' + row[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()