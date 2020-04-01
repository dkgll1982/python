#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-25 10:46:10
# @Remark: 人生苦短，我用python！

import os
import cx_Oracle
import sys
import xlrd
import time
import hashlib
import requests
import threading
from PIL import Image, ImageDraw, ImageFont
import copy

class photo_shuiying():
    def __init__(self, file_name):
        super().__init__()
        self.dbuser = 'test'
        self.dbpwd = 'esri@123'
        self.dbserver = '10.21.198.127:15223/xe'
        self.datatype = 'shuiying_photo'        # 要导入的excel数据类型
        self.collist = ''
        self.key_column = ''
        self.base_dir = r'原始照片'
        self.sy_dir = r'水印照片'         # 添加水印后存储的路径
        self.sy_img = r'sy.png'    # 要添加的水印图片位置
        self.log_file = r'log.txt'       # 日志文件路径
        self.file_name = file_name
        self.file_md5 = self.getfilemd5()
        self.headers = {
            'Connection': 'close',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        }
        self.mk_dir(self.base_dir)
        self.mk_dir(self.sy_dir)
        self.sheet_list =[]

    # 创建文件目录
    def mk_dir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)

    # 发送请求
    def send_request(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            msg = '请求%s出错，错误原因：%s'%(url, e)
            print(msg)
            self.write_content(msg, self.log_file, 'a')

    # 写入文件
    def write_content(self, content, path,mode = 'wb'):
        with open(path, mode) as f:
            f.write(content)

    # 获取文件md5值
    def getfilemd5(self):
        md5 = ''
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'rb') as f:
                contents = f.read()
                f.close()
                md5 = hashlib.md5(contents).hexdigest()
        return md5

    # 图片添加水印
    def img_add_sy(self, img_path, sy_path): 
        image = Image.open(img_path)
        rgba_image = image.convert('RGBA')
        rgba_watermark = Image.open(sy_path).convert('RGBA')
    
        image_x, image_y = rgba_image.size
        watermark_x, watermark_y = rgba_watermark.size
    
        # 缩放图片
        scale = 1   #（水印图片尺寸保持与原始图片一致）
        watermark_scale = max(image_x / (scale * watermark_x), image_y / (scale * watermark_y))
        new_size = (int(watermark_x * watermark_scale), int(watermark_y * watermark_scale))
        rgba_watermark = rgba_watermark.resize(new_size, resample=Image.ANTIALIAS)
        # 透明度
        #rgba_watermark_mask = rgba_watermark.convert("L").point(lambda x: min(x, 180))
        #rgba_watermark.putalpha(rgba_watermark_mask)
    
        watermark_x, watermark_y = rgba_watermark.size
        # 水印位置
        # rgba_image.paste(rgba_watermark, (image_x - watermark_x, image_y - watermark_y), rgba_watermark_mask) #右下角
        rgba_image.paste(rgba_watermark, (image_x - watermark_x, 0) )                       # 右上角 
        out = Image.composite(rgba_image, image, rgba_image) 
        return out.convert('RGB')       #去掉A（透明度）

    # 读取excel,保存到db
    def savecard_todb(self):
        self.sheet_list =[]
        filemd5 = self.getfilemd5()
        # 1.打开文件
        work_book = xlrd.open_workbook(self.file_name)
        # sheet数量
        sheet_count = len(work_book.sheets())

        db_conn = cx_Oracle.connect(
            self.dbuser, self.dbpwd, self.dbserver, encoding="UTF-8")
        db_cursor = db_conn.cursor()

        # 先删除已导入的数据
        sql_del = "delete from cigproxy.excel_table where type='{}' and z='{}'".format(self.datatype,self.file_md5)
        db_cursor.execute(sql_del)

        # 2.通过sheet页索引创建sheet页对象
        for i in range(sheet_count):
            work_sheet = work_book.sheet_by_index(i)

            # 3.获取excel文件sheet页 行列数
            self.totalcount = work_sheet.nrows
            num_cols = work_sheet.ncols
            num_collist = work_sheet.row_values(0)
            sheet_name = work_sheet.name

            self.mk_dir(self.base_dir+'\\'+sheet_name)
            self.mk_dir(self.sy_dir+'\\'+sheet_name)
            self.sheet_list.append(copy.deepcopy(sheet_name))
            print("正在导入Excel文件[{}],md5值:{},sheet[{}]的列为:{}...".format(os.path.basename(self.file_name),
                                                                      self.file_md5, sheet_name, num_collist))

            letter = 'ABCDEFGHIJKLMNOPQRSTUVWXY'        # excel_table的列为A,B,C,D这样的形式
            for x in range(len(num_collist)):
                cname = num_collist[x].strip().replace('\n', '').replace('\r', '').replace(
                    '（', '').replace('）', '')[0:8]    # oracle列名暂定8个汉字，25个英文字母的长度
                self.collist = self.collist + \
                    'ta.{} as "{}",'.format(letter[x], cname)
                if '身份证' in cname:                   # 身份证号码作为关联列进行匹配
                    self.key_column = letter[x]

            col = ''
            for l in letter[0:num_cols]:
                col = col + ',:' + l
            col = ':XH,:TYPE,:Z,:Y' + col

            sql_cmd = 'insert into cigproxy.excel_table({}) values ({})'.format(col.replace(':', ''), col)

            rn = 0
            for curr_row in range(self.totalcount):
                rn = rn + 1
                row = work_sheet.row_values(curr_row)
                row.insert(0, rn)
                row.insert(1, self.datatype)
                row.insert(2, self.file_md5)
                row.insert(3, sheet_name)
                db_cursor.execute(sql_cmd, row)
                if rn % 1000 == 0:                     # 每1000次提交一次结果
                    db_conn.commit()
            db_conn.commit()

            print("导入Excel文件[{}],md5值:{},sheet[{}]完成！".format(
                os.path.basename(self.file_name), self.file_md5, sheet_name))

        db_conn.commit()
        db_cursor.close()
        db_conn.close()

    # 查询人口数据，调用接口
    def get_photo(self):
        conn = cx_Oracle.connect(
            self.dbuser, self.dbpwd, self.dbserver, encoding="UTF-8")
        cursor = conn.cursor()

        # 查询人口数据
        sql1 = """SELECT * FROM (
                    select {} sfzh,tb.id,TC.FILE_NAME,TC.FILE_PATH,lower(substr(file_name,instr(file_name,'.',-1)+1)) file_type,
                        case when TC.visit_path like '/%' then 'http://jczl.giscloud.cx'||TC.visit_path else TC.visit_path end visit_path,
                        ROW_NUMBER() OVER(PARTITION BY TC.B_ID ORDER BY TC.CREATE_DATE DESC NULLS LAST,TC.FILE_SIZE DESC NULLS LAST) AS RN,TA.Y SHEET_NAME
                    from cigproxy.excel_table  ta
                    join cigproxy.zz_person tb on ta.{}=tb.card_num 
                    left join cigproxy.zz_attachment tc on tc.file_type='per-image' and tc.b_id=tb.id
                    where type='{}' and ta.z='{}'  
                ) where RN=1 and visit_path is not null""".format(self.key_column, self.key_column, self.datatype, self.file_md5)

        cursor.execute(sql1)
        rows = cursor.fetchall()                # 得到所有数据集
        for row in rows:
            card_num = row[0]
            file_type = row[4] 
            url = row[5].replace('\\','/')      #url地址\\不能识别，替换成/
            sheet_name = row[7]
            res = self.send_request(url)
            if res:
                full_path = r"{}\{}\{}.{}".format(self.base_dir,sheet_name,card_num,file_type)
                self.write_content(res.content, full_path)
                print('下载身份证%s的照片成功!' %(card_num))

        print('全部照片下载完成！')
        cursor.close()
        conn.close()

    # 添加水印并保存在相应目录
    def save_sy_img(self):
        for sheet_name in self.sheet_list:
            for file_name in os.listdir(self.base_dir+'/'+sheet_name):
                card_num = file_name.split('.')[0]
                try:
                    new_img = self.img_add_sy(self.base_dir+'/'+sheet_name+'/'+file_name, self.sy_img)
                    new_img.save(self.sy_dir+'/'+sheet_name+'/'+card_num+'.JPG')
                    print('身份证%s水印添加完成!' % (card_num))
                except Exception as e:
                    msg = '身份证%s水印添加失败,错误原因:%s' % (card_num,e)
                    print(msg)
                    self.write_content(msg, self.log_file, 'a')

    def start(self):
        self.savecard_todb()    # 读取excel,保存到db
        self.get_photo()        # 查询人口照片数据，调用照片接口，下载到本地
        self.save_sy_img()      # 添加水印并保存在相应目录

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        file_name = args[1] 
        if os.path.isfile(file_name):
            print("主线程(%s)启动" % (threading.current_thread().name))
            start = time.time()
            photo_s = photo_shuiying(file_name)
            photo_s.start()
            end = time.time()
            print("主线程(%s)结束,总耗时：%0.2f秒" %(threading.current_thread().name, end-start))
        else:
            print('Waring!!!,excel file path is not exist.')
    else:
        print('Erorr!!!,please enter excel file path.')
