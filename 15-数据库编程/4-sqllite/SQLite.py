#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 14:25:32 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 14:25:32 
# @Software: vscode 

# 导入访问SQLite的模块
import sqlite3
# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('15-数据库编程/4-sqllite/first.db')
# ②、获取游标
c = conn.cursor()
# ③、执行DDL语句创建数据表
# c.execute('''create table user_tb2(
#     _id integer primary key autoincrement,
#     name text,
#     pass text,
#     gender text)''')
# # 执行DDL语句创建数据表
# c.execute('''create table order_tb2(
#     _id integer primary key autoincrement,
#     item_name text,
#     item_price real,
#     item_number real,
#     user_id inteter,
#     foreign key(user_id) references user_tb(_id) )''')


c.execute('''insert into order_tb2(item_name,item_price,item_number,user_id) values('张三',312,123,'1')''');
c.execute('''insert into order_tb2(item_name,item_price,item_number,user_id) values('李四',152,263,'1')''');
c.execute('''insert into order_tb2(item_name,item_price,item_number,user_id) values('王五',172,293,'1')''');
c.execute('''insert into order_tb2(item_name,item_price,item_number,user_id) values('马六',142,243,'1')''');
c.execute('''insert into order_tb2(item_name,item_price,item_number,user_id) values('钱琦',128,293,'1')''');

# 如果程序使用 executemany() 方法，则可以多次执行同一条 SQL 语句
# ③、调用executemany()方法把同一条SQL语句执行多次
# c.executemany('insert into user_tb values(null, ?, ?, ?)',
#     (('sun', '123456', 'male'),
#     ('bai', '123456', 'female'),
#     ('zhu', '123456', 'male'),
#     ('niu', '123456', 'male'),
#     ('tang', '123456', 'male')))

# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('update user_tb set name=? where _id=?',
    (('小孙', 2),
    ('小白', 3),
    ('小猪', 4),
    ('小牛', 5),
    ('小唐', 6)))
# 通过rowcount获取被修改的记录条数
print('修改的记录条数：', c.rowcount)    

# 执行DDL语句创建数据表
# c.execute('''create table order_tb2(
#     _id integer primary key autoincrement,
#     item_name text,
#     item_price real,
#     item_number real,
#     user_id inteter,
#     foreign key(user_id) references user_tb(_id) )''')
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()