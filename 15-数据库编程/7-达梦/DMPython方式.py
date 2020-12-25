# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020/12/22 16:36 
# @Remark: Life is short, I use python！
# @Software: PyCharm
# 参考链接：http://www.dameng.com/teachers_view.aspx?TypeId=183&Id=735&FId=t26:183:26
 
import dmPython

conn=dmPython.connect(user='SYSDBA',password='tggc12345',server='10.21.198.201',port=5236)
cursor = conn.cursor()
cursor.execute('select * from DBA_TABLES WHERE ROWNUM<10')
values = cursor.fetchall()

print(values)

cursor.close()
conn.close()

# dmPython的安装：https://blog.csdn.net/weixin_45699851/article/details/110486975
# 如果已经部署DM客户端，则进行如下操作：
# 1、下载并解压源码包dmPython.zip
# unzip dmPython.zip
# 2、运行下面的命令：
# cd dmPython
# python setup.py install

# 3、配置环境变量
# dmPython 的运行需要使用 dpi 动态库，用户应将 dpi 所在目录（一般为 DM 安装目录中的 bin 目录）加入系统环境变量,
# 将dmdbms\bin目录添加到系统的环境变量中
