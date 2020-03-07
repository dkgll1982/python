#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-21 19:20:37 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-21 19:20:37 
# @Software: vscode 
from urllib import request
import http.cookiejar as cookielib
import urllib
import json

# 流程
# 1：判断cookie是否存在且未过期
# 2：不存在或过期则重新登录，并更新持久化cookie，有效则跳过此步 
# 3：通过有效cookie调用接口，如果cookie无效重新回到第一步
  