#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-10 21:19:26 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-10 21:19:26 
# @Software: vscode  

import  PyPDF2

pdfobj = open(r'C:\Users\dkgll\Desktop\python目录\zipfile\odps.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfobj)

pdfwr = PyPDF2.PdfFileWriter()                  #新的PDF对象
for pageNum in range(pdfRd.numPages):
    pdfwr.addPage(pdfRd.getPage(pageNum))       #一次将一页放入新的PDF对象

pdfwr.encrypt('deepstone')                      #执行加密
encrypdf = open(r'C:\Users\dkgll\Desktop\python目录\zipfile\new.pdf','wb')  #开启二进制文件供写入
pdfwr.write(encrypdf)                           #执行写入
encrypdf.close()

