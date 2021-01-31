from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")

#获取元素属性 get_attribute('class')
logo = browser.find_elements_by_css_selector("link[rel='shortcut icon']")
print(logo)
print(logo[0].get_attribute('href'))
print('*'*40)

#获取节点文本
tag = browser.find_element_by_class_name('ExploreHomePage-ContentSection')
print('text:',tag.text)                             # 获取节点的文本内容

#获取节点ID、位置、标签名和大小
print('id:',tag.id)                                 # 获取节点的ID
print('location:',tag.location)                     # 获取节点的位置
print('tag_name:',tag.tag_name)                     # 获取节点的标签名
print('size:',tag.size)                             # 获取节点的大小
print('class',tag.get_attribute('class'))           # 获取节点的class属性
print('id',tag.get_attribute('id'))
print('outerHTML:',tag.get_attribute('outerHTML'))  # 获取某个元素的html
#Selenium Webdriver：如何找到元素的所有属性:https://www.it1352.com/1877776.html 
attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', tag)
