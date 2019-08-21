#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-21 15:09:42 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-21 15:09:42 
# @Software: vscode 

import cx_Oracle
import os
import urllib.request
import xlsxwriter
import requests

#上传地址 
url = "http://jczl.giscloud.cx/zhzlbackend/common/uploadFile"


#文件名
#files = {'file': open(r"C:\Users\dkgll\Desktop\7692A53708F95425049F79672A679C08.png", 'rb')}

#测试发现：Accept、User-Agent这俩必不可少
head1={
    #'Host':'jczl.giscloud.cx',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    #'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
    #'Accept-Encoding':'gzip, deflate', 
    #'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Cookie':"passport=8d0084b3-3140-4875-b7ad-d91cbb051aa4; CIGUserid=ADMIN; CIGToken=aa328620-853e-4700-978f-27e57b9c70cd; CIGUsername=%E9%95%BF%E5%85%B4%E5%B9%BF%E7%94%B5; true=GEzbBGOXm0OfDBW1AABa"
}      

#r = requests.post(url, files=files,headers=head) 

#获取网格员
def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('test','esri@123','10.21.198.127:15223/xe')
    cursor = conn.cursor()

    sql =  ("select TB.ID,Tc.FILE_NAME,VISIT_PATH,FILE_SIZE from cigproxy.zz_person ta "+
            "    join cigproxy.zz_grid_member tb on ta.card_num=tb.id_card "+
            "    JOIN cigproxy.zz_attachment tc on ta.id=tc.b_id and tc.file_type='per-image'  "+
            "        WHERE not exists(select * from cigproxy.zz_attachment td where tb.id=td.b_id and td.file_type='gridPerson')")

    #print(sql)
    
    cursor.execute(sql);
    rows = cursor.fetchall()  # 得到所有数据集
    li =[];
    for row in rows:
        li.append({"ID":row[0],"FILE_NAME":row[1],"VISIT_PATH":row[2],"FILE_SIZE":row[3]}); 

    print("Number of rows returned: %d" % cursor.rowcount)

    cursor.close()
    conn.close()
    return  li

def download_img(VISIT_PATH,FILE_NAME):
    header = head1 # 设置http header
    request = urllib.request.Request(VISIT_PATH, headers=header)
    try:
        response = urllib.request.urlopen(request)
        filename = "C:\\Users\\dkgll\\Desktop\\python目录\\网格员\\"+FILE_NAME
        with open(filename, "wb") as f:
            f.write(response.read()) # 将内容写入图片
        return filename
    except:
        return "failed" 

if __name__ == "__main__":  
    li = get_person()
    for i in range(len(li)):
        download_img(li[i]["VISIT_PATH"],li[i]["FILE_NAME"])