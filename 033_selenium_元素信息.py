# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 4:51 PM
# @Author : 张安然
# @File : '033_selenium_元素信息以及交互
# @Project : python_space
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
# 获取指定id的clas属性,获取标签名
kw = browser.find_element_by_id('kw')
print(kw.get_attribute('class'))
print(kw.tag_name)

# 获取指定id的内容
n_class = browser.find_element_by_class_name('undertips-link-text')
print(n_class.text)

