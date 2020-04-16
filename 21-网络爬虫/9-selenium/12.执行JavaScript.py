from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")

#获取元素属性 get_attribute('class')
logo = browser.find_elements_by_css_selector("link[rel='shortcut icon']")
print(logo)
print(logo[0].get_attribute('href'))
print('*'*40)

js = "document.getElementById('Popover1-toggle').value= 'js渲染'"
browser.execute_script(js)
 
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

#滚动到底部
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('window.alert("dkgll：到底部了")')