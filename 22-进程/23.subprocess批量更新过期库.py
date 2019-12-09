#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-25 13:09:41 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-25 13:09:41 
# @Software: vscode 

#参考链接：https://www.cnblogs.com/luckjun/p/4958338.html
#查看系统里过期的python库，可以用pip命令

#pip list  #列出所有安装的库

#pip list --outdated #列出所有过期的库
#对于列出的过期库，pip也提供了更新的命令

#pip install --upgrade 库名 
#但此命令不支持全局全部库升级。
 
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)

#subprocess模块中的Popen与call的区别

#1.subprocess.call(*popenargs, **kwargs)
#　　运行命令。该函数将一直等待到子进程运行结束，并返回进程的returncode。如果子进程不需要进行交互,就可以使用该函数来创建。

#2.subprocess.Popen
#subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。它的构造函数如下：
#subprocess.Popen(args, bufsize=0, executable=None, \
#                             stdin=None, stdout=None, stderr=None, \
#                             preexec_fn=None, close_fds=False, shell=False, \
#                             cwd=None, env=None, universal_newlines=False,\
#                             startupinfo=None, creationflags=0) 