from urllib import request
import http.cookiejar as cookielib
import urllib

# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(cookie_handler)

# 自定义opener的addheadders的参数，可以赋值HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# 需要登录的账户和密码
data = {"email":"dkgll@qq.com", "password":"3221160"}

# 通过urlencode()转码
postdata = urllib.parse.urlencode(data).encode('utf8')

# 构建Request请求对象，包含需要发送的用户名和密码
request = request.Request("http://www.renren.com/PLogin.do", data = postdata)

# 通过opener发送这个请求，并获取登录后的Cookie值，
opener.open(request)

# opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")

# 打印响应内容
# 7. 打印响应内容
with open(r'backup\爬虫\cookie登录.html','w',encoding='utf8') as f:
    f.write(response.read().decode('utf-8')) 