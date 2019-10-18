#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-17 19:58:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-17 19:58:15 
# @Software: vscode 

#服务配置类
class server():
    
    #url
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self,value):
        self._url=value

    #用戶名
    @property
    def userid(self):
        return self._userid
    @userid.setter
    def userid(self,value):
        self._userid=value

    #密碼
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter
    def pwd(self,value):
        self._pwd=value

    #ip
    @property
    def ip(self):
        return self._ip
    @ip.setter
    def ip(self,value):
        self._ip=value

    #端口
    @property
    def port(self):
        return self._port
    @port.setter
    def port(self,value):
        self._port=value

    #数据库SID
    @property
    def sid(self):
        return self._sid
    @sid.setter
    def sid(self,value):
        self._sid=value