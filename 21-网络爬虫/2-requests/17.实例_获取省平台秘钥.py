import requests
import json
import cx_Oracle
import time,datetime
import hashlib
import json
import os
import math
from concurrent.futures import ThreadPoolExecutor
import threading
from DBUtils.PooledDB import PooledDB
#注意点：https://blog.csdn.net/mxdzchallpp/article/details/80411514 （python多线程操作数据库问题）

class sptspider():
    def __init__(self):
        super().__init__()
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        self.SecretByKeyUrl = 'http://59.202.115.11/gateway/app/refreshTokenByKey.htm'  #48小时调用
        self.SecretBySecUrl = 'http://59.202.115.11/gateway/app/refreshTokenBySec.htm'  #15分钟调用
        user='cigwbj'
        password='esri@123'
        host='10.21.198.126'
        port='15214'
        sid='xe'
        dsn = cx_Oracle.makedsn(host,port,sid)
        self.pool = PooledDB(cx_Oracle,
                             mincached = 20,
                             blocking = True,
                             user = user,
                             password = password,
                             dsn = dsn)
        
    #请求省平台秘钥
    def send_request(self,url,appkey,appsecret):
        date = int(time.time()*1000)
        md5= hashlib.md5()
        md5.update((appkey+appsecret+str(date)).encode())
        sign = md5.hexdigest() 
        
        params = {
            "appKey":appkey,
            "sign":sign,
            "requestTime":date
        } 
        response = requests.get(url = url,params = params)
        if response.status_code == 200:
            return response
        
    #解析秘钥数据
    def parse_request(self,response,appkey,deptname): 
        text = response.text
        j = json.loads(text) 
        if j["code"] == '00':       #成功
            d = j["datas"]
            refreshSecret = d["refreshSecret"]
            refreshSecretEndTime = d["refreshSecretEndTime"]
            requestSecret = d["requestSecret"]
            requestSecretEndTime = d["requestSecretEndTime"]
            self.update_serc(appkey,refreshSecret,refreshSecretEndTime,requestSecret,requestSecretEndTime,deptname)
        else:
            print("【{deptname}】请求秘钥错误，返回结果：{}".format(text))
    
    #保存秘钥    
    def update_serc(self,appkey,refreshSecret,refreshSecretEndTime,requestSecret,requestSecretEndTime,deptname):   
        conn = self.pool.connection()
        cursor = conn.cursor()   
        #保存秘钥
        sql = "INSERT INTO BASE_SPT_KEYSECRET(REQUESTSECRETENDTIME,REFRESHSECRETENDTIME,REQUESTSECRET,REFRESHSECRET,create_user,APP_KEY)VALUES(:1,:2,:3,:4,:5,:6)"
        params = (requestSecretEndTime,refreshSecretEndTime,requestSecret,refreshSecret,'python',appkey)           
        cursor.execute(sql,params)
        #删除旧的api地址
        sql = "delete from base_spt_url where APP_KEY=:1"
        cursor.execute(sql,[appkey])
        #插入新的api地址
        sql = """INSERT INTO base_spt_url(key,url_str,APP_KEY)
                SELECT  key,BASEURL||appKey||sign||requestTime||additional||'&'||example as url,APP_KEY  FROM (
                    SELECT TB.KEY AS APP_KEY,ROW_NUMBER() OVER(PARTITION BY TA.KEY ORDER BY TA.KEY) AS RN, TA.KEY,BASEURL BaseUrl,'?appKey='||GET_UTF8_STR(TB.KEY) appKey,
                        '&'||'sign='||GET_UTF8_STR(lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(
                        INPUT_STRING => TB.KEY||TD.SERC||td.CREATE_DATE)))) sign,
                        '&'||'requestTime='||GET_UTF8_STR(td.CREATE_DATE) requestTime,
                        '&'||'additional='||GET_UTF8_STR('{\"powerMatters\":\"' || TC.SXBM||'\",\"subPowerMatters\":\"' || TC.ZXBM||'\",\"accesscardId\":\"sjgl\",\"materialName\":\"' || TC.zxmc||'\",\"sponsorName\":\"大数据管理中心\"}') additional,
                        example
                    FROM BASE_SPT_INTERFACE TA
                        JOIN BASE_SPT_SERC TB ON ','||TB.INTERFACE||',' LIKE '%,'||TA.KEY||',%'
                        JOIN BASE_SPT_QLSX TC ON (','||tC.deptID2||',' like '%,'||tb.deptid||',%' and tC.zxmc is not null and tC.zxbm is not null and tC.state=1) 
                        JOIN (select to_char((SYSDATE - TO_DATE('1970-1-1 8', 'YYYY-MM-DD HH24')) * 86400000 + TO_NUMBER(TO_CHAR(SYSTIMESTAMP(3), 'FF'))) create_date,SERC,app_key from (
                            select create_date,row_number() over(partition by app_key order by create_date desc nulls last) rn,requestsecret SERC,app_key from base_spt_keysecret 
                            ) where rn=1) TD ON TD.APP_KEY=TB.KEY
                ) TA 
                WHERE RN=1 and APP_KEY=:1""" 
        cursor.execute(sql,[appkey])
        conn.commit()
        print(f'获取【{deptname}】秘钥成功，当前秘钥：{requestSecret}')
        cursor.close()
        conn.close()
        
    #查询数据库秘钥
    def get_serc(self,args):
        conn = self.pool.connection()
        cursor = conn.cursor()    
        sql = '''select * from (
                    select REQUESTSECRETENDTIME,REFRESHSECRETENDTIME,REQUESTSECRET,REFRESHSECRET,
                        count(1) over(partition by app_key) as requestcount,
                        row_number() over(partition by app_key order by create_date desc) rn 
                    from base_spt_keysecret 
                    where app_key='{}'
                        and trunc(sysdate)=trunc(create_date)
                ) where rn=1'''.format(args[0])
        cursor.execute(sql)
        row = cursor.fetchone() 
        cursor.close() 
        conn.close()
        if row is not None: 
            current_time = int(round(time.time() * 1000))             #13位的时间戳
            diff = math.ceil((row[0]-current_time)/1000)
            return args,row[4]+1,diff,True if diff < 60 else False         #每隔14分钟刷新一次秘钥 (此处判断不要采用服务器时间，可能服务器时间未矫正)      
        else:
            return args,1,30,True
        
    #查询应用信息
    def get_appinfo(self):
        conn = self.pool.connection()
        cursor = conn.cursor()      
        #此处需要更新配置的应用key，秘钥信息。否则请求会报签名错误  
        sql = "select key,serc,dept from base_spt_serc where interface is not null and DEPT='湖州市政法委'"
        cursor.execute(sql)
        row = cursor.fetchall() 
        cursor.close() 
        conn.close()
        
        return row
    
    #判断是否工作时间
    def is_worktime(self):
        # 范围时间(晚上9点终止运行)
        d_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'23:50', '%Y-%m-%d%H:%M')   
        # 当前时间
        c_time = datetime.datetime.now()
        # 判断当前时间是否在范围时间内
        return True if c_time < d_time else False
            
    def start (self): 
        data = self.get_appinfo()
        while True:
            if not self.is_worktime():
                print('非工作时间，停止运行！')
                break
            # 创建一个包含4条线程的线程池
            with ThreadPoolExecutor(max_workers = 14) as pool:
                # 使用线程执行map计算
                # 后面元组有3个元素，因此程序启动3条线程来执行action函数
                results = pool.map(self.get_serc,data) 
                for row in results: 
                    appinfo,requesrcount,diff,tag = row
                    appkey,appsecret,deptname = appinfo
                    if tag:
                        print(f'【{deptname}】第{requesrcount}次重新请求秘钥！')
                        response = self.send_request(self.SecretByKeyUrl,appkey,appsecret)
                        if response:
                            self.parse_request(response,appkey,deptname)
                    else: 
                        print(f'【{deptname}】本地秘钥将于{diff}秒后失效，当前可以继续使用！')
                print()
            time.sleep(60) 

if __name__ == "__main__":
    spts = sptspider()
    spts.start()
