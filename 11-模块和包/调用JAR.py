# -*- coding:utf-8 -*-
# Filename: main.py
# Author：hankcs
# 参考：https://www.cnblogs.com/botoo/p/8038507.html

from jpype import *
import jpype 
import json

a = r'C:\Program Files\Java\jre1.8.0_181\bin\server\jvm.dll' #jvm.dll启动成功
jpype.startJVM(a, "-Djava.class.path=D:\\data\\gtapi.jar")   #jar包的位置
pdf = JClass('testrsr.PdfControllerTest')                    #java的类名

userId= "cc0689a0-d286-43f3-ba91-658f1bc1f125";
privateKey = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANql8gtIgx+LJGmV024PzHJJ/qO5Fvj5aaXXC1ZVyTsxbOMylU65jc3u1ig83M8y/iCHrvbLzQ1D0GY15ywepJAkykUZxaQhA1/hnSGMwQA1IvSk7xsRfzM4CgNtPqJgfY6Q5/wRfa+90vvHnzPf6/NgKCf4RJ3UOL2i6JT6jA/PAgMBAAECgYEAo6xjkyS121AKcuuQOSyka82OS7sLQldaSaW/u+I94AywqSa9dBAc4dJvB/H/jS9r4qgPRnnrRonEIC8rnPBXWJmmMJRYt96cvCRcmWfHcv8G2yg+3Zq48ImduIhfRwgABZz+2mFJVtO7cef3mV/9CWV+rkvVGHO+dMBZM+YT/WECQQDvO2kulclJrHvcHOnVKzyMgPn5TMavicpYOo6N+gU90DNcjgjQWazPK3LuTyejiOD9pMERJLHyv45cZVtBL1xxAkEA6fkxyWXB/t06wLc+rnQzs5on+BtXMom3B5e3AdhIH8vj19iFZRMf70YjfP/+VjRclGjM9ord+Eha9pnpt5FQPwJAeTAAbV/lctPUfsGK1rirWIWxm89/ysajYSRwuI1SAGkqy5UL8/epad0ZwI0KiHY7e2Hth7CuEElnZXjWzGOgkQJBAK09KsTxSFO6YH9C7vFi7skj8kY9kDHGUDQZ/JIsHzMT128BTbvKDlIvP6WVMi+H86ibdG9z4OiuQlPnIGsf+CcCQGm7E8gzp/KCtDMsa797yapJOfCKlE3B9LKnu04li2fDAvS20ULVk+vZHHUhlCuav4cL+sJKAWQNZ5iuLh+6Xbg=";
JsonObject = {
    "isAllCity":"0",
    "cdbh":"cd20180119-0028223" ,
    "name":"陈青青",
    "zjh":"33050119890104880X",
    "xzqbm":"330501",
    "isShowXzxx":"1",
    "sm":"查询范围:{0}.",
    "cxfw":"湖州市区",
    "cdyt":"无房证明",
    "jgmc":"政法委",
    "bjsy":"湖州不动产权属查询",
    "cxbt":"湖州市不动产登记信息查询记录",
    "qyca":"0"
}

obj = json.dumps(JsonObject)

#调用java的方法
print(pdf.GetEncrypResult(userId,privateKey,obj))
shutdownJVM()