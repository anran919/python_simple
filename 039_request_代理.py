# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 8:23 PM
# @Author : 张安然
# @File : '037_request_get请求示例
# @Project : python_space
import random

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

proxies_list = [
    {'http': '120.220.220.95:8085'},
    {'http': '47.105.91.226:8118'},
    {'http': '58.220.95.44:10174'},
    {'http': '180.97.87.63:80'},
]

proxies = random.choice(proxies_list)
print('proxies', proxies)
response = requests.post(url, data, headers=headers, proxies=proxies)
response.encoding = 'utf-8'
# 两种方式
print(response.json())
# print(response.text)
