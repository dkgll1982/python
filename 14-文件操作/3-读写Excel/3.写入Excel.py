# -*- coding: utf-8 -*-
# @Time : 2017/10/3 16:52 
# @File : xlsxWriterTest.py 
# @Software: PyCharm

import xlsxwriter,datetime,io,urllib.request

workbook = xlsxwriter.Workbook(r'backup\excel\Demo1.xlsx')    # 创建一个名为‘Demo1.xlsx’的工作表
worksheet = workbook.add_worksheet("人生苦短我用python")                                  # 创建一个工作表对象
worksheet2 = workbook.add_worksheet("C#")                                  
worksheet3 = workbook.add_worksheet("Java")                                     
worksheet3 = workbook.add_worksheet("golan")   
worksheet3 = workbook.add_worksheet()           # 添加一个表单，按照先后顺序，默认为sheet1,2,3...的形式，此处sheet5
worksheet3 = workbook.add_worksheet()           # 此处sheet6                              

worksheet.set_column('A:A', 20)                 # 设定第一列（A）的宽度为20px
worksheet.set_column('B:B', 22)                 # 设定第二列（A）的宽度为20px
# bold = workbook.add_format({'blod': True})

worksheet.write('A1', '简介')                  
worksheet.write('A2', '你好，世界！')           
worksheet.write('B1', '姓名')                   
worksheet.write('B2', '麦克.格雷迪！')           
worksheet.write('C1', '工作单位')                  
worksheet.write('C2', 'ESPN电视台')               
worksheet.write('D1', '网址')             


# 行列表示法的单元格下标以0作为起始值，如‘3,0’等价于‘A3’
worksheet.write_string(2, 0, '12222222222222222223')              # 使用列行表示法写入数字‘123’
worksheet.write(3, 0, '45111111111111111111116')              # 使用列行表示法写入数字‘456’
worksheet.write(4, 0, '=SUM(A3:A4)')    # 求A3:A4的和，并写入‘4,0’，即‘A5’ 
worksheet.write_number('A6', 2.3451)
worksheet.write_boolean('A7', False)
date_time = datetime.datetime.strptime('2013-01-23', '%Y-%m-%d')
date_format = workbook.add_format({'num_format': 'd mmmm yyyy'})
worksheet.write_datetime('A8', date_time, date_format)
worksheet.write_url('D2', 'https://www.python.org/')
worksheet.write_url('D3', 'ftp://www.python.org/')
worksheet.write_url('D4', 'https://www.python.org/')
worksheet.write_url('D5', 'mailto:jmcnamara@cpan.org')
#All of the these URI types are recognized by the write() method, so the following are equivalent:
#即write方法能自动识别URL，这里等效于write_url
worksheet.write('D6', 'https://www.python.org/')  # Same.
#可以使用string参数显示替代字符串：
worksheet.write_url('D7', 'https://www.python.org', string='Python home')

data = ('乔治华盛顿', '白宫', '总统网')

# Write the data to a sequence of cells.
worksheet.write_row('B8', data)
# The above example is equivalent to:
# worksheet.write('A1', data[0])
# worksheet.write('A2', data[1])
# worksheet.write('A3', data[2])
worksheet.write_column('B9', data)
 
#'hidden'
#'level'
#'collapsed'
cell_format = workbook.add_format({'bold': True, 'italic': True})   # 定一个加粗的格式对象

#set_row(row, height, cell_format, options)方法
#其作用是设置行单元格属性。
#- row（int类型），指定行位置，起始下标为0；
#- height（float类型），设置行高，单位为像素；
#- cell_format（format类型）指定格式对象；
#- options（dict类型）设置行hidden（隐藏）、level（组合分级）、collapsed（折叠）。 
worksheet.set_row(1, 14, cell_format)      # 第一行单元格高度为40px，且引用加粗格式对象
worksheet.set_row(5, 84, cell_format)      # 第五行单元格高度为40px，且引用加粗格式对象
worksheet.set_row(6, 84, cell_format)      # 第五行单元格高度为40px，且引用加粗格式对象
worksheet.set_row(7, 84, cell_format)      # 第五行单元格高度为40px，且引用加粗格式对象
worksheet.set_row(8, 84, cell_format)      # 第五行单元格高度为40px，且引用加粗格式对象
worksheet.set_row(9, 84, cell_format)      # 第五行单元格高度为40px，且引用加粗格式对象

#set_column(first_col, last_col, cell_format, options)方法
worksheet.set_column(1,3,15, cell_format)      # 第一行单元格高度为40px，且引用加粗格式对象

#insert_image()方法接受字典形式的可选参数来定位和缩放图片。可用的参数和它们的默认值有：
#{
#    'x_offset': 0,
#    'y_offset': 0,
#    'x_scale': 1,
#    'y_scale': 1,
#    'url': None,
#    'tip': None,
#    'image_data': None,
#    'positioning': None,
#}

option = {
    'x_offset': 5,
    'y_offset': 5,
    'x_scale': 0.1,
    'y_scale': 0.1,
    'url': 'https://blog.csdn.net/auserbb/article/details/79259328',
    'tip': '我是图片',
    'image_data': None,
    'positioning': None
}
worksheet.insert_image('B6', r'images\miaomiao.png',option)                 # 在A5单元格插入图片 
print(option)
worksheet.insert_image('B7', r'images\jpg\20160704101150_fUYEw.jpeg',option)

url = 'http://b-ssl.duitang.com/uploads/item/201709/07/20170907152318_YX2Ax.jpeg'
#读取网络图片
image_data = io.BytesIO(urllib.request.urlopen(url).read())

option2 = {
    'x_offset': 5,
    'y_offset': 5,
    'x_scale': 0.09,
    'y_scale': 0.14,  
    'positioning': None,
    'image_data': image_data
}

worksheet.insert_image('C6', url, option2)

workbook.close()        # 关闭Excel文件