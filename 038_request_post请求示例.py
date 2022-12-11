# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 8:23 PM
# @Author : 张安然
# @File : '037_request_get请求示例
# @Project : python_space

import requests

url = 'https://dict.youdao.com/keyword/key'
data = {
    'text': '在线翻译',
    'lang': 'zh',
    'to': 'en'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.post(url, data, headers=headers)
response.encoding = 'utf-8'
# 两种方式
print(response.json())
# print(response.text)

