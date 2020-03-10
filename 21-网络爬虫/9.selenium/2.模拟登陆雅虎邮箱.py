# coding = utf-8
# 参考链接：https://www.cnblogs.com/573734817pc/p/11176815.html

#模拟浏览器自动登录yahoo邮箱
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

#一下三行为无头模式运行，无头模式不开启浏览器，也就是在程序里面运行的
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=(r'C:\Users\dkgll\AppData\Local\Google\Chrome\Application\chromedriver.exe'), options=chrome_options)
# #如果不用上面三行，那么就用下面这一行。运行的时候回自动的开启浏览器，并在浏览器中自动运行，你可以看到自动运行的过程
# browser = webdriver.Chrome(executable_path=(r'C:\Users\0923\AppData\Local\Google\Chrome\Application\chromedriver.exe'))
#设置访问链接
browser.get("https://www.yahoo.com")
#点击登录按钮
browser.find_element_by_id("uh-signin").click()
#输入用户名
browser.find_element_by_id("login-username").send_keys("bjs***99")
#点击“下一步”
browser.find_element_by_id("login-signin").click()
#等待10秒，以防读取不到（#login-passwd）元素
sleep(10)
#输入密码
browser.find_element_by_id("login-passwd").send_keys("Zf***234")
#点击signin按钮
browser.find_element_by_id("login-signin").click()
#获取cookie
cookie_items = browser.get_cookies()
cookie_str = ""
#组装cookie字符串
for item_cookie in cookie_items:
    item_str = item_cookie["name"]+"="+item_cookie["value"]+"; "
    cookie_str += item_str
    print(item_cookie)
#打印出来看一下
print(cookie_str)
# sleep(5)
# browser.get_screenshot_as_file('test.png')
# browser.close()
# print('test!')