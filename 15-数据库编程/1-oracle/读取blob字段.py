#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-19 12:40:34 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-19 12:40:34 
# @Software: vscode 


import os
import cx_Oracle
import time
import imghdr
import struct

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

db_orcl = cx_Oracle.connect("cigproxy/cigproxy@172.21.246.244:15211/xe")
cr_orcl = db_orcl.cursor()
cr_orcl.execute("select * from test.dws_person_photo_mpsb_m WHERE rownum=1 and photo_id='3305000001002012919' ")
rs_user = cr_orcl.fetchall()


for user in rs_user:
    userId = user[0]
    print(userId)
    if user[2] == '':
        continue
    blob = user[2].read().dec 
    with open(r"backup\{}.jpeg".format(userId), "wb") as f:
        f.write(blob) 

db_orcl.commit()
cr_orcl.close() 
 