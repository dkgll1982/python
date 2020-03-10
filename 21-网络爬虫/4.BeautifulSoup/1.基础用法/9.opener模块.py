from urllib import request
from io import BytesIO
import gzip

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = request.HTTPHandler()

# 构建一个HTTPSHandler 处理器对象，支持处理HTTPS请求
# http_handler = request.HTTPSHandler()

# 调用 request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = request.build_opener(http_handler)

# 构建 Request请求
request = request.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

# 获取服务器响应内容
htmls = response.read()
# 第一个print输出的字节码可以看到它是以"b’\x1f\x8b\x08"开头的
# 说明它是gzip压缩过的数据，这也是报错的原因，所以我们需要对我们接收的字节码进行一个解码操作
buff = BytesIO(htmls)
f = gzip.GzipFile(fileobj=buff)
htmls = f.read().decode('utf-8') 

# 打印字符串
print(htmls)