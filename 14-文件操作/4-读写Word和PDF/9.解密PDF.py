#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-10 21:07:03 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-10 21:07:03 
# @Software: vscode 

#检查PDF是否被加密
import  PyPDF2

def encryptYouN(fn):
    pdfobj = open(fn,'rb')
    pdfRd = PyPDF2.PdfFileReader(pdfobj)
    if pdfRd.isEncrypted:
        print('%s 文件有加密' % fn)
    else:
        print('%s 文件没有加密'% fn)

encryptYouN(r'C:\Users\dkgll\Desktop\python目录\zipfile\13240119730222428X.pdf')
encryptYouN(r'C:\Users\dkgll\Desktop\python目录\zipfile\new.pdf')

pdfobj = open(r'C:\Users\dkgll\Desktop\python目录\zipfile\new.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfobj)

# 可能报错（NotImplementedError: only algorithm code 1 and 2 are supported）：因为加密软件本身版本过高导致
# 参考链接：https://blog.csdn.net/weixin_39278265/article/details/84799843
if pdfRd.decrypt('123456'):     #第一次故意输错密码，提示“解密失败”
    pageobj = pdfRd.getPage(0)
    txt = pageobj.extractText()
    print(txt)
else:
    print('解密失败')

if pdfRd.decrypt('deepstone'):
    pageobj = pdfRd.getPage(0)
    txt = pageobj.extractText()
    print('解密成功，文本内容：',txt)
else:
    print('解密失败')    