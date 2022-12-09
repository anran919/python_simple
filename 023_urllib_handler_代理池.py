# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 2:37 PM
# @Author : 张安然
# @File : '023_urllib_handler_代理池
# @Project : python_space
import urllib.request
import random

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    # 代理池
    proxies_list = [
        {'http': '120.220.220.95:8085'},
        {'http': '47.105.91.226:8118'},
        {'http': '58.220.95.44:10174'},
        {'http': '180.97.87.63:80'},
    ]
    proxies = random.choice(proxies_list)
    print(proxies)
    request = urllib.request.Request(url=url, headers=headers)
    handler = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    with open('百度.html', 'w', encoding='utf-8') as fp:
        fp.write(content)
