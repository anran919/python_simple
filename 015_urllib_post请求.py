# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 8:27 PM
# @Author : 张安然
# @File : '015_urllib_post请求
# @Project : python_space
import urllib.request
import urllib.parse
import json
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
#     'Connection': 'keep-alive',
#     'Content-Length': 141,
#     'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryLwjH9rsAtBfum0SN',
#     'Cookie': 'STUDY_SESS="dvgFwfhnp59ZiIPFDL3DOxFf1Xe5yc1JF6O6DWbxGo0uS5bS6eUqM7wBGbzgb+qPtZgz2szD4vsBLt6SiL/1EPv5GVWv326h9xRqsOevsE9cotj0ffcGUayZJb4ziSs2p+LDVju9fPBgh6YliIofr+YJYGwXyUmwKVEHaEbEThInppr6KrivyjY6FmKs/Qou"; STUDY_INFO="anran0919@163.com|-1|1023431248|1668773799859"; DICT_SESS=v2|9RxjwAYk0cOYOfquRMOG0PLnHU56LqS0OfnHJF64qL0JyhfpBnfUA0YY6LPLnLzf0wS0LJykMUGRpyOMkm64zY0zAhfwK0fJy0; DICT_LOGIN=1||1668773799888; OUTFOX_SEARCH_USER_ID=1169377356@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=2023268033.1767347',
#     'Host': 'dict.youdao.com',
#     'Origin': 'https://fanyi.youdao.com',
#     'Referer': 'https://fanyi.youdao.com/',
#     'sec-ch-ua': ' "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': 'macOS',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
url = 'https://dict.youdao.com/keyword/key'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
data = {
    'text': '在线翻译',
    'lang': 'zh',
    'to': 'en'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
result = response.read().decode('utf-8')
print((json.loads(result)['data'])[0]['explain'])
