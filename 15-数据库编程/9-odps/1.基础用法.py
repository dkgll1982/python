# 参考链接：https://blog.csdn.net/weixin_34318326/article/details/90195822?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1

from odps import ODPS
#链接odps
o = ODPS(access_id='AABc4DQCdfGbucSy', #登陆账号
         secret_access_key='b61OsjXABc73syEZdkcqoCSIsMHNdO', #登陆密码
         project='hzdn_cx_mbdc_prod1', #odps上的项目名称 
         endpoint='http://service.cn-huzhou-hzdsj-d01.odps.ops.cloud.huzhou.gov.cn/api') #官方提供的接口

#定义处理非法字符的方法
def illegal_char_rm(l):
    la = list()
    from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
    for record in l: #遍历每条表记录
        for index,value in enumerate(record.values): #遍历记录的每一列的值，record.values类型为list，取list的index和value需要用enumerate，不然会报错
            record[index]=ILLEGAL_CHARACTERS_RE.sub('', value) if isinstance(value,str) else value #如果值类型为字符串，替换为空，否则保留原值
        la.append(record)
    return la

#定义写Excel的方法
def write_excel(workbook_name,sheet_name,data):
    data = illegal_char_rm(data) #写入前进行非法字符处理
    import openpyxl
    workbook = openpyxl.Workbook() #创建工作簿workbook
    sheet = workbook.active #创建工作表sheet，默认使用active页
    sheet.title = sheet_name #给工作表赋名
    sheet.append(list(data[0]._name_indexes.keys())) #取sql查询结果的字段名
    for record in data:
        sheet.append(record.values) #取每条记录
    workbook.save(workbook_name) #保存工作薄并命名

#定义将odps中已存在的表写入Excel方法
def write_excel_form_odpstable(workbook_name,sheet_name,odps_table_name):
    data = [value for value in o.read_table(odps_table_name)]
    write_excel(workbook_name,sheet_name,data)

#将odps中已存在的表写入Excel方法
workbook_name=r'test'+'.xlsx'  #这里可以定义存储路径，不要忘了前边的r，即保留字符串，反斜杠不转义
sheet_name='aa'

#将odps中已存在的表写入Excel
odps_table_name='stg_zs_qsxx_cx' #odps中已存在的表的名字，没有分区的
write_excel_form_odpstable(workbook_name,sheet_name,odps_table_name)
