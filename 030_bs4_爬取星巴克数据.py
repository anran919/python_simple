# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 11:12 PM
# @Author : 张安然
# @File : '030_bs4_爬取星巴克数据
# @Project : python_space
import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.starbucks.com.cn/menu/'
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    strong_list = soup.select('.product li strong')
    for value in strong_list:
        print(value.get_text())
