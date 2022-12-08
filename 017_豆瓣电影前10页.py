# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 10:20 PM
# @Author : 张安然
# @File : '017_豆瓣电影前10页
# @Project : python_space


import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def create_request(start_page):
    data = {
        "type": '22',
        "interval_id": '100:90',
        "action": '',
        "start": (start_page - 1) * 20,
        "limit": '20'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data, headers)
    content = get_content(request)
    down_load(content, start_page)


def get_content(res):
    response = urllib.request.urlopen(res)
    return response.read().decode('utf-8')


def down_load(content, start_page):
    with open('豆瓣电影分页下载' + str(start_page) + '.json', 'w') as fp:
        fp.write(content)


if __name__ == '__main__':
    start = int(input('请输入起始页码'))
    end = int(input('请输入结束页码'))
    for page in range(start, end + 1):
        create_request(start)
