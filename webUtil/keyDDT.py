from 自动化框架.webUtil.findElement import *
from 自动化框架.webUtil.elementAction import *

# 关键词驱动
class keyDDT:

    # 初始化wd
    def __init__(self, wd):
        self.wd = wd

    # 初始化传入关键词
    def keyDDT(self, key):
        # 分割关键词
        li = key.split(';')
        # 查询元素
        ele = self.selectEle(li[0], li[1])
        # 元素执行操作
        self.eleDo(ele, li[2], li[3])

    # 查询元素
    def selectEle(self, how, what):
        if how == 'name':
            return byName(self.wd, what)
        elif how == 'xpath':
            return byXpath(self.wd, what)
        elif how == 'link':
            return byLink(self.wd, what)
        elif how == 'class':
            return byClassName(self.wd, what)
        elif how == 'css':
            return byCss(self.wd, what)

    # 元素执行操作
    def eleDo(self, ele, how, what=''):
        if how == 'click':
            doClick(ele)
        elif how == 'input':
            sendStr(ele, what)
        elif how == 'mouseClick':
            doMouseClick(self.wd, ele)
        elif how == 'submit':
            doSubmit(ele)