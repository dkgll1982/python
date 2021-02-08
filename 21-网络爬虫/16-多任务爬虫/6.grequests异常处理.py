import grequests

def err_handler(request, exception):
    print("请求出错")

req_list = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),     #  超时异常
    grequests.get('http://fakedomain/'),                            #  该域名不存在
    grequests.get('http://httpbin.org/status/500')                  #  正常返回500的请求
]

#grequests.map()方法还支持自定义异常处理函数
res_list = grequests.map(req_list, exception_handler=err_handler)
print(res_list)