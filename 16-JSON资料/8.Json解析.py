import json
import cx_Oracle
from concurrent.futures import ThreadPoolExecutor
import time
import os
from dbutils.pooled_db import PooledDB

class GuoTuSpider():
    def __init__(self):
        super().__init__()
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        user='cigwbj'
        password='esri@123'
        host='10.21.198.126'
        port='15214'
        sid='xe'
        dsn = cx_Oracle.makedsn(host,port,sid)
        #连接池
        self.pool = PooledDB(cx_Oracle,
                             mincached = 20,
                             blocking = True,
                             user = user,
                             password = password,
                             dsn = dsn)
        total_size = 384193                                 #数据量
        self.total_page = 20                                #页数 
        self.page_size = int(total_size/self.total_page)    #每页行数
        self.rownum = 100                                   #每次取数据量
        
    #查询数据信息
    def get_data(self,pageindex):
        try: 
            conn = self.pool.connection()
            cursor = conn.cursor()      
            sql1 = '''SELECT * FROM (
                        select ID,PARA1 CARD_NUM,PARA2 NAME,BODY,COLUMN1 RN from BASE_SPT_XTDJ_TB 
                        where TYPE_ID='gtfw'
                            and body not like '%【%'
                            and COLUMN1 IS NOT NULL
                            and id not in(
                                select id from zz_guotu
                            )
                    ) ta
                    where ta.RN BETWEEN {}*{} AND {}*{} AND ROWNUM<={}'''.format(self.page_size,pageindex,self.page_size,pageindex+1,self.rownum)
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for row in rows:
                id = row[0]
                card_num = row[1]
                name = row[2]
                body = json.load(row[3])
                params = []
                qlrxxList = []
                dyqxxList = []
                cfxxList = []
                yyxxList = []
                xzxxList = []
                for l in body:  
                    for q in l['qlrxxList']:
                        qlrxxList.append([id,card_num,name,q['qlr'],q['bdcqzh'],q['sbh'],q['fzsj'],q['bdcdyh'],
                                        q['zjh'],q['zjzl'],q['qlrlb'],q['qlrlx'],q['gyfs'],q['dz'],q['yb'],q['gddh'],
                                        q['yddh'],q['qlrfrmc'],q['qlrfrdh'],q['qlrfrzjzl'],q['qlrfrzjh'],q['qlrfrlxdz'],
                                        q['qlbl'],q['fj']])
                    sql3 = '''INSERT INTO ZZ_GUOTU_QLRXXLIST(id,card_num,name,qlr,bdcqzh,sbh,fzsj,bdcdyh,zjh,zjzl,qlrlb,
                                qlrlx,gyfs,dz,yb,gddh,yddh,qlrfrmc,qlrfrdh,qlrfrzjzl,qlrfrzjh,qlrfrlxdz,qlbl,fj) 
                              VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8,:v9,:v10,:v11,:v12,:v13,:v14,:v15,:v16,:v17,
                                :v18,:v19,:v20,:v21,:v22,:v23)'''  
                                
                    for d in l['dyqxxList']:
                        dyqxxList.append([id,card_num,name,d['dyqr'],d['dyzmh'],d['zqse'],d['dyfs'],d['dydjsj'],
                                          d['zwlxsj'],d['dyfj']])
                    sql4 = '''INSERT INTO zz_guotu_dyqxxlist(id,card_num,name,dyqr,dyzmh,zqse,dyfs,dydjsj,zwlxsj,dyfj) 
                              VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8,:v9)'''   
                                
                    for c in l['cfxxList']:
                        cfxxList.append([id,card_num,name,c['cfwh'],c['cfjg'],c['cfqx'],c['djyy'],c['cfyyf'],c['cfdjzxbsm']])
                    sql5 = '''INSERT INTO zz_guotu_cfxxList(id,card_num,name,cfwh,cfjg,cfqx,djyy,cfyyf,cfdjzxbsm) 
                              VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8)'''  
                                
                    for y in l['yyxxList']:
                        yyxxList.append([id,card_num,name,y['id'],y['yysqr'],y['djyy'],y['djsj'],y['cxsj']])
                    sql6 = '''INSERT INTO zz_guotu_yyxxList(id,card_num,name,yyxx_id,yysqr,djyy,djsj,cxsj) 
                              VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7)'''   
                                
                    for x in l['xzxxList']:
                        xzxxList.append([id,card_num,name,x['id'],x['xzzxjg'],x['xzwj'],x['xzwh'],x['xzyy'],x['xzjssj']])
                    sql7 = '''INSERT INTO zz_guotu_xzxxList(id,card_num,name,xzxx_id,xzzxjg,xzwj,xzwh,xzyy,xzjssj) 
                              VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8)''' 
                              
                    params.append([id,card_num,name,l['zl'],l['bdcdyh'],l['qllx'],l['qlxz'],l['szc'],l['zcs'],
                                    l['tdsyqmj'],l['fwjg'],l['yt'],l['mj'],l['jgsj'],l['jcnf'],l['gyqk'],l['fwxz'],
                                    l['djsj'],l['fj'],l['qlbsm'],l['tdsyqssj'],l['tdsyjssj'],l['tdfj'],l['tdyt'],
                                    l['qlzt'],l['dybsm'],l['zyzxsj'],l['tdqzh'],l['xzzt'],l['qlr'],l['bdcqzh'],
                                    l['bdczjh'],l['sbh'],l['dyzk'],l['cfzk'],l['dyzkname'],l['cfzkname'],l['syqx']])
                
                sql2 = '''INSERT INTO zz_guotu (id,card_num,name,zl,bdcdyh,qllx,qlxz,szc,zcs,tdsyqmj,fwjg,yt,mj,jgsj,
                            jcnf,gyqk,fwxz,djsj,fj,qlbsm,tdsyqssj,tdsyjssj,tdfj,tdyt,qlzt,dybsm,zyzxsj,tdqzh,xzzt,qlr,
                            bdcqzh,bdczjh,sbh,dyzk,cfzk,dyzkname,cfzkname,syqx) 
                          VALUES (:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8,:v9,:v10,:v11,:v12,:v13,:v14,:v15,:v16,:v17,:v18,
                            :v19,:v20,:v21,:v22,:v23,:v24,:v25,:v26,:v27,:v28,:v29,:v30,:v31,:v32,:v33,:v34,:v35,:v36,
                            :v37)'''
                            
                cursor.executemany(sql2,params)
                cursor.executemany(sql3,qlrxxList)
                cursor.executemany(sql4,dyqxxList)
                cursor.executemany(sql5,cfxxList)
                cursor.executemany(sql6,yyxxList)
                cursor.executemany(sql7,xzxxList)
                print(f"身份证号—{card_num}的房屋数据查询成功!")
            
            conn.commit() 
            cursor.close() 
            conn.close() 
                    
        except Exception as e:
            print("数据库查询错误！",e)
    
if __name__ == "__main__":
    gts = GuoTuSpider() 
    while True:
        with ThreadPoolExecutor(max_workers = 10) as pool:
            results = pool.map(gts.get_data,[x for x in range(gts.total_page)])