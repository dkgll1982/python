# -*- coding: utf-8 -*-
# @Time    : 2018/05/23
# @Author  : suixin
# @Email   : 350606539@QQ.com
# @File    : 异常.py
import traceback

a=12
b=20
e="*"

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')



def myFunc():
    try:
        c=2*"儿童、f"
        d=a*b
        f=((a**b)**b)**b/2
        print(f)
    except Exception as e:
        print(traceback.format_exc());
    except BaseException as e:
        #traceback.print_exc()
        traceback.print_exc(file=open('C:\\Users\\dkgll\\Desktop\\python目录\\python——error.log.txt','a+'));
        print(traceback.format_exc());
    print("继续执行")
myFunc()