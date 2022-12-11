# _*_ coding : utf-8 _*_
# @Time: 2022/12/10 9:45 PM
# @Author : 张安然
# @File : '040_古诗文网,验证码登录
# @Project : python_space


import requests
from bs4 import BeautifulSoup

login_html_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url=login_html_url, headers=headers)
content = response.text
soup = BeautifulSoup(content, 'lxml')
# 获取隐藏域
VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
VIEWS_TATE_GENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print('VIEWSTATE: ', VIEWSTATE)
print('VIEWS_TATE_GENERATOR: ', VIEWS_TATE_GENERATOR)

# 获取验证码
# 获取验证码图片
image_code_src = soup.select('#imgCode')[0].attrs.get('src')
image_code_src = 'https://so.gushiwen.cn/RandCode.ashx' + image_code_src
print('image_code_src', 'https://so.gushiwen.cn/RandCode.ashx' + image_code_src)
# 下载验证码图片 这种方式不行,有bug.需要使用session
# urllib.request.urlretrieve(image_code_src, './images/古诗文网验证码图片.jpg')
# verification_code = input('请输入验证码')

# 使用session
session = requests.session()
# 获取验证码url的内容
response_code = session.get(image_code_src)
content_code = response_code.content
with open('./images/古诗文网验证码图片.jpg', 'wb') as fp:
    fp.write(content_code)

# 开始登录
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
verification_code = input('请输入验证码')
data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWS_TATE_GENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'anran0919@163.com',
    'pwd': 'ef123456',
    'code': verification_code,
    'denglu': '登录'
}
response = session.post(url=login_url, headers=headers, data=data)
with open('./html/古诗文网登录.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
