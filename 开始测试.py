import unittest
from 自动化框架 import HTMLTestRunner
from 自动化框架.testCase.test0907 import baidu_main_page


if __name__ == '__main__':
    suite1 = unittest.makeSuite(baidu_main_page)
    # unittest.TextTestRunner().run(suite1)
    with open('./report/测试结果.html', 'wb') as f:
        r = HTMLTestRunner.HTMLTestRunner(stream=f,
                                              title='测试',
                                              description='详细结果')
        r.run(suite1)