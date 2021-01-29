import time
from pku_law_selenium.Base import Base
from pku_law_selenium.elements import *


class Init(Base):
    """
    初始化网页
    """
    def __init__(self, str_url):
        super().__init__()
        try:
            self.dr.get(str_url)
            # super().refresh()
            # time.sleep(2)
            print("进入", self.dr.title)
            if TimeoutError is True:
                super().refresh()
        except TimeoutError as e:
            print("超时了，{}".format(e))
            return False
        finally:
            self.dr.set_window_size(1024, 1024)  # 设置浏览器长宽
            # self.dr.set_page_load_timeout(5)

    @staticmethod
    def get_cookie(self):
        self.dr.refresh()
        c = self.dr.get_cookies()
        # print(c)
        cookies = {}
        # 获取cookie中的name和value,转化成requests可以使用的形式
        for cookie in c:
            cookies[cookie['name']] = cookie['value']
        return cookies
        # print(cookies)

    def copy_fulltext(self):
        # 点击复制按钮
        super().click(by='css_selector', element=copy_btn_css)

    def get_fulltext(self):
        # 获取复制文本的属性内容
        return super().get_elem_attr('xpath', copy_fulltext_xpath, 'data-clipboard-text')

