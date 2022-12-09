# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 4:40 PM
# @Author : 张安然
# @File : '025_html解析_baidu_百度一下四个文字
# @Project : python_space

import urllib.request
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    #   解析源码
    tree = etree.HTML(content)
    # 获取想要的数据
    # value =tree.xpath('//input[@id="su"]/@value')
    value =tree.xpath('//*[@id="su"]/@value')
    print(value)
