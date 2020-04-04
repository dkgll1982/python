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
print('text:',tag.text) 

#获取节点ID、位置、标签名和大小
print('id:',tag.id)
print('location:',tag.location)
print('tag_name:',tag.tag_name)
print('size:',tag.size)