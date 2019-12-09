import csv
#参考链接：https://blog.csdn.net/weixin_36279318/article/details/79078255

#今天在导入公司的csv数据宽表时，遇到了csv中表头内容为中文的问题。
#系统提示：
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 0: invalid start byte 
#解决办法
#with open(文件名,encoding='gbk',errors="ignore") as f:

csv_reader = csv.reader(open(r'backup\污染企业分布.csv', encoding='GBK',errors="ignore"))

# rows=[row for row in  csv_reader]
# print(rows[0])
# print(rows[1])

print('*'*40)

#2.读取文件第一行数据
# head_row=next(csv_reader)
# print(head_row)
# head_row=next(csv_reader)
# print(head_row)

#4.获取文件头及其索引
for index,column_header in enumerate(csv_reader):
    print(index,column_header)

print('*'*40)

for row in csv_reader:
    print(row[0],row[1],row[3])
