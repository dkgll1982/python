#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-10 15:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : mysql连接
# @Software: PyCharm

import pymysql.cursors

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cig', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# ③、执行DDL语句创建数据表
cursor.execute('''create table user_tb1(
    user_id int primary key auto_increment,
    name varchar(255),
    pass varchar(255),
    gender varchar(255))''')
# 执行DDL语句创建数据表
cursor.execute('''create table order_tb1(
    order_id integer primary key auto_increment,
    item_name varchar(255),
    item_price double,
    item_number double,
    user_id int,
    foreign key(user_id) references user_tb(user_id) )''')


# 创建sql 语句，并执行
import random
for x in range(101):
    sql = "INSERT INTO `users` (`email`, `password`) VALUES ('huzhiheng@itest.info', '"+str(random.randint(100000,999999))+"')"
    cursor.execute(sql)

# 提交SQL
connection.commit()

# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
sql = "SELECT `id`, `password` FROM `users` WHERE `email`='dkgll@qq.com'"
cursor.execute(sql)

#查询数据库单条数据
result = cursor.fetchone()
print(result)

print("-----------华丽分割线------------")

# 执行数据查询
sql = "SELECT `id`, `password` FROM `users`"
cursor.execute(sql)

#查询数据库多条数据
result = cursor.fetchall()
for data in result:
    print(data)

# 关闭数据连接
connection.close()