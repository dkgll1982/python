import aiohttp
import asyncio
import time
import datetime
import cx_Oracle
import socket
import os
import sys

# def get_host_ip():
#     """
#     查询本机ip地址
#     :return:
#     """
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(('8.8.8.8', 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#     return ip

ip = sys.argv[1]

# 获取查询的数据列表 
def get_data():
    #ip = get_host_ip()
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql1 = f"select * from(select tb.name,url_str FROM base_spt_url ta join base_spt_interface tb on tb.enable=1 and ta.key=tb.key and tb.ip like '%{ip}%' and ta.key not like 'jkm%')"
    cursor.execute(sql1)
    return cursor.fetchall()  # 得到所有数据集

async def get_page(name,url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            page_text = await response.text()  # read()  json() 
            print('接口:%s,结果:%s'%(name,page_text[0:110]))   
                
start = time.time()

for i in range(2000):
    tasks = []
    loop = asyncio.get_event_loop()
    rows = get_data()
    for row in rows:
        c = get_page(row[0],row[1])
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)
