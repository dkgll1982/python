#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://cn.bing.com/')
driver.maximize_window()
searchElement = driver.find_element_by_id('sb_form_q').send_keys('selenium')
searchButtonElement = driver.find_element_by_id('sb_form_go')
ActionChainsDriver = ActionChains(driver).click(searchButtonElement)
#此时不执行perform()，我们可以看到虽然使用click()点击了搜索按钮，但是确实没有执行点击搜索过程。 
#此时执行perform()，我们已经可以看到执行了点击搜索按钮，执行了搜索操作。
ActionChainsDriver.perform()   
time.sleep(5)
driver.quit()

# ActionChains 提供了以下方法
# click(on_element=None)  　　                              #单击鼠标左键
# click_and_hold(on_element=None) 　　                      #点击鼠标左键，按住不放
# context_click(on_element=None)                            #点击鼠标右键
# double_click(on_element=None)                             #双击鼠标左键
# drag_and_drop(source, target)                             #拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset)         #拖拽到某个坐标然后松开
# move_by_offset(xoffset, yoffset)                          #鼠标移动到距离当前位置（x,y）
# move_to_element(to_element)                               #鼠标移动到某个元素
# move_to_element_with_offset(to_element, xoffset, yoffset) #将鼠标移动到距某个元素多少距离的位置
# release(on_element=None)                                  #在某个元素位置松开鼠标左键
# perform()                                                 #执行链中的所有动作