# 用id查询元素
def byId(wd, str):
    return wd.find_element_by_id(str)

# 用name查询元素
def byName(wd, str):
    return wd.find_element_by_name(str)

# 用xpath查询元素
def byXpath(wd, str):
    return wd.find_element_by_xpath(str)

# 用linktxt定位
def byLink(wd, str):
    return wd.find_element_by_partial_link_text(str)

# 用classname定位
def byClassName(wd, str):
    return wd.find_element_by_class_name(str)

# 用css定位
def byCss(wd, str):
    return wd.find_element_by_css_selector(str)
