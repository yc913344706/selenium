from lib.login import CookieLogin
from this_info import BASE_DIR
from lib.yc_sleep import ycsleep
import os


def login(wd):
    url = "https://weibo.com/"
    wd.get(url=url)

    # cooikes = wd.get_cookies()
    # for cooike in cooikes:
    #     print(cooike)
    ycsleep(6, 'after enter login weibo')
    wd.delete_all_cookies()

    # 持久化登录，之后登录就不需要上面的扫二维码
    login = CookieLogin(os.path.join(BASE_DIR, "scripts", "cookie.json"))
    cookies = login.load_cookies()
    try:
        for cookie in cookies:
            cookie_dict = {
                'domain': '.weibo.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": '',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            print(cookie_dict)
            wd.add_cookie(cookie_dict)
    except Exception as e:
        print(e)

    ycsleep(5, 'after load cookie')

    wd.refresh()
