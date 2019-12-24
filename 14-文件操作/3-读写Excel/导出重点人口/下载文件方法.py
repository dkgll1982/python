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

api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"

#获取重点人员
def get_person(control_type):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj','esri@123','10.21.198.126:15214/xe')
    cursor = conn.cursor()

    # sql =  ("with tb as ("+
    # "select sys_guid() id,short_filename as filename,'图片' as category,tb.id as b_id,'per-image' FILE_TYPE,null as file_path,replace(filename,'C:\Data\证照库','http://10.21.198.201:8080/image') as visit_path, "+
    # "        \"SIZE\" AS FILE_NAME,TO_DATE(replace(REPLACE(SUBSTR(lastmodifiedtime,0,10),' '),'月'),'dd-mm-YY') CREATE_DATE,'DKGLL0806' AS CREATE_USER  "+
    # "    from BASE_SPT_XTDJ_ALLIMG ta  "+
    # "        join cigproxy.zz_person@dlink2 tb on IC_CARD=tb.card_num "+
    # ") "+
    # " SELECT name AS 姓名	,CARD_NUM 身份证	,decode(GENDER,'1','男','2','女') 性别, "+
    # "    TRUNC((to_char(sysdate, 'yyyyMMdd') - to_char(BIRTH_DATE, 'yyyyMMdd')) /10000) as 年龄,nvl(nvl(R_ADDR,d_addr),'浙江省湖州市长兴县') 户籍	,'cx_zz' 所属库,'' 照片,replace(visit_path,'\\','/') URL,name||'_'||card_num||'.png' FILENAME "+
    # "FROM CIGPROXY.ZZ_PERSON@DLINK2  TA "+
    # "    JOIN TB ON TA.ID=TB.B_ID AND FILE_TYPE='per-image'"+
    # "WHERE  FOCUS_CONTROL like '%"+control_type+"%'")

    #信访人员统计
    sql =  ("SELECT name AS 姓名 ,CARD_NUM 身份证        ,"+
    "           decode(GENDER,'1','男','2','女') 性别,     "+
    "           TRUNC((to_char(sysdate, 'yyyyMMdd') - to_char(BIRTH_DATE, 'yyyyMMdd')) /10000) as 年龄,"+
    "           nvl(nvl(R_ADDR,d_addr),'浙江省湖州市长兴县') 户籍  ,'cx_zz' 所属库,'' 照片,"+
    "           replace(visit_path,'\','/') URL,name||'_'||card_num||'.png' FILENAME "+
    "        FROM CIGPROXY.ZZ_PERSON@DLINK2  TA    "+
    "           JOIN CIGPROXY.ZZ_ATTACHMENT@DLINK2 TB ON TA.ID=TB.B_ID AND FILE_TYPE='per-image'"+
    "        WHERE TA.CARD_NUM IN("+
    "                '33052219441118102X',"+
    "                '33052219650804002X',"+
    "                '330522193801234110',"+
    "                '330522196010310627',"+
    "                '330522195411111333',"+
    "                '33052219570812002X',"+
    "                '330522196203073728',"+
    "                '330522196211064119',"+
    "                '330522195707035114',"+
    "                '330522194101263310',"+
    "                '330522197012035969',"+
    "                '330522194505311016',"+
    "                '330522196606036913',"+
    "                '330522197012293933',"+
    "                '330522194402023118',"+
    "                '330522195703283938',"+
    "                '330522195602041032',"+
    "                '330522196105174517',"+
    "                '330522194708085522',"+
    "                '330522195301104722',"+
    "                '330522195107246313',"+
    "                '330522195109231318',"+
    "                '330522194808011045',"+
    "                '33052219720302471X',"+
    "                '330522198202135711',"+
    "                '33052319661204211X',"+
    "                '330522197501302132',"+
    "                '330522199306112113',"+
    "                '330522194510102518',"+
    "                '330522197411042517',"+
    "                '330522197206142519',"+
    "                '330522197606022719',"+
    "                '33052219620429352X',"+
    "                '330522198101242112',"+
    "                '210682196601010073',"+
    "                '33052219791106371X',"+
    "                '330522197807093716',"+
    "                '33052219791203411X',"+
    "                '330522197708314114',"+
    "                '330522198006163715',"+
    "                '33052219761103153X',"+
    "                '330522196704020069',"+
    "                '330522195706190032',"+
    "                '330522196005065516',"+
    "                '512226196808067325',"+
    "                '330522196110225534',"+
    "                '330522199401215313',"+
    "                '512226196404040951',"+
    "                '330522198111135118',"+
    "                '330522197912195132',"+
    "                '33052219760202571X',"+
    "                '330522197701265137',"+
    "                '330522197004265115',"+
    "                '330522196610261566',"+
    "                '362131196304245033',"+
    "                '330522196511261050',"+
    "                '330522196510051019',"+
    "                '330522195404016928',"+
    "                '330522199905073312',"+
    "                '330522198011103311',"+
    "                '330522195011226959',"+
    "                '330522196305224910',"+
    "                '330522198104174186',"+
    "                '330522196505181310',"+
    "                '330522197403101310',"+
    "                '330522195205171319',"+
    "                '330522197111071332',"+
    "                '330522194102035926',"+
    "                '330522196311015939',"+
    "                '330522194611096516',"+
    "                '330522195312236536',"+
    "                '330522194712185913',"+
    "                '330522196401016513',"+
    "                '330522197307265913',"+
    "                '330522198109056517',"+
    "                '330522196701116727',"+
    "                '330522196812275931',"+
    "                '330522195511235931',"+
    "                '330522197710095918',"+
    "                '330522197809226316',"+
    "                '330522195206156313',"+
    "                '330522196207146736',"+
    "                '330522197612111910',"+
    "                '330522197607254335',"+
    "                '330522197302063917',"+
    "                '330522195603133916',"+
    "                '330522198110221014',"+
    "                '330522198001141015',"+
    "                '330522197112250033',"+
    "                '330522196603311035',"+
    "                '33052219730316041X',"+
    "                '330522198809110422')");

    print(sql)
    
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
<<<<<<< HEAD
    book = xlsxwriter.Workbook(r'backup\长兴重点人口\\'+dirname+'\\'+dirname+'人员.xlsx')
=======
    book = xlsxwriter.Workbook(r'backup\\长兴重点人口\\'+dirname+'\\'+dirname+'人员.xlsx')
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
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
        filename = download_img(li[i]["FILENAME"],li[i]["URL"], dirname,api_token)
        sheet.insert_image(i+1, 6, filename, {'x_scale': 0.2, 'y_scale': 0.18,'x_offset': 5,'y_offset': 5})

    book.close();

def download_img(img_name,img_url, dirname,api_token):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
<<<<<<< HEAD
        filename = r"backup\长兴重点人口\\"+dirname+r"\img\\"+ img_name
=======
        filename = r"backup\\长兴重点人口\\"+dirname+"\\img\\"+ img_name
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed" 