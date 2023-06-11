from selenium.webdriver.common.by import By
from lib.yc_sleep import ycsleep


def manualy_login(wd):
    url = "https://weibo.com/"
    wd.get(url=url)

    # 现主页实现登录,用二维码扫就行
    # 20230611: old
    # wd.find_element(By.XPATH, '//*[@id="__sidebar"]/div/div[1]/div[1]/div/button').click()
    # 20230611: new
    wd.find_element(By.CSS_SELECTOR, ".LoginCard_btn_Jp_u1").click()
    ycsleep(20)