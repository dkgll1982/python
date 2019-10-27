# –*– coding: utf-8 –*–
# @Time      : 2019/2/18 21:21
# @Author    : Damon_duanlei
# @FileName  : read_excel.py
# @BlogsAddr : https://blog.csdn.net/Damon_duanlei

import xlrd

#-----------------------------------------------------------------------------
#--                              xlrd模块                                   --
#-- 参考链接：  https://www.cnblogs.com/zhang-jun-jie/p/9273721.html         --
#-----------------------------------------------------------------------------

#1.打开文件：
#xlrd.open_workbook(参数)
#参数说明	        释义
#filename	        要打开的电子表格文件的路径
#logfile	        写入消息和诊断信息的日志文件
#verbosity	        增加写入日志文件的跟踪材料的数量
#use_mmap	        是否使用 mmap 模块
#file_contents	    文件内容
#encoding_override	文件编码
#formatting_info	格式化信息
#on_demand=False	False状态为没有特殊需求，默认加载全部
#ragged_rows=False	False状态为空行用空单元格
#x1 = xlrd.open_workbook("data.xlsx")

#2.获取sheet：
#获取所有sheet名字：x1.sheet_names（）
#获取sheet数量：x1.nsheets
#获取所有sheet对象：x1.sheets()
#通过sheet名查找：x1.sheet_by_name("test”)
#通过索引查找：x1.sheet_by_index(3) 

#3.获取sheet的汇总数据： 
#获取sheet名：sheet1.name
#获取总行数：sheet1.nrows
#获取总列数：sheet1.ncols
 
#4.单元格批量读取：
# a）行操作：
#sheet1.row_values(0)           # 获取第一行所有内容，合并单元格，首行显示值，其它为空。
#sheet1.row(0)         　　     # 获取单元格值类型和内容
#sheet1.row_types(0)            # 获取单元格数据类型
#b) 表操作 
#sheet1.row_values(0, 6, 10)   # 取第1行，第6~10列（不含第10表）
#sheet1.col_values(0, 0, 5)    # 取第1列，第0~5行（不含第5行）
#sheet1.row_slice(2, 0, 2)     # 获取单元格值类型和内容
#sheet1.row_types(1, 0, 2)     # 获取单元格数据类型

#5.特定单元格读取：
# a) 获取单元格值：
#sheet1.cell_value(1, 2)
#sheet1.cell(1, 2).value
#sheet1.row(1)[2].value 
#b) 获取单元格类型：
#sheet1.cell(1, 2).ctype
#sheet1.cell_type(1, 2)
#sheet1.row(1)[2].ctype

#6.(0,0)转换A1:
#xlrd.cellname(0, 0)   # (0,0)转换成A1
#xlrd.cellnameabs(0, 0) # (0,0)转换成$A$1
#xlrd.colname(30)  # 把列由数字转换为字母表示

#、数据类型：
#空：0
#字符串：1
#数字：2
#日期：3
#布尔：4
#error：5

# 1. 打开文件
work_book = xlrd.open_workbook(r"C:\Users\dkgll\Desktop\python目录\长兴县国家重点扶持高新技术企业_科技局.xls")
# 2. 显示所有的sheet页
sheet_names = work_book.sheet_names()
print(sheet_names)

# 3. 创建sheet页对象
# 3.1 通过sheet页名称创建sheet页对象
work_sheet_1 = work_book.sheet_by_name("有效期内")
# 3.2 通过sheet页索引创建sheet页对象
work_sheet_2 = work_book.sheet_by_index(0)

# 4.获取excel文件sheet页 行列数
# 4.0sheet数量
num_sheets = work_book.nsheets
print("Excel文件的sheet数为:{}个".format(num_sheets))
# 4.1 行数
num_rows = work_sheet_1.nrows
print("Excel文件的行数为:{}行".format(num_rows))
# 4.2 列数
num_cols = work_sheet_2.ncols
print("Excel文件的列数为:{}列".format(num_cols))

print('\r\n'+'='*40+'\r\n')
# 5. 读取单元格内容
# 5.1整行读取

for curr_row in range(num_rows):
    row = work_sheet_1.row_values(curr_row)
    print('row%s is %s' % (curr_row, row))

print('\r\n'+'='*40+'\r\n')
# 5.2整列读取

for curr_col in range(num_cols):
    col = work_sheet_2.col_values(curr_col)
    print('col%s is %s' % (curr_col, col))

print('\r\n'+'='*40+'\r\n')
# 5.3逐个单元格读取

for rown in range(num_rows):
    for coln in range(num_cols):
        cell_vlue = work_sheet_1.cell_value(rown, coln)
        # 如需读到空即开始读取下一列 可使用下方注释代码
        # if cell_vlue is None:
        #     break
        print("{}行{}列:{}\t".format(rown, coln, cell_vlue), end="")
        if coln == 3:
            print("")

print('\r\n'+'='*40+'\r\n')
# 单元格批量读取
print(work_sheet_1.row_values(0))  # 获取第一行所有内容，合并单元格，首行显示值，其它为空。
print(work_sheet_1.row(2))         # 获取单元格值类型和内容
print(work_sheet_1.row_types(2))   # 获取单元格数据类型

print('\r\n'+'='*40+'\r\n')
# 列操作
print(work_sheet_1.row_values(10, 2, 5))   # 取第1行，第6~10列（不含第10表）
print(work_sheet_1.col_values(1, 2, 5))    # 取第1列，第0~5行（不含第5行）
print(work_sheet_1.row_slice(2, 0, 2))     # 获取单元格值类型和内容，同sheet1.row(0)
print(work_sheet_1.row_types(1, 0, 2))     # 获取单元格数据类型

print('\r\n'+'='*40+'\r\n')
# 特定单元格读取(只取一个单元格)
# 取值
print(work_sheet_1.cell_value(1, 5))    #第几行第几列
print(work_sheet_1.cell(1, 5).value)    #第几行第几列
print(work_sheet_1.row(1)[5].value)     #第几行第几列

#取类型
print(work_sheet_1.cell(1, 2).ctype)
print(work_sheet_1.cell_type(1, 2))
print(work_sheet_1.row(1)[2].ctype)