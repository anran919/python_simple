# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 2:57 PM
# @Author : 张安然
# @File : '024_html解析
# @Project : python_space

"""
常用解析插件
xpath  安装chrome插件,重新打开浏览器,按下快捷键command + shift+ x
JsonPath
BeautifulSoup
"""

from lxml import etree

# xpath解析本地文件,使用etree.parse()
# 解析服务器响应的文件(使用多),使用etree.HTML()

# 1. 本地解析
tree = etree.parse('html/index.html')  # 每个标签必须有结束标签
# 1.1 路径查询
li_list = tree.xpath('//ul/li')
print(len(li_list))

# 1.2 谓词查询
# 通过id过滤
# list = tree.xpath('//ul[@id]/li')
# list = tree.xpath('//ul[@id]')
# 获取标签里的内容
# list = tree.xpath('//ul[@id]/li/text()')
# 标签属性值过滤
# list = tree.xpath('//ul[@id="t1"]/li/text()')

# 1.3属性查询
# 查询id为l11的li标签的class属性值
# n_class = tree.xpath('//ul[@id="t1"]/li[@id="l11"]/@class')

# 1.4模糊查询
# n_list = tree.xpath('//ul[contains(@id,"t")]')
# n_list = tree.xpath('//ul[starts-with(@id,"t")]')

# 1.5 内容查询
# n_list = tree.xpath('//ul/li/text()')


# 1.6 逻辑查询
n_list = tree.xpath('//ul/li[@id="l11" or @id="l21"]/text()')
print(n_list)

