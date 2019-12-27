import cx_Oracle
from threading import Thread
import time
import os,shutil
 
#shutil.copyfile应用,参数必须具体到文件名
def mycopyfile(sourcefile,dir,photoname):
    if not os.path.exists(dir):
        print("dir:%s not exit!" % (dir)) 
        os.makedirs(dir)
    if not os.path.isfile(sourcefile):
        print("file:%s not exit!" % (sourcefile)) 
    else:
        shutil.copyfile(sourcefile,dir+'\\'+photoname)

# 获取查询的数据列表
def get_data(data_from, type):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    
    sql = '''SELECT DATA_FROM,type,FILENAME,'C:\\湖州重点\\'||DATA_FROM||'重点人口_'||type DIR_NAME,NAME||'_'||CARD_NUM||'.'||REPLACE(PNG,'.*.') PHOTO_NAME FROM (
            SELECT PNG,DECODE(TB.DATA_FROM,'cx','长兴','aj','安吉','nth','南太湖','wx','吴兴','nx','南浔','dq','德清') DATA_FROM, 
                TB.FOCUS_CONTROL,TB.CARD_NUM,TB.NAME,replace(TA.FILENAME,'new\\','') FILENAME,
                DECODE(TC.TYPE,'201','刑满释放','202','社区矫正','203','精神病','204','吸毒','205','艾滋病','206','信访','207','重点青少年','208','邪教','209','传销','210','其他','211','危险品从业人员') TYPE
            FROM BASE_SPT_XTDJ_ALLIMG TA
                JOIN CZZ_PERSON TB ON TA.IC_CARD=TB.CARD_NUM AND TB.FOCUS_CONTROL IS NOT NULL
                JOIN (SELECT TO_CHAR(200+LEVEL) TYPE FROM DUAL CONNECT BY LEVEL<12) TC ON TB.FOCUS_CONTROL LIKE '%'||TC.TYPE||'%'
            WHERE DATA_FROM='{}' and tc.type='{}' )'''.format(data_from, type)
    
    #print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()  # 得到所有数据集 

    for row in rows:
        mycopyfile(row[2],row[3],row[4])

    conn.commit() 
    cursor.close()
    conn.close()    

if __name__ == "__main__":
    start = time.time()

    data_from = ['cx', 'dq', 'aj', 'wx', 'nth', 'nx']
    type = ['201', '202', '203', '204', '205',
            '206', '207', '208', '209', '210', '211']

    ThreadList = []

    for x in data_from:
        for y in type:
            ThreadList.append(Thread(name=x+'_'+y,
                                     target=get_data, args=(x, y,)))

    for tr in ThreadList:
        tr.start()

    for tr in ThreadList:
        tr.join()

    end = time.time()

    print('拷贝共计耗时：%ds' % (end-start))
