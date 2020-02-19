from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

proxy_list = [
    {"http" : "119.147.137.79:8008"},
    {"http": "221.5.54.6:808"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
httpproxy_handler = request.ProxyHandler(proxy)
nullproxy_handler = request.ProxyHandler({})

print(type(httpproxy_handler),type(nullproxy_handler))

proxySwitch = True #定义一个代理开关

# 通过 request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = request.build_opener(httpproxy_handler)
else:
    opener = request.build_opener(nullproxy_handler)

req = request.Request("http://www.baidu.com/",headers=headers)

# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(req)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# request.install_opener(opener)
# response = request.urlopen(req)

print(response.read().decode('utf-8'))

#————————————————
#版权声明：本文为CSDN博主「__静禅__」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/Ka_Ka314/article/details/80972732