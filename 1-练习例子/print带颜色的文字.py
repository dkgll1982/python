#!/usr/bin/env python
#-*- coding:utf-8 -*-
#参考链接：https://www.cnblogs.com/easypython/p/9084426.html
info = input("Please  Introduce yourself: ")
print('\033[1;33mWe asked him to introduce himself first.He said \" %s .\"\033[3;31m' %info)
print('这行是上一行结尾的颜色输出效果 ')

print('\033[0m这是显示方式0')
print('\033[1m这是显示方式1')
print('\033[4m这是显示方式4')
print('\033[5m这是显示方式5')
print('\033[7m这是显示方式7')
print('\033[8m这是显示方式8')
print('\033[30m这是前景色0')
print('\033[31m这是前景色1')
print('\033[32m这是前景色2')
print('\033[33m这是前景色3')
print('\033[34m这是前景色4')
print('\033[35m这是前景色5')
print('\033[36m这是前景色6')
print('\033[37m这是前景色7')
print('\033[40m这是背景色0')
print('\033[41m这是背景色1')
print('\033[42m这是背景色2')
print('\033[43m这是背景色3')
print('\033[44m这是背景色4')
print('\033[45m这是背景色5')
print('\033[46m这是背景色6')
print('\033[47m这是背景色7')

#!/usr/bin/env python
#-*- coding:utf-8 -*-
print('\033[1;31;40m')     #下一目标输出背景为黑色，颜色红色高亮显示
print('*' * 50)
print('**\033[7;31m错误次数超限，用户已被永久锁定，请联系管理员！\033[1;31;40m'+'**')  #字体颜色红色反白处理
print('*' * 50)
print('\033[0m')