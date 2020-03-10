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
        self.member_url = 'https://www.yaozh.com/member'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
            'Cookie': 'acw_tc=707c9f9615823659036492531e31695b4b026b1dd03e3a688c586dd0f06ce1; _ga=GA1.1.1234601909.1582366105; UtzD_f52b_ulastactivity=1582366088%7C0; PHPSESSID=m657vc0cmth0fv18st703809i4; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1583806533; _gid=GA1.2.1224974903.1583806534; _gat=1; yaozh_userId=882093; UtzD_f52b_saltkey=wehT89v6; UtzD_f52b_lastvisit=1583802958; yaozh_uidhas=1; yaozh_mylogin=1583806560; acw_tc=707c9f9615823659036492531e31695b4b026b1dd03e3a688c586dd0f06ce1; _ga=GA1.1.1234601909.1582366105; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1582365909%2C1583806533; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D751963; UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _gid=GA1.1.189842148.1583806783; UtzD_f52b_lastact=1583815036%09uc.php%09; _gat=1',
            'Referer': 'https://www.yaozh.com/login/proxy', 
        }
        self.member_header = { 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
        self.cookie = CookieJar()
        self.cookiehandle = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookiehandle)
        self.form_data = urllib.parse.urlencode({
            "username": "suixin8205",
            "pwd": "qwer123",
            "formhash": "FC09490E33",
            "backurl": "%2F%2Fwww.yaozh.com",
        }).encode("utf8")
        
    def send_request(self):
        request = urllib.request.Request(self.login_url,data = self.form_data,headers=self.headers)
        response = self.opener.open(request)
        
        if response.status == 200:
            # 可以按标准格式将保存的Cookie打印出来
            cookieStr = ""
            for item in self.cookie:
                cookieStr = cookieStr + item.name + "=" + item.value + ";"
            print('获取cookie成功:{}'.format(cookieStr))
            request =urllib.request.Request(self.member_url,headers=self.member_header)
            response = self.opener.open(request)
            if response.status == 200:
                print('获取会员页成功！')
                self.write_content(response)

    def write_content(self,response):
        with open(r'backup\\爬虫\yaozhi.html','w',encoding='utf8') as f:
            f.write(response.read().decode('utf8'))

    def start(self):
        self.send_request()


if __name__ == '__main__':
    yzs = YaoZhiSpider()
    yzs.start()
