# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy
from scrapy import signals
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse  
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException,TimeoutException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class JczlDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    
    #处理请求方法，获取spider里的webdriver对象，进行处理
    def process_request(self, request, spider):
        url = request.url   
        #  对页面响应体数据的篡改, 如果是每个模块的 url 请求, 则处理完数据并进行封装
        if url in ["http://huzhou-jczl-cx.spacecig.com/zhzl-frames/main.html"]:      
            browser = spider.chrome   
            browser.get(url)         
            
            time.sleep(1)
            
            #2021/01/29：这是加进去的代码,如果不加入这一句的话，没办法正常切换到内嵌框架
            #参考：https://blog.csdn.net/static_at/article/details/84636388
            browser.switch_to_default_content()             #切换到主页面
            
            wait = WebDriverWait(browser,20)
            iframes = browser.find_elements_by_tag_name("iframe")
            for iframe in iframes:
                #获取节点ID、位置、标签名和大小
                print('[id:',iframe.id,
                    ';location:',iframe.location,
                    ';tag_name:',iframe.tag_name,
                    ';size:',iframe.size,
                    ';outerHTML:',iframe.get_attribute('outerHTML'), 
                    ';text:',iframe.text,']'
                ) 
            #2021/01/28测试：调试时可以进入框架页面，运行时一直切换不了,问题待解决~    
            #2021/01/29测试：加入browser.switch_to_default_content() 这一句就可以正常切换框架了~~~
            browser.switch_to_frame(iframes[0]) 
            time.sleep(1)
            
            print('-'*40)
            input = browser.find_elements_by_xpath("//input")
            for index,item in enumerate(input,start=1): 
                attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
                print(f'input元素{index}——',attrs,' name:',item.get_attribute('name'),' size:',item.size,' class',item.get_attribute('class'),' id',item.get_attribute('id'))
                #输入内容如下：
                # {'autocomplete': 'off', 'name': 'userid', 'placeholder': '请输入用户名或手机号', 'type': 'text'}  name: userid  size: {'height': 20, 'width': 155}  class   id 
                # {'autocomplete': 'off', 'placeholder': '请输入密码', 'type': 'text'}  name:   size: {'height': 20, 'width': 155}  class   id 
                # {'autocomplete': 'off', 'name': 'phone', 'placeholder': '请输入手机号', 'type': 'text'}  name: phone  size: {'height': 0, 'width': 0}  class   id 
                # {'autocomplete': 'off', 'name': 'code', 'placeholder': '请输入验证码', 'style': 'border: none; width: 55%;', 'type': 'text'}  name: code  size: {'height': 0, 'width': 0}  class   id
                # {'autocomplete': 'off', 'class': 'form-control', 'placeholder': '请输入新密码', 'type': 'text'}  name:   size: {'height': 0, 'width': 0}  class form-control  id 
                # {'autocomplete': 'off', 'class': 'form-control', 'placeholder': '请再次输入新密码', 'type': 'text'}  name:   size: {'height': 0, 'width': 0}  class form-control  id 
            print('-'*40)
            
            try:   
                #用户名
                userid = wait.until(EC.element_to_be_clickable((By.NAME,'userid'))) 
                userid.send_keys("admin")
                #密码
                pwd = browser.find_element_by_xpath("//div[@class='textInput paw']/input")
                pwd.send_keys('DFYOPS1RrpdVlu2U')

                #登录按钮
                btnlogin = browser.find_element_by_class_name('login_btn')
                btnlogin.click()
            finally:
                time.sleep(3)   #强制等待3秒    
                print('title:',browser.title,";url:",browser.current_url)  
            
            html = browser.page_source
            #返回响应给spider    
            return HtmlResponse(url = url,body = html,request = request,encoding = 'utf-8')
        else:
            #普通请求走process_response返回response
            return None


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
