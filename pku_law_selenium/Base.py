from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from configs import s


class Base(object):
    """
    Base封装所有页面都公用的方法
    """
    def __init__(self):
        self.dr = s.driver
        # self.url = url

    def find(self, by, element):
        """
        等待元素，直到找到
        :param by: 'id','name','xpath','link_text','partial_link_text','tag_name','class_name','css_selector'
        :param element: UIElements
        # :param state: 'present','clickable','invisible','visible'
        :return:
        """
        try:
            ele_find = self.dr.ensure_element(by, element)
            return ele_find
        except NoSuchElementException as e:
            print("通过{}没能找到元素{} Error:{}".format(by, element, e))
            return False

    def click(self, by, element):
        """
        等待元素，直到找到，无视弹窗直接点击
        :param by:
        :param element:
        :return:
        """
        try:
            self.dr.execute_script('arguments[0].click()', self.find(by, element))
        except NoSuchElementException as e:
            print("没有找到元素{} Error:{}".format(element, e))
        except ElementNotInteractableException as ee:
            print("元素{}不可交互 Error:{}".format(element, ee))
        except TimeoutException as te:
            print("超时pass,", format(te))
            pass
        except Exception as eee:
            print("!!!异常:{}".format(eee))

    def get_elem_attr(self, by, elem, attr_tag):
        # 通过by方式获取elem元素下的attr_tag属性值
        a = self.find(by, elem)
        attr = a.get_attribute(attr_tag)
        # print(attr)
        return attr

    def refresh(self):
        self.dr.refresh()

    def close_browser(self):
        self.dr.close()
