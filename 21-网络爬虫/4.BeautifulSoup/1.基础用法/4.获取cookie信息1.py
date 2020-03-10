import urllib.error, urllib.request, urllib.parse
import http.cookiejar

LOGIN_URL = 'http://jczl.giscloud.cx/iam/login.html?ReturnUrl=%2Fzhzl-frames%2Fmain2.html'
#get_url为使用cookie所登陆的网址，该网址必须先登录才可
get_url = 'http://jczl.giscloud.cx/zhzl-frames/main2.html'
values = {'passport':'a26509d7-8b85-4b11-bcc5-13bb3d2c88a7',
          'CIGUserid':'ADMIN',
          'CIGToken':'2b76befa-a64c-4e1d-80d3-04fefcf87cee', 
          'CIGUsername':'%E9%95%BF%E5%85%B4%E5%B9%BF%E7%94%B5',
          'true':'OefDSgtnPQ1mQBulAAEj'
         }
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
headers = {'User-Agent':user_agent, 'Connection':'keep-alive','Location':'/zhzl-frames/main2.html'}
#将cookie保存在本地，并命名为cookie.txt
cookie_filename = r'backup/cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
try:
    response = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

for item in cookie_aff:
    print('Name ='+ item.name)
    print('Value ='+ item.value)
#使用cookie登陆get_url
get_request = urllib.request.Request(get_url,headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode('utf8'))