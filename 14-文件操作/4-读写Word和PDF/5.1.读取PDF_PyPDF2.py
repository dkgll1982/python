from PyPDF2 import PdfFileReader, PdfFileWriter
#读取乱码问题未解决
 
readFile = r'backup\pdf\test.pdf'
# 获取 PdfFileReader 对象
pdfFileReader = PdfFileReader(readFile) # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
# 获取 PDF 文件的文档信息
documentInfo = pdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)
# 获取页面布局
pageLayout = pdfFileReader.getPageLayout()
print('pageLayout = %s ' % pageLayout)
 
# 获取页模式
pageMode = pdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)
 
xmpMetadata = pdfFileReader.getXmpMetadata()
print('xmpMetadata = %s ' % xmpMetadata)
 
# 获取 pdf 文件页数
pageCount = pdfFileReader.getNumPages()
 
print('pageCount = %s' % pageCount)
for index in range(0, pageCount):
  # 返回指定页编号的 pageObject
  pageObj = pdfFileReader.getPage(index)
  print('index = %d , pageObj = %s' % (index, type(pageObj))) # <class 'PyPDF2.pdf.PageObject'>
  # 获取 pageObject 在 PDF 文档中处于的页码
  pageNumber = pdfFileReader.getPageNumber(pageObj)
  print('pageNumber = %s ' % pageNumber)

def getPdfContent(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0, pdf.getNumPages()):
        pageObj = pdf.getPage(i)
 
    extractedText = pageObj.extractText()
    content += extractedText + "\n"
    # return content.encode("ascii", "ignore")
    return content.encode("gbk", "ignore")

#print(getPdfContent(readFile))

print('='*60)

from PyPDF2.pdf import PdfFileReader 
import os
import os.path
from time import strftime,strptime
 

def getDataUsingPyPdf2(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0, pdf.getNumPages()):
        extractedText = pdf.getPage(i).extractText()
        content +=  extractedText + "\n"
    return content.encode("utf-8", "ignore")
    #return content


def removeBlankFromList(list_old):
    list_new = []
    for i in list_old:
        if i != '':
            list_new.append(i)
    return list_new


if __name__ == '__main__':  
    filename_long = readFile
    outputString = getDataUsingPyPdf2(filename_long)
    outputString = outputString.split('\n')
    outputString_new = removeBlankFromList(outputString)
    outputString = outputString_new
    try:
        rectime = strftime('%Y-%m-%d %H:%M:%S',strptime(outputString[1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
    except:
        rectime = strftime('%Y-%m-%d %H:%M:%S',strptime(outputString[-1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
        pn = outputString[0].split()
        if len(pn) > 1:
            topbut = pn[1]
        else:
            topbut = ''
        pn = pn[0].strip() 
        print('topbut=%s' % topbut) 
