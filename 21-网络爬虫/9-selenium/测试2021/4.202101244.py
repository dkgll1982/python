from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

USERNAME = 'dkgll' # 输入账号
PASSWORD = 'guo0z6i0h7a1n6' # 输入密码

# 随机时间，防止过快被检测
seconds = random.randint(2, 5)

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('https://www.baidu.com')

# 打开登录界面
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u1 > a.lb'))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_10__footerULoginBtn'))).click()
time.sleep(seconds)
# 输入账号密码
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_10__userName'))).send_keys(USERNAME)
time.sleep(seconds)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_10__password'))).send_keys(PASSWORD)
time.sleep(seconds)
# 勾选下次自动登录
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_10__memberPassLabel'))).click()
time.sleep(seconds)
# 点击登录按钮
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_10__submit'))).click()