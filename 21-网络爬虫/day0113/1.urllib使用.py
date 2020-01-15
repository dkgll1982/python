import urllib.request
import urllib.response
import urllib.parse
import urllib.error

c = 'hello 中文网！！'
print(bytes(c, 'utf8'))
print(bytes(c, 'utf-8'))
print(bytes(c, encoding='utf-8'))
print(c.encode('utf-8'))

# 这个函数只能接收key-value pair格式的数据。即只针对dict的, 并且目前不提供urldecode方法
parse = bytes(urllib.parse.urlencode(
    {'name': '张三', "age": 12, 'card_num': "41108200001112"}), encoding='utf-8')
print(parse)
#运行之后我们看到可以正常的返回结果，接着我们将timeout时间设置为0.1
#运行程序会提示如下错误：socket.timeout: timed out
try:
    #res = urllib.request.urlopen('http://httpbin.org/post', data=parse, timeout=1)
    res = urllib.request.urlopen('http://www.baidu.com')
    #响应类型、状态码、响应头
    #通过response.status、response.getheaders().response.getheader("server")，获取状态码以及头部信息
    print("info:%s,code:%s;url:%s;status:%s;headers:%s;header['server']:%s"%(res.info(),#获取响应头
                                                      res.getcode(),    #获取状态码    
                                                      res.geturl(),     #获取url
                                                      res.status,       #获取状态码
                                                      res.getheaders(), #获取响应头
                                                      res.getheader("server")))
    #response.read()获得的是响应体的内容
    #print('response:',res.read().decode('utf-8'),sep='\n')
    with open(r'backup/baidu.html','wb') as f:
        f.write(res.read())
except urllib.error.URLError as e:
    print('TIME OUT:',e.reason)

