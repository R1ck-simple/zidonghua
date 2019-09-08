from selenium.webdriver.common.action_chains import ActionChains

# 填入文本
def sendStr(ele, str):
    ele.send_keys(str)

# 点击
def doClick(ele):
    ele.click()

# 表单确认
def doSubmit(ele):
    ele.submit()
# # 填入文本
# def sendStr(ele, str):
#     ele.send_keys(str)
# 鼠标点击
def doMouseClick(wd, ele):
    ActionChains(wd).move_to_element(ele).click().perform()