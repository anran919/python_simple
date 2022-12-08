# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 7:38 PM
# @Author : 张安然
# @File : 'urllib_get请求
# @Project : python_space

import urllib.request
import urllib.parse

# url = 'https://www.baidu.com/s?wd=周杰伦'
#  参数处理,第一种方式,quote
url = 'https://cn.bing.com/search?q=' + urllib.parse.quote('周杰伦')
# print(url)
headers = {
    'User-Anent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

#  参数处理,第二中方式
search = {
    'q': '周杰伦',
    'v': 'song'
}

url = 'https://cn.bing.com/search?'+urllib.parse.urlencode(search)
print(url)
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


