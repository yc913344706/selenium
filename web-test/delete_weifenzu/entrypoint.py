
from lib.yc_sleep import ycsleep
from login.auto_login import login
from login.manually_login import manualy_login
from lib.log import color_logger

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def pre_params():
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

    return options

from selenium import webdriver
from selenium.webdriver.common.by import By


def start_multi_manage(wd):
    ycsleep(1, 'start multi manage')
    wd.find_element(By.CSS_SELECTOR, ".FollowGroup_stbtn_3-kBd").click()


def start_multi_select(wd):

    for j in range(1, 10):

        ycsleep(0.2)
        mouse_click(wd, f".vue-recycle-scroller__item-view:nth-child({j}) .woo-checkbox-shadow")
        # wd.find_element(By.CSS_SELECTOR,
        #                          f".vue-recycle-scroller__item-view:nth-child({j}) .woo-checkbox-shadow").click()


def mouse_click(wd, css_name):
    # 定位目标元素
    element = wd.find_element(By.CSS_SELECTOR, css_name)
    # 执行 JavaScript 代码，将元素滚动到可见区域
    # wd.execute_script("arguments[0].scrollIntoView(false);", element)
    # 使用 ActionChains 执行点击操作
    ActionChains(wd).move_to_element(element).click().perform()


def start_multi_cancel(wd):
    color_logger.info("start multi cancel")
    mouse_click(wd, ".woo-button-s:nth-child(2)")


def button_delete(wd):
    e = wd.find_element(By.CSS_SELECTOR, ".woo-dialog-btn:nth-child(2)")

    # print(">>>>>>>>>>>>>> 定位到的元素")
    # print(e)
    # print(type(e))
    # print(e.id)
    # print(e.tag_name)
    # print(e.size)
    # print(e.rect)
    # print(e.text)

    e.click()
    # mouse_click(wd, ".woo-dialog-btn:nth-child(2)")


def js_delete(wd):
    js = 'document.querySelector(".woo-dialog-btn:nth-child(2)").click()'
    wd.execute_script(js)


def start_multi_cancel_confirm(wd):
    color_logger.info("start multi cancel confirm")
    ycsleep(2, '确认前等待')

    js_delete(wd)
    # button_delete(wd)

    ycsleep(3, '确认后等待')


def start(wd):
    login(wd)
    # manualy_login(wd)

    url = "https://weibo.com/u/page/follow/5975438546/followGroup?tabid=0"
    wd.get(url)

    for index in range(1, 150):
        ycsleep(3, sleep_info=f"delete index: {index}")
        start_multi_manage(wd)
        start_multi_select(wd)
        start_multi_cancel(wd)
        start_multi_cancel_confirm(wd)
        wd.refresh()

    ycsleep(60, 'after all over')

    wd.close()
    wd.quit()
