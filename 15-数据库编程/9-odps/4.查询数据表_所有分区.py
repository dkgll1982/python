#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-02-29 09:26:57
# @Last Modified by: guojun
# @Last Modified time: 2020-02-29 09:26:57
# @Software: vscode
from odps import ODPS
import cx_Oracle
import os
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
import re
import time
import logging  # 引入logging模块
import os.path 

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'                                        #设置plsql客户端字符集

class Matedata_odps:
    def __init__(self):
        self.conn = "cigproxy/cigproxy@172.21.246.244:15211/xe"                                 # 存储的odps的表名的位置
        self.access_id = 'HWqOnIUpeYhyd7BR'                                                     # 登陆账号
        self.access_key = '0RG5GJpo2WjCCwpUkQzcwjGGzKX8Tn'                                      # 登陆密码
        self.project = 'hzdn_mplc_dev'                                                          # odps上的项目名称
        self.endpoint = 'http://service.cn-huzhou-hzdsj-d01.odps.ops.cloud.huzhou.gov.cn/api'   # 官方提供的接口
        self.rowcount = 100000
        self.path = r'样例数据\\'                                                                #导出样例数据存放路径

        # 链接odps
        self.op = ODPS(access_id=self.access_id,
                       secret_access_key=self.access_key,
                       project=self.project,
                       endpoint=self.endpoint)

    # 获取odps上对应分区表的元数据信息
    def get_matedata(self, tables):
        for row in tables:
            table_name = row[0]                          #表名  
            t = self.op.get_table(table_name)            
            table_comment = t.comment                    #表注释
            #schema = t.schema                           #表架构信息  
            schema = re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',str(t.schema)) #此处将表架构信息转换成元组保存
            col_comment = [t[-1] for t in schema]        #列注释信息
            if '分区字段' in col_comment[-1]:             #分区字段在最后，不需要，删除之
                col_comment.pop()
                
            l = []                                       #获取表的所有分区信息   
            try:  
                for par in t.partitions:                 #如果分区不存在会报错
                    l.append(par.name)
            except Exception as e: 
                pass 
            #l = None if l == [] else l[-1] 
            data = []                                    #每个分区取部分数据进行叠加
            try:
                if l == []:
                    data = [value for value in self.op.read_table(  
                            table_name, start = 0, limit = self.rowcount, partition = None)] 
                    print('查询:{}表({})_无分区成功！'.format(table_comment,table_name))
                else:
                    for item in l: 
                        try:  
                            for value in self.op.read_table(table_name, start = 0, limit = self.rowcount, partition = item):
                                data.append(value) 
                            print('查询:{}表({})分区[{}]成功！'.format(table_comment,table_name,item))
                        except Exception as e:
                            msg = '错误1:查询{}表({})分区[{}]错误,错误信息：{}！'.format(table_comment,table_name,item,e)
                            print(msg)  
                            self.save_log(msg)
                            
                self.write_excel(data,col_comment,table_comment[0:100],table_name[0:100])    
                print('导出:{}表({})全部分区[{}]成功！\n'.format(table_comment,table_name,l))
            except Exception as e:      
                self.write_excel([],col_comment,table_comment[0:100]+"_未推送",table_name[0:100])   
                msg = '错误2:查询{}表({})分区[{}]错误,错误信息：{}！\n'.format(table_comment,table_name,l,e)
                print(msg)
                self.save_log(msg)
    
    # 将数据写入excel
    def write_excel(self,data,colname,workbook_name,sheet_name):
        workbook_name = workbook_name+"({})".format(sheet_name)
        data = self.illegal_char_rm(data)                           # 写入前进行非法字符处理
        workbook = openpyxl.Workbook()                              # 创建工作簿workbook
        sheet = workbook.active                                     # 创建工作表sheet，默认使用active页
        sheet.title = sheet_name                                    # 给工作表赋名
        #list(data[0]._name_indexes.keys())                         # 取sql查询结果的字段名 
        sheet.append(colname)    
        for record in data:
            sheet.append(record.values)                             # 取每条记录
            
        if len(data) == 0:
            workbook_name = '(记录为0)' + workbook_name
            
        # 然后创建一个目录:
        if not os.path.exists(self.path): 
            os.mkdir(self.path)  
               
        workbook.save(self.path+workbook_name+'.xlsx')   # 保存工作薄并命名
        
    # 定义处理非法字符的方法
    def illegal_char_rm(self,l):
        la = list()
        for record in l:  # 遍历每条表记录
            # 遍历记录的每一列的值，record.values类型为list，取list的index和value需要用enumerate，不然会报错
            for index, value in enumerate(record.values):
                record[index] = ILLEGAL_CHARACTERS_RE.sub('', value) if isinstance(
                    value, str) else value  # 如果值类型为字符串，替换为空，否则保留原值
            la.append(record)
        return la  
      
    #写入日志            
    def save_log(self,msg):
        # 第一步，创建一个logger
         logger = logging.getLogger()
         logger.setLevel(logging.INFO)  # Log等级总开关
         # 第二步，创建一个handler，用于写入日志文件
         rq = time.strftime('%m%d%H', time.localtime(time.time())) 
         log_name = self.path + '导出错误_' + rq + '.log'
         logfile = log_name
         fh = logging.FileHandler(logfile, mode='w')
         fh.setLevel(logging.ERROR)  # 输出到file的log等级的开关
         # 第三步，定义handler的输出格式
         formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
         fh.setFormatter(formatter)
         # 第四步，将logger添加到handler里面
         logger.addHandler(fh)
         logger.error(msg)
         
    # 获取所有存储的odps的表名，并将样例数据写入excel
    # 测试无分区的表：dws_prsn_company_represent_person_info_mmsb_d
    # 测试分区表：dws_disaster_shelter_memb
    # 测试错误表：dws_prsn_severe_psychopath_mpsb_m
    def start(self):
        sql = '''SELECT DISTINCT "推送后的表名" table_name FROM test."BASE_表结构0228" 
            where "推送后的表名" in(
                'dws_evt_production_safety_accident_punishment_info_memb_m',
                'dws_disaster_shelter_memb',
                'dws_prpt_unit_honour_info_egint_mjb_m',
                'dws_prpt_unit_honour_info_egint_mstb_m',
                'dws_prpt_transport_unit_honor_commendation_info_htb_m',
                'dws_evt_administrative_penalty_info_mcb_m',
                'dws_evt_administrative_penalty_info_mepb_w',
                'dws_evt_administration_penalty_info_mieb_w'                
            )'''
        conn = cx_Oracle.connect(self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        self.get_matedata(rows)
        cursor.close()
        conn.close()
    
if __name__ == '__main__':  
    start = time.time()
    mate = Matedata_odps()
    mate.start()
    end = time.time()
    print("导出样例数据完成！！！""总耗时：%0.6fs"%(end -start)); 