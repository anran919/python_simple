# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 4:06 PM
# @Author : 张安然
# @File : '032_selenium_元素定位
# @Project : python_space
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# source = driver.page_source
content = driver.find_element_by_id('form')  # 获取id ='form'
print(content)
input_ = driver.find_element_by_name('wd')  # 获取name ='wd'
print(input_)
n_list = driver.find_element_by_xpath('//*[@id="kw"]')  # 根据xpath获取对象
print(n_list)
n_form = driver.find_element_by_tag_name('form')  # 根据标签名获取元素
print(n_form)
s_list = driver.find_elements_by_css_selector('.s_ipt')  # 根据css选择器获取元素(使用bs4语法)
print('根据css选择器获取元素', s_list)
link_list = driver.find_elements_by_link_text('新闻')  # 根据link标签获取元素
print('根据link标签获取元素', link_list)
