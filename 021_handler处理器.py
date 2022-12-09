# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 11:03 AM
# @Author : 张安然
# @File : '021_handler处理器
# @Project : python_space
import urllib.request

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    #   获取handler对象
    handler = urllib.request.HTTPHandler()
    #   获取opener对象
    opener = urllib.request.build_opener(handler)
    #     调用open方法
    response = opener.open(request)
    content = response.read().decode('utf-8')
    print(content)
