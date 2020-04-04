from selenium import webdriver

browser = webdriver.Chrome()
 
#当查找节点而节点并没有立即出现时，隐式等待将等待一段时间再去查找DOM,默认的时间是0 
browser.implicitly_wait(10)
browser.get("http://www.zhihu.com/explore")
input = browser.find_element_by_id('Popover1-toggle1')
print(input)