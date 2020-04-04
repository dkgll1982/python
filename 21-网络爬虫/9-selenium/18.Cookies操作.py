#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-04 18:04:09 
# @Remark: 人生苦短，我用python！
# 前后端写入Cookie时domain的一个问题: https://blog.csdn.net/u010633266/article/details/103029978

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
print('cookies1:',browser.get_cookies())

#不传domain，默认当前域名；
#只要传了domain，则会强制在前面加上一个.，不管是一级还是二级域名；
#domain只能“小于等于”当前域名，否则写入不成功；
browser.add_cookie({
    'name':'dkgll',
    'domain':'.zhihu.com',
    'value':'suixin'
})
print('cookies2:',browser.get_cookies())
browser.delete_all_cookies()
print('cookies3:',browser.get_cookies())

