#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-08-21 19:38:25
# @Last Modified by: guojun
# @Last Modified time: 2019-08-21 19:38:25
# @Software: vscode

import cx_Oracle
import os
import urllib.request
from 坐标转换 import bd09_to_wgs84, bdapi
import threading
import time
import urllib.request
import json
import datetime

# 获取查询的数据列表 
def get_zb(index):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    # ORACLE连接参数
    conn = cx_Oracle.connect('test', 'esri@123', '10.21.198.127:15223/xe')
    cursor = conn.cursor()

    # 查询数据的sql
    sql1 = 'SELECT * FROM test.SJ_JWD where update_date is null'
    # 修改返回结果的sql
    sql2 = ""

    cursor.execute(sql1);
    rows = cursor.fetchall()  # 得到所有数据集

    update_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in rows:
        try:
            wgs_zb = bd09_to_wgs84(float(row[9]), float(row[10]))  # 将百度坐标转为WGS84坐标
            wgs_x, wgs_y = str(wgs_zb[0]), str(wgs_zb[1])
            sql2 = "update test.SJ_JWD set wgs_x='%s',wgs_y='%s',update_date=to_date('%s','YYYY-MM-DD HH24:MI:SS') where id='%s'" % (
                wgs_x, wgs_y, update_date, row[0])
            cursor.execute(sql2)
        except Exception as e:
            print('Error:', e)
        finally:
            pass
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("主线程(%s)启动" % (threading.current_thread().name))
    start = time.time()

    T = threading.Thread(target=get_zb, name="Thread"+str(1), args=(1,))

    T.start()
    T.join()

    time.sleep(2)

    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒" % (threading.current_thread().name, end-start))
