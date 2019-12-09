#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-21 16:21:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-21 16:21:20 
# @Software: vscode 
 
import cx_Oracle
import os
import urllib.request
import xlsxwriter
import requests
import json
import os, sys

#上传地址 
url = "http://jczl.giscloud.cx/zhzlbackend/common/uploadFile"
#测试发现：Accept、User-Agent这俩必不可少
head={
    #'Host':'jczl.giscloud.cx',
    #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    #'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
    #'Accept-Encoding':'gzip, deflate', 
    #'Connection':'keep-alive',
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Cookie':"passport=8d0084b3-3140-4875-b7ad-d91cbb051aa4; CIGUserid=ADMIN; CIGToken=0c5eae9a-bdcd-4548-9ab4-90b850fbd6df; CIGUsername=%E9%95%BF%E5%85%B4%E5%B9%BF%E7%94%B5; true=cPnWEVCZOFb7n9BwAAEo"
}

#更新
def update_bid(cardnum,id1,id2):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('test','esri@123','10.21.198.127:15223/xe')
    cursor = conn.cursor()  
    
    sql2 = "update cigproxy.zz_attachment set file_type='gridPerson',B_ID=(select id from cigproxy.zz_grid_member where id_card='"+cardnum+"' and rownum=1) where id = '" +id1+"' or id='"+id2+"'"
    #print(sql2);
    cursor.execute(sql2) 
    conn.commit() 
    cursor.close()
    conn.close()   

def upload_img(FILE_NAME):
    files = {'file': open(r"backup\\网格员\\"+FILE_NAME, 'rb')}
    r = requests.post(url, files=files,headers=head)  
    card_num = FILE_NAME[0:18]
    response = r.json()
    try:
        update_bid(card_num,response["data"]["id"],response["data"]["thumbnail"]["id"]);
    except:
        pass

def del_img(FILE_NAME):
    if (os.path.exists(FILE_NAME)):
        os.remove(FILE_NAME)

if __name__ == "__main__":   
    dir = r"backup\网格员"
    fileNames = os.listdir(dir)
    for file in fileNames:
        #print(file)
        upload_img(file) 