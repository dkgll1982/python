#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-02-22 18:14:49
# @Last Modified by: guojun
# @Last Modified time: 2020-02-22 18:14:49
# @Software: vscode

from urllib import request
from http.cookiejar import CookieJar
import urllib
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class YaoZhiSpider():
    def __init__(self):
        self.login_url = 'https://www.yaozh.com/login'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'                
        }
        self.cookie = CookieJar()
        self.cookiehandle = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookiehandle)
        self.form_data = urllib.parse.urlencode({
            "username": "suixin8205"
            "pwd": "qwer123111",
            "formhash": "3E3C3ADE9",
            "backurl": "https%3A%2F%2Fwww.yaozh.com%2F",
        }).decode("utf8")
        
    def send_request(self):
        request = urllib.request.Request(self.login_url,data = self.form_date)
        response = self.opener.open(request)
        print()

    def write_content(self):
        pass

    def start(self):
        pass


if __name__ == '__main__':
    yzs = YaoZhiSpider()
    yzs.start()
