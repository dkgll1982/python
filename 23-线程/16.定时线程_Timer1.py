# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:何以解忧
@Blog(个人博客地址): shuopython.com
@WeChat Official Account(微信公众号)：猿说python
@Github:www.github.com

@File:python_timer.py
@Time:2019/10/22 21:25

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

# 导入线程模块
import threading

def thread_Timer():
    print("该起床啦...5秒之后再次呼叫你起床...")

    # 声明全局变量
    global t1
    # 创建并初始化线程
    t1 = threading.Timer(5,thread_Timer)
    # 启动线程
    t1.start()

if __name__ == "__main__":
    # 创建并初始化线程
    t1 = threading.Timer(5, thread_Timer)
    # 启动线程
    t1.start()