# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 4:40 PM
# @Author : 张安然
# @File : 026_html解析_站长之家_图片下载
# @Project : python_space

import urllib.request
import urllib.parse
from lxml import etree

keyword = ''


def create_request(page):
    search = {
        # 'keyword': '校园',
        'keyword': keyword,
        'page': page
    }
    if page == 1:
        search = {
            'keyword': keyword,
            # 'keyword': '校园',
        }
    print(page)
    url = 'https://sc.chinaz.com/tupian/?' + urllib.parse.urlencode(search)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 '
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def get_images_url(html_content):
    tree = etree.HTML(html_content)
    for i in range(1, 20):
        image_node = '/html/body/div[3]/div[3]/div[' + str(i) + ']/img/@data-original'
        alt_node = '/html/body/div[3]/div[3]/div[' + str(i) + ']/img/@alt'
        image_value = tree.xpath(image_node)
        image_name = tree.xpath(alt_node)
        file_name = image_name[0]
        file_url = 'https:' + image_value[0].replace('scpic1', 'scpic').replace('Files', 'files').replace('_s', '')
        down_load(file_url, file_name)


def down_load(url, filename):
    print("file_name: " + filename)
    print("file_url:" + url)
    file_path = './images/' + filename + '.jpg'
    urllib.request.urlretrieve(url=url, filename=file_path)


if __name__ == '__main__':
    keyword = input('请输入图片分类,如:风景图片,动物图片,美食图片,人物图片')
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入终止页码'))
    for index in range(start_page, end_page + 1):
        content = create_request(index)
        get_images_url(content)
