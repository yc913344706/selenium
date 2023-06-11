from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, BASE_DIR)

from lib.login import CookieLogin

prefs = {
    'profile.default_content_setting_values': {
        'notifications': 2  # 隐藏chromedriver的通知
    },
    'credentials_enable_service': False,  # 隐藏chromedriver自带的保存密码功能
    'profile.password_manager_enabled': False  # 隐藏chromedriver自带的保存密码功能
}

# 创建一个配置对象
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置为开发者模式,禁用chrome正受到自动化检测的显示
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug

wd = webdriver.Chrome(service=Service(r'D:\Study\chromedriver.exe'), options=options)

# 最大化窗口
wd.maximize_window()
wd.implicitly_wait(5)

url = "https://weibo.com/"
wd.get(url=url)

# 现主页实现登录,用二维码扫就行
# 20230611: old
# wd.find_element(By.XPATH, '//*[@id="__sidebar"]/div/div[1]/div[1]/div/button').click()
# 20230611: new
wd.find_element(By.CSS_SELECTOR, ".LoginCard_btn_Jp_u1").click()
sleep(20)

# 保存cookie到本地
cookies = wd.get_cookies()

cookie_fname = 'cookie.json'
login = CookieLogin(cookie_fname)

login.save_cookies(cookies)

wd.close()
wd.quit()