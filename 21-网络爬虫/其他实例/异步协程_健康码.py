import aiohttp
import asyncio
import time
import datetime
import cx_Oracle
import socket
import os
import sys  

ip = sys.argv[1]

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 获取查询的数据列表 
def get_data(): 
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql1 = f"select * from(select tb.name,url_str FROM base_spt_url ta join base_spt_interface tb on tb.enable=1 and ta.key=tb.key and tb.ip like '%{ip}%' and ta.key like 'jkm%')"
    cursor.execute(sql1)
    return cursor.fetchone()                    # 得到所有数据集
 
#判断是否工作时间
def is_worktime():
    # 范围时间(晚上9点终止运行)
    d1_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:20', '%Y-%m-%d%H:%M') 
    d2_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:50', '%Y-%m-%d%H:%M')   
    # 当前时间
    c_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    return True if c_time >d1_time and c_time <d2_time else False
            
async def get_page(name,url):
    async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(total = 10)) as session:   #10s超时  
        try:
            async with await session.get(url=url) as res: 
                if res.status == 200:
                    page_text = await res.text()   # read()  json() 
                    print('%s-接口:%s,结果:%s'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),name,page_text[2:23]))    
                else:
                    print("{}-Error: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),res))
        except Exception as e:
            print("{}-请求超时错误{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),e))
                
start = time.time()

while True:
    if is_worktime():
        print('非工作时间，停止运行！')
        break
    
    tasks = []
    loop = asyncio.get_event_loop()
    row = get_data()
    for i in range(100): 
        c = get_page(row[0],row[1])
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)
