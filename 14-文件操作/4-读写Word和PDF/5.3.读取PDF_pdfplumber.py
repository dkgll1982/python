#参考链接：https://www.cnblogs.com/gl1573/p/10064438.html
import pdfplumber

path = r'backup\pdf\测试.pdf'
pdf = pdfplumber.open(path)

#可以读取电子表格
for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())                        

    for table in page.extract_tables():
        # print(table)
        for row in table:
            print(row)
        print('---------- 分割线 ----------')

pdf.close()