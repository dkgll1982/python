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

def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy/cigproxy@127.0.0.1/orcl')
    cursor = conn.cursor()

    cursor.execute( " SELECT name AS 姓名	,CARD_NUM 身份证	,decode(GENDER,'1','男','2','女') 性别,"+
                    "   TRUNC((to_char(sysdate, 'yyyyMMdd') - to_char(BIRTH_DATE, 'yyyyMMdd')) /10000) as 年龄,R_ADDR 户籍	,'' 所属库,'' 照片,replace(visit_path,'\\','/') URL,name||'_'||card_num||'.png' FILENAME"+
                    " FROM CIGPROXY.ZZ_PERSON@link_cx  TA "+
                    "   JOIN CIGPROXY.zz_attachment@link_cx TB ON TA.ID=TB.B_ID AND FILE_TYPE='per-image' AND TB.CREATE_DATE>TO_DATE('2019-06-01','YYYY-MM-DD')"+
                    " WHERE FOCUS_CONTROL IS NOT NULL  AND R_ADDR LIKE '浙江省湖州市长兴县%'");
    rows = cursor.fetchall()  # 得到所有数据集
    li =[];
    for row in rows:
        li.append({"name":row[0],"card_num":row[1],"gender":row[2],"age":row[3],"addr":row[4],"URL":row[7],"FILENAME":row[8]});
     #   print("%s, %s, %s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4], row[7], row[8]))

    print("Number of rows returned: %d" % cursor.rowcount)

    cursor.close()
    conn.close()
    return  li;

def save_excel(li):
    book = xlsxwriter.Workbook('C:\\Users\\dkgll\\Desktop\\python目录\\重点人口\\重点人口证照.xlsx')
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
        filename = download_img(li[i]["FILENAME"],li[i]["URL"], api_token)
        sheet.insert_image(i+1, 6, filename, {'x_scale': 0.2, 'y_scale': 0.18,'x_offset': 5,'y_offset': 5})

    book.close();

def download_img(img_name,img_url, api_token):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        filename = "C:\\Users\\dkgll\\Desktop\\python目录\\重点人口\\img\\"+ img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"

def imgtoexcel(filename):
    book = xlsxwriter.Workbook('C:\\Users\\dkgll\\Desktop\\python目录\\pict.xlsx')
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

    li = get_person();
    save_excel(li);
    print("")
    print("导入完成！！！")