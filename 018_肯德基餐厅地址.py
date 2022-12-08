# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 11:18 PM
# @Author : 张安然
# @File : '018_肯德基餐厅地址
# @Project : python_space

import urllib.request
import urllib.parse

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def creat_request(page):
    data = {
        "cname": "武汉",
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    return urllib.request.Request(base_url, data, headers)


def get_response(req):
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')


def down_load(start, content):
    with open('KFC_地址' + str(start) + '.json', 'w', encoding='utf-7') as fp:
        fp.write(content)


if __name__ == '__main__':
    start = int(input('请输入起始页码'))
    end = int(input('请输入结束页码'))
    for index in range(start, end):
        request = creat_request(index)
        content = get_response(request)
        down_load(index, content)
