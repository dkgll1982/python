from selenium import webdriver
from time import sleep
import pyperclip,pyautogui

driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()
driver.get('http://desk.zol.com.cn/showpic/1920x1200_777_13.html')

#鼠标移动到指定位置，右键点击
pyautogui.rightClick(x=1000, y=500)

#输入V
pyautogui.typewrite(['V'])

#将地址以及文件名复制
pic_dir = 'D:\\35.jpg'
pyperclip.copy(pic_dir)

#等待窗口打开，以免命令冲突，粘贴失败，试过很多次才有0.8，具体时间自己试
sleep(0.8)
#粘贴
pyautogui.hotkey('ctrlleft','V')
#这个也可以实现粘贴
# pyautogui.keyDown('ctrl')
# pyautogui.press('v')
# pyautogui.keyUp('ctrl')

#确认保存
pyautogui.press('enter')