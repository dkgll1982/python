#参考链接：https://www.cnblogs.com/superhin/p/11583560.html

import grequests

request_list = [
    grequests.get('http://httpbin.org/get?a=1&b=2',timeout=0.01),
    grequests.get('http://www.sina.com.cn'),
    grequests.get('https://news.baidu.com'),
]

exception_url = []  # 异常url存储列表

# 异常捕获方法
def exception_handler(request, exception): 
    exception_url.append(exception_url)
    print(request.url,":",exception)
    
# 此处map的requests参数是装有实例化请求对象的列表,其返回值也是列表，
# size参数可以控制并发的数量, 不设置为最大并发数，并发数也不能太大，怕你的机器抗不下来，最大控制到1000吧
response_list = grequests.map(request_list,size=5, exception_handler=exception_handler) 
for response in response_list:
    if response:
        print(response.status_code,response.url)