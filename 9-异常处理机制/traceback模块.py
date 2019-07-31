#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 20:47:21 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 20:47:21 
# @Software: vscode 
import traceback

class SelfException(Exception): pass

def main():
    firstMethod()
def firstMethod():
    secondMethod()
def secondMethod():
    thirdMethod()
def thirdMethod():
    raise SelfException("自定义异常信息")
#main()


#traceback.print_exc()：将异常传播轨迹信息输出到控制台或指定文件中。
#format_exc()：将异常传播轨迹信息转换成字符串。

a=12
b=20
e="*"

def myFunc():
    try:
        c=2*"儿童、f"
        d=a*b
        #f=((a**b)**b)**b/0
        #print(f)
        raise BaseError

    except Exception as e:
        print('222222222222222')
        print(traceback.format_exc());
    except BaseException as e:
        # 捕捉异常，并将异常传播信息输出控制台
        #traceback.print_exc()
        # 捕捉异常，并将异常传播信息输出指定文件中
        traceback.print_exc(file=open('C:\\Users\\dkgll\\Desktop\\python目录\\python——error.log.txt','a+'));
        print('-'*40)
        print(traceback.format_exc());
    print("继续执行")
myFunc()
print('-'*40)