# coding:utf8
import requests
import gevent
from gevent import monkey 
import urllib
from urllib import request
import http.cookiejar as cookielib
import json
import time
monkey.patch_all()      # 用于将标准库中大部分阻塞式调用修改为协作式运行 

class JkmSpider():
    def __init__(self):
        super().__init__()
        host = 'http://jczl.giscloud.cx/'
        self.inter_url = host + "healthWeb/front/index/healthQuery"
        self.login_url = host + "iam/saml/login"
        self.userpwd = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}  
        self.per_data = {"sfzh":"340406198507213836","mzt":"绿码","mffd":"杭州市"}
        self.form_data = bytes(json.dumps(self.per_data), 'utf8')
        self.headers = self.get_cookieheader()
        
    def get_cookieheader(self):    
            # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
            cookie = cookielib.CookieJar()
            # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
            # 参数就是构建的CookieJar()对象
            cookie_handler = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(cookie_handler)
            # 自定义opener的addheadders的参数，可以赋值HTTP报头参数
            opener.addheaders = [("Content-type","application/json;charset=UTF-8"),("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36")]
    
            # 通过urlencode()转码
            postdata = urllib.parse.urlencode(self.userpwd).encode('utf8')
            # 构建Request请求对象，包含需要发送的用户名和密码
            req = request.Request(self.login_url, data = postdata)
            # 通过opener发送这个请求，并获取登录后的Cookie值，
            response = opener.open(req)  
            # 可以按标准格式将保存的Cookie打印出来
            cookieStr = ""
            for item in cookie:
                cookieStr = cookieStr + item.name + "=" + item.value + ";"

            # 舍去最后一位的分号(此处取到cookie值)
            cookieStr = cookieStr[:-1]   
            headers = {
                "Host":'jczl.giscloud.cx',
                "Content-type":"application/json;charset=UTF-8",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                "Cookie":cookieStr
            } 
            return headers
    
    #请求   
    def send_request(self):  
        try:
            response = requests.post(self.inter_url,data=self.form_data,headers=self.headers) 
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(e)

    def start(self):  
        max = 100
        workers = 20
        for i in range(1,max+1):
            g_list = list()
            for x in range(1,workers+1):
                g = gevent.spawn(self.send_request)
                g_list.append(g)
            gevent.joinall(g_list)
            for index,g in enumerate(g_list,start=1):
                print(f'第{i}次循环第{index}条={(i-1)*workers+index},结果:',g.value)
        
if __name__ == "__main__":
    jkms = JkmSpider()
    start = time.time()
    jkms.start()

    print('总耗时：', time.time()-start)