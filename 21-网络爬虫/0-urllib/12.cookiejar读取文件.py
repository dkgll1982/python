from urllib import request
import http.cookiejar as cookielib

# 保存cookie的本地磁盘文件名
filename = r'backup\爬虫\cookie.txt'

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = cookielib.MozillaCookieJar(filename)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = request.build_opener(handler)

# 创建一个请求
response = opener.open("http://www.baidu.com")

# 保存cookie到本地文件
cookiejar.save() 