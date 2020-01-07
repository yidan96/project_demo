import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#driver.find_element_by_id("kw").send_keys("10086")

# driver.find_element(by=By.XPATH, value="//*[xxxx]").send_keys("10086")

# feature = By.ID, "kw"
# driver.find_element(*feature).send_keys("10086")


# WebDriverWait(driver, 15, 1).until(lambda x: x.find_element_by_id("kw")).send_keys("10086")


# 某个元素的特征，属于page
search_text_field = By.ID, "kw"


# 根据特征找元素，属于base
def find_element(feature):
    return WebDriverWait(driver, 20, 1).until(lambda x: x.find_element(*feature))


# 根据特征和内容输入，属于base
def input(feature, text):
    find_element(feature).send_keys(text)


# 根据页面的元素特征输入，属于page
def input_search(text):
    input(search_text_field, text)


# 调用搜索输入并传入数据，属于脚本
input_search("hello")

