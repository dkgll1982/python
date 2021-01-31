# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.http import HtmlResponse 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException,TimeoutException  
import time

class MyDownloadMiddleware():   
    #处理请求方法，获取spider里的webdriver对象，进行处理
    def process_request(self, request, spider):
        url = request.url
        browser = spider.chrome 
        browser.get(url)      
          
        # 显示等待:WebDriverWait()
        # WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
        # driver：浏览器驱动
        # timeout：最长超时时间，默认以秒为单位
        # poll_frequency：检测的间隔步长，默认为0.5s
        # ignored_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。 
        wait = WebDriverWait(browser,3)  
        
        # 调用该方法提供的驱动程序作为参数，直到返回值为True
        wait_until = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'm-b-sm'))) 
        # 在设置时间（3s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。
        # 再等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.
        
        html = browser.page_source
        #返回响应给spider    
        return HtmlResponse(url = url,body = html,request = request,encoding = 'utf-8')

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

