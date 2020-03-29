#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-28 23:12:11 
# @Remark: 人生苦短，我用python！

from lxml import etree
import re
import time
import os
import sys
import requests
from urllib import parse as urlparse
import xml.dom.minidom
from xml.dom.minidom import parse,parseString 
import cx_Oracle
import copy

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class CaiPiaoSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://kaijiang.500.com'
        self.url = urlparse.urljoin(self.host,'/static/info/kaijiang/xml/ssq/list.xml?_A=YEOXJFGK1585300798751')
        self.detail_url = urlparse.urljoin(self.host,'/shtml/ssq/{}.shtml')
        self.base_dir = ''
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }
        #ORACLE连接参数
        self.conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        self.cursor = self.conn.cursor() 
        #建表语句
        # CREATE TABLE  "BASE_SSQ_INFO" 
        # (	"QIHAO" VARCHAR2(20 BYTE), 
        #     "HAOMA" VARCHAR2(20 BYTE), 
        #     "KJRQ" VARCHAR2(50 BYTE), 
        #     "JZRQ" VARCHAR2(50 BYTE), 
        #     "XIAOLIANG" VARCHAR2(20 BYTE), 
        #     "JIANGCHI" VARCHAR2(20 BYTE)
        # )  ;

        # CREATE TABLE "BASE_SSQ_ZJXX" 
        # (	"QIHAO" VARCHAR2(20 BYTE), 
        #     "type" VARCHAR2(20 BYTE), 
        #     "num" VARCHAR2(20 BYTE), 
        #     "PRIZE" VARCHAR2(20 BYTE)
        # ) ;

    # 发送请求
    def send_request(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print('URL:{},错误信息:{}'.format(url, e))

    # 解析请求
    def parse_content(self, response): 
        xml_dom = parseString(response.text) 
        expect = xml_dom.getElementsByTagName('row')
        row_set = {x[0] for x in self.get_data()}
        row_index = 0
        for item in expect:
            qihao = item.getAttribute('expect') 
            if qihao not in row_set:
                detail_res = self.send_request(self.detail_url.format(qihao))
                if detail_res:
                    self.parse_detail(detail_res)
                    if row_index%100 == 0:      #每100条提交一次
                        self.conn.commit()
                    row_index += 1
                time.sleep(1)                   #别爬太快
        self.conn.commit()                      #整体提交一次
        #完成之后关闭游标和连接
        self.cursor.close()
        self.conn.close()
        
    # 解析详情
    def parse_detail(self,response): 
        response.encoding = 'gb18030' 
        html = etree.HTML(response.text) 
        dict = {}
        dict["qihao"] = html.xpath("//font[@class='cfont2']/strong/text()")[0]  
        dict["haoma"] = ','.join(html.xpath("//div[@class='ball_box01']/ul/li//text()"))
        
        riqi = html.xpath("//span[@class='span_right'][1]/text()")[0]
        partten = re.compile('开奖日期：(.*?日)\s*兑奖截止日期：\s*(.*?日)') 
        result = re.findall(partten,riqi)
        if result:
            dict["kjrq"],dict["jzrq"] = result[0]
        else:
            dict["kjrq"],dict["jzrq"] = '',''         
        dict["xiaoliang"] = html.xpath("//span[@class='cfont1 '][1]/text()")[0]
        dict["jiangchi"] = html.xpath("//span[@class='cfont1 '][2]/text()")[0] 
         
        self.insert_record(dict)
        params,det = [],{}   
        table = html.xpath('//table[@class="kj_tablelist02"][2]')[0] 
        for i in range(3,9):
            det["qihao"] = dict["qihao"]
            det["type"] = table.xpath('.//tr[%d]//td[1]/text()'%i)[0].replace('\r\n','').replace('\t','')
            det["num"] = table.xpath('.//tr[%d]//td[2]/text()'%i)[0].replace('\r\n','').replace('\t','')
            det["prize"] = table.xpath('.//tr[%d]//td[3]/text()'%i)[0].replace('\r\n','').replace('\t','')  
            # 此处采用copy.deepcopy，因为拷贝对象的值改变了，会导致最终列表的每一项都变化了、
            params.append(copy.deepcopy(det)) 
        self.insert_detail(params)
        print('获取第{}期双色球中奖信息完成！'.format(dict["qihao"]))
        
    # 查询数据    
    def get_data(self):
        sql = 'select qihao from BASE_SSQ_INFO'
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 得到所有数据集 
   
    # 执行添加记录的SQL    
    def insert_record(self,dict):
        sql = """INSERT INTO BASE_SSQ_INFO(qihao,haoma,kjrq,jzrq,xiaoliang,jiangchi)
                 select :qihao,:haoma,:kjrq,:jzrq,:xiaoliang,:jiangchi from dual where not exists(
                     select * from BASE_SSQ_INFO where qihao=:qihao
                 ) """
        self.cursor.execute(sql,dict) 
        
    # 执行添加详情的SQL    
    def insert_detail(self,params):
        sql = """INSERT INTO BASE_SSQ_ZJXX(qihao,"type","num",prize)
                 select :qihao,:type,:num,:prize from dual where not exists(
                         select * from base_ssq_zjxx where qihao =:qihao and "type"=:type
                ) """
        self.cursor.executemany(sql,params)  

    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_content(response)

if __name__ == "__main__":
    start = time.time()
    cps = CaiPiaoSpider()
    cps.start()
    end = time.time()
    print('爬取数据完成，耗时%.2fs'%(end - start))
