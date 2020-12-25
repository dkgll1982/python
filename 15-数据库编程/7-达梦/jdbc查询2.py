#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-22 16:26:30 
# @Remark: Life is short, I use python！

import jaydebeapi

url = 'jdbc:dm://10.21.198.201:5236/DMHR'
user = 'SYSDBA'
password = 'tggc12345'
dirver = 'dm.jdbc.driver.DmDriver'
jarFile = r'D:\Programing\pdi-ce-9.1.0.0-324\data-integration\lib\DmJdbcDriver18.jar'
sqlStr = 'select count(1) dual '
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()