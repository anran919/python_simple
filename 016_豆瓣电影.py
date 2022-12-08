# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 9:44 PM
# @Author : 张安然
# @File : '016_豆瓣电影
# @Project : python_space

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
data = {
    "type": '22',
    "interval_id": '100:90',
    "action": '',
    "start": '0',
    "limit": '20'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
# fp = open('豆瓣电影.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()

# 方式二
with open('豆瓣电影.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
