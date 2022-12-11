# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 8:08 PM
# @Author : 张安然
# @File : '036_requests_基本使用
# @Project : python_space

import requests

response = requests.get('http://www.baidu.com')
# 设置响应的编码格式
response.encoding = 'utf-8'
# "_content",
# "status_code",
# "headers",
# "url",
# "history",
# "encoding",
# "reason",
# "cookies",
# "elapsed",
# "request",
print('text', response.text)  # 网页源码
print('headers', response.headers)  # 网页headers
print('encoding', response.encoding)  # 网页编码
print('url', response.url)  # url
print('cookies', response.cookies)  # cookies
print('history', response.history)  # history
print('status_code', response.status_code)  # cookies
