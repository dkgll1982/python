#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 14:59:44 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 14:59:44 
# @Software: vscode 

# 导入访问MySQL的模块
import pymysql.cursors

# ①、连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cig', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# ②、获取游标
c = conn.cursor()
# ③、调用callproc()方法执行存储过程
# 虽然add_pro存储过程需要3个参数，但最后一个参数是传出参数，
# 因此程序不会用它的值
result_args = c.callproc('add_pro', (5, 6, 0))
# 返回的result_args既包含了传入参数的值，也包含了传出参数的值
print(result_args)
# 如果只想访问传出参数的值，可直接访问result_args的第3个元素，如下代码
print(result_args[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()