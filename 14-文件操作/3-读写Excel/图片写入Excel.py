#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-27 20:21
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 图片写入Excel
# @Software: PyCharm

# coding=utf-8

import cx_Oracle
import os
import urllib.request
import xlsxwriter
from PIL import Image

def get_FileSize(filePath):
     
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)
 
    return round(fsize, 2)


#获取重点人员
def get_person(control_type):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj','esri@123','10.21.198.126:15214/xe')
    cursor = conn.cursor()

    sql =  ("with tb as ("+
    "select sys_guid() id,short_filename as filename,'图片' as category,tb.id as b_id,'per-image' FILE_TYPE,null as file_path,replace(filename,'C:\Data\证照库','http://10.21.198.201:8080/image') as visit_path, "+
    "        \"SIZE\" AS FILE_NAME,TO_DATE(replace(REPLACE(SUBSTR(lastmodifiedtime,0,10),' '),'月'),'dd-mm-YY') CREATE_DATE,'DKGLL0806' AS CREATE_USER  "+
    "    from BASE_SPT_XTDJ_ALLIMG ta  "+
    "        join cigproxy.zz_person@dlink2 tb on IC_CARD=tb.card_num "+
    ") "+
    " SELECT name AS 姓名	,CARD_NUM 身份证	,decode(GENDER,'1','男','2','女') 性别, "+
    "    TRUNC((to_char(sysdate, 'yyyyMMdd') - to_char(BIRTH_DATE, 'yyyyMMdd')) /10000) as 年龄,nvl(nvl(R_ADDR,d_addr),'浙江省湖州市长兴县') 户籍	,'cx_zz' 所属库,'' 照片,replace(visit_path,'\\','/') URL,name||'_'||card_num||'.png' FILENAME "+
    "FROM CIGPROXY.ZZ_PERSON@DLINK2  TA "+
    "    JOIN TB ON TA.ID=TB.B_ID AND FILE_TYPE='per-image'"+
    "WHERE  FOCUS_CONTROL like '%"+control_type+"%' and rownum<300")

    #print(sql)

    cursor.execute(sql);
    rows = cursor.fetchall()  # 得到所有数据集
    li =[];
    for row in rows:
        li.append({"name":row[0],"card_num":row[1],"gender":row[2],"age":row[3],"addr":row[4],"URL":row[7],"FILENAME":row[8]});
     #   print("%s, %s, %s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4], row[7], row[8]))

    print("Number of rows returned: %d" % cursor.rowcount)

    cursor.close()
    conn.close()
    return  li;

def save_excel(li,dirname):
    book = xlsxwriter.Workbook(r'backup\\长兴重点人口\\'+dirname+'\\'+dirname+'人员.xlsx')
    sheet = book.add_worksheet('重点人口')

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})

    sheet.set_column("A:A", 10)  # 设置A到D列的列宽为25
    sheet.set_column("B:B", 20)  # 设置A到D列的列宽为25
    sheet.set_column("C:D", 8)  # 设置A到D列的列宽为25
    sheet.set_column("E:E", 50)  # 设置A到D列的列宽为25
    sheet.set_column("F:F", 10)  # 设置A到D列的列宽为25
    sheet.set_column("G:G", 14)  # 设置A到D列的列宽为25
    sheet.write('A1', '姓名', bold)
    sheet.write('B1', '身份证号', bold)
    sheet.write('C1', '性别', bold)
    sheet.write('D1', '年龄', bold)
    sheet.write('E1', '户籍', bold)
    sheet.write('F1', '所属库', bold)
    sheet.write('G1', '证照', bold)

    for i in range(len(li)):
        if i>0:
            sheet.set_row(i, 86)  # 将行高从1改为20.

        sheet.write(i+1, 0, li[i]["name"])
        sheet.write(i+1, 1, li[i]["card_num"])
        sheet.write(i+1, 2, li[i]["gender"])
        sheet.write(i+1, 3, li[i]["age"])
        sheet.write(i+1, 4, li[i]["addr"])
        sheet.write(i+1, 5, "cx_zz")

        #下载证照
        #filename = download_img(li[i]["FILENAME"],li[i]["URL"], dirname,api_token)

        filename = r"backup\\长兴重点人口\\"+dirname+"\\img\\"+ li[i]["FILENAME"]

        im = Image.open(filename)#返回一个Image对象
        #print('宽：%d,高：%d'%(im.size[0],im.size[1]),end ='  ')
        x_scale,y_scale= round(70.0/im.size[0],2),round(78.0/im.size[1],2)
        #print('宽比例：%s,高比例：%s'%(x_scale,y_scale))

        #缩放比例调整有问题，需要图片自适应单元格大小
        size = get_FileSize(filename) 
        if size<50:
            x_scale,y_scale= 1.0,1.0  

        sheet.insert_image(i+1, 6, filename, {'x_scale': x_scale, 'y_scale': y_scale,'x_offset': 5,'y_offset': 5})

    book.close();

def download_img(img_name,img_url, dirname,api_token):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        filename = r"backup\\长兴重点人口\\"+dirname+"\\img\\"+ img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"

def imgtoexcel(filename):
    book = xlsxwriter.Workbook(r'backup\\pict.xlsx')
    sheet = book.add_worksheet('demo')

    bold = book.add_format({'bold': True})

    sheet.set_row(1,95)  # 将行高从1改为20.
    sheet.set_row(2,95)  # 将行高从1改为20.
    sheet.set_column("A:B", 15)  # 设置A到D列的列宽为25
    sheet.set_column("C:C", 21)  # 设置A到D列的列宽为25
    # Write some data headers. 带自定义粗体blod格式写表头
    sheet.write('A1', '姓名', bold)
    sheet.write('B1', '身份证号', bold)
    sheet.write('C1', '证照', bold)

    #for x in range(0,10):
    sheet.write(1,0, "张三")
    sheet.write(1,1, "311000000000")
    sheet.insert_image(1,2, filename, {'x_scale': 0.5, 'y_scale': 0.5})

    sheet.write(2,0, "李四")
    sheet.write(2,1, "314000000000")
    sheet.insert_image(2,2, filename, {'x_scale': 0.5, 'y_scale': 0.5})

    book.close()

if __name__ == '__main__':
    # 下载要的图片
    #img_url = "https://img-bss.csdn.net/1564022305551.jpg"
    api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    #f = download_img(img_url, api_token)
    #imgtoexcel(f);

    li = get_person('204');
    save_excel(li,"吸毒");

    print("")
    print("导入完成！！！")