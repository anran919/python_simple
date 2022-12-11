# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 5:02 PM
# @Author : 张安然
# @File : '034_selenium_交互.py
# @Project : python_space

from selenium import webdriver
import time

keyword = input('输入搜索内容')

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')

# 休眠3秒
time.sleep(3)

# 获取文本输入框对象
n_input = browser.find_element_by_id('kw')

# 在文本框中输入内容

n_input.send_keys(keyword)

time.sleep(3)

# 获取搜索按钮
n_search = browser.find_element_by_id('su')

# 点击按钮
n_search.click()

time.sleep(3)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)

time.sleep(3)

# 点击下一页
next_button = browser.find_element_by_class_name('n')
next_button.click()

time.sleep(3)
browser.execute_script(js_bottom)

time.sleep(3)

# 返回上一页
browser.back()

time.sleep(2)

browser.execute_script(js_bottom)

time.sleep(2)
# 再回去
browser.forward()
time.sleep(2)
browser.execute_script(js_bottom)

# 退出
browser.quit()
