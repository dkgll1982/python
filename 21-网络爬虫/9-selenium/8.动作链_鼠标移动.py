#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys,os  

path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"text3.html") 
driver = webdriver.Chrome()
driver.get(path)
driver.maximize_window()
#第一个操作:鼠标移动到某个元素
#为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
MoveElement = driver.find_element_by_xpath('//*[@id="box1"]')   #鼠标移到到目标元素
time.sleep(3)
'''将鼠标移到MoveElement'''
Action = ActionChains(driver)

Action.move_to_element(MoveElement).perform()
time.sleep(5)
driver.save_screenshot(r'images\move_to_element.png')   #记录一下我们开始的坐标位置
'''x坐标为正数向右偏移，x坐标为负数向左偏移'''
'''y坐标为正数向下偏移，y坐标为负数向上偏移'''
#为了更好的显示我们效果，当鼠标移动到目标位置的时候，我们显示了鼠标的坐标，以后让当前的位置变成绿色
Action.move_by_offset(-311,-11).perform() #move_by_offset以鼠标当前的位置为中心进行偏移，移动到距离当前位置(x,y)
time.sleep(5)
driver.save_screenshot(r'images\move_by_offset.png')   #记录一下我们移动后的坐标位置
driver.quit()