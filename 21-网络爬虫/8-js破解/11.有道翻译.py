#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-15 23:07:20
# @Remark: 人生苦短，我用python！

import requests
import random
import time
import hashlib

class FanYiSpider():
    def __init__(self):
        super().__init__()
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "251",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "_ntes_nnid=ce0d48f3ed527a0c43afd6e4d8aae924,1567428879416; OUTFOX_SEARCH_USER_ID_NCOO=2083067221.0469992; OUTFOX_SEARCH_USER_ID=-881967154@10.108.160.12; _ga=GA1.2.53054865.1578466693; JSESSIONID=aaa0W2ACXN2vBcmIZ49fx; ___rl__test__cookies=1586963603309",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            "X-Requested-With": "XMLHttpRequest"
        }
        self.kw = input('请输入要翻译的词：')
        self.ts = self.get_ts()
        self.bv= self.get_bv()
        self.salt = self.get_salt()
        self.sign = self.get_sign()
        
    def send_request(self):
        data = {
            "i": self.kw,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": self.salt,
            "sign": self.sign,
            "ts": self.ts,
            "bv": self.bv,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION"
        }
        response = requests.post(url=self.url, data=data, headers=self.headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print('URL：{}，状态码：{}'.format(url, response.status_code))

    def get_salt(self):
        return self.ts + str(random.randint(0,10));
   
    def get_sign(self):     
        data = "fanyideskweb" + self.kw + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"      
        md5 = hashlib.md5()
        md5.update(data.encode())
        return md5.hexdigest() 

    def get_ts(self):
        return str(int(time.time()* 1000))

    def get_bv(self):
        appversion = ' 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        md5 = hashlib.md5()
        md5.update(appversion.encode())
        return md5.hexdigest() 
    
if __name__ == "__main__":
    fys = FanYiSpider()
    fys.send_request() 
    # print(time.time())
    # print(str(int(time.time() * 1000)))
