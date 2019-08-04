import xlsxwriter

path="C:\\Users\dkgll\\Desktop\python目录\\103.xlsx";
workbook = xlsxwriter.Workbook(path)
# 在G盘xxoo文件下创建103的excel
worksheet = workbook.add_worksheet('s001')
# 103的excel的sheet页名称为s001
worksheet.write(0, 0, 123456)
worksheet.write(2, 1, 664)
worksheet.write(1, 5, 250)
# 写入信息
workbook.close()

