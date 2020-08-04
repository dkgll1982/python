# 模拟登录古诗文网
import requests
from lxml import etree
from fake_useragent import UserAgent as ua
from ydmhttp import YDMHttp  # 导入上面整理好的云打码接口

# 古诗文网址
url = 'https://so.gushiwen.org'

# 登录页面路径
login_page_url = '/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

# 登录请求的url
login_request_url = '/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'

# 请求头
headers = {    
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'       
}

# 准备一个session对象
session = requests.Session()

# 获取登录页面内容
page_text = session.get(url + login_page_url, headers=headers).text

# 获取保存图片验证码
tree = etree.HTML(page_text)
code_img_url = url + tree.xpath('//*[@id="imgCode"]/@src')[0]
print('---->',code_img_url)
img_data = session.get(code_img_url, headers=headers).content
filename = r'backup\爬虫\验证码\code_img.jpg'
with open(filename, 'wb') as fp:
    fp.write(img_data)
      
# 使用云打码识别图片验证码
ydm = YDMHttp(filename = filename, codetype = 1004, timeout = 10)
cid, code_text = ydm.decode()
# 以 f开头表示在字符串内支持大括号内的python 表达式
print(f'验证码识别结果：{code_text}') 

# # 登录请求的参数
# # 下面两个参数会变化，所以我们就动态获取：
# __VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
# __VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
# data = {
#     '__VIEWSTATE': __VIEWSTATE,
#     '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
#     'from': 'http://so.gushiwen.org/user/collect.aspx',
#     'email': 'www.zhangbowudi@qq.com',
#     'pwd': 'bobo328410948',  # 你没看错，它就是明文
#     'code': code_text,
#     'denglu': '登录',
# }

# # 开始模拟登录：
# page_text = session.post(url + login_request_url,headers=headers, data=data).text

# with open(r'backup\爬虫\gushiwen.html', 'w', encoding='utf-8') as fp:
#     fp.write(page_text)
