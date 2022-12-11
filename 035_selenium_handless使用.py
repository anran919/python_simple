# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 5:59 PM
# @Author : 张安然
# @File : '035_selenium_handless使用
# @Project : python_space

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path ='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_options.binary_location = path
browser = webdriver.Chrome(options=chrome_options)


browser.get('https://www.baidu.com/')
browser.save_screenshot('百度.png')

