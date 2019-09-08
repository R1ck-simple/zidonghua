import sys
import ddt
import unittest
from time import sleep
from selenium import webdriver
from 自动化框架.webElement.webElement import *
from 自动化框架.webUtil.keyDDT import keyDDT
from 自动化框架.getData.getData import getData

@ddt.ddt
class baidu_main_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wd = webdriver.Firefox(firefox_binary=r'C:\FengHShia-App\Firefox\firefox.exe',
                                   executable_path='./browserDriver/geckodriver.exe')
        cls.wd.get('https://www.baidu.com')
        # cls.wd.find_element_by_css_selector().submit()
        cls.keyDDT = keyDDT(cls.wd)

    @ddt.data(*getData('登录测试'))
    def test_login(self, data):
        # a = public_page_element()
        # b = login_frame_element()
        # self.keyDDT.keyDDT(a.login_ele + ';' + 'click;')
        # sleep(2)
        # self.keyDDT.keyDDT(b.user_login + ';' + 'mouseClick;')
        # self.keyDDT.keyDDT(b.userName + ';' + 'input;17313056105')
        # self.keyDDT.keyDDT(b.password + ';' + 'input;xuan89948632.')
        # self.keyDDT.keyDDT(b.login_bottom + ';' + 'submit;')
        for i in data:
            data_case = i.split('*')
            mod = sys.modules['自动化框架.webElement.webElement']
            p_cls = getattr(mod, data_case[0])
            ele = getattr(p_cls(), data_case[1])
            self.keyDDT.keyDDT(ele + ';' + data_case[2])
            sleep(1)
        sleep(5)
        self.wd.get('https://www.baidu.com')