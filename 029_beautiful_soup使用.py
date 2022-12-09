# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 10:28 PM
# @Author : 张安然
# @File : '029_beautiful_soup使用
# @Project : python_space
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./html/index.html', 'r', encoding='utf-8'), 'lxml')
# print(soup)
# 根据标签名字查找节点
# 查找第一个节点
# print(soup.ul.li)
# 获取标签属性和属性值
# print(soup.ul.attrs)

# bs4的一些函数
# find
# find_all
# select

# 1. find 返回第一个复合条件的数据
# print(soup.find('li'))
# find 增加条件
# print(soup.find('li', id="l21"))
# 关键之查询条件,加_
# print(soup.find('li', class_="tc1"))
# 2. find_all,返回所有a标签的列表
# print('find_all', soup.find_all('li'))
# find_all 获取多个标签使用['li','a']
# print(soup.find_all(['li', 'a']))
# find_all 查找前几个数据
# print('find_all 查找前几个数据', soup.find_all('li', limit=4))

#  3. select (常用)
#  返回所有的标签
# print('select', soup.select('li'))
#  查找类选择器
# print('查找类选择器', soup.select('.tc1'))
# 查找id选择器
# print('查找id选择器', soup.select('#l11'))
# 查找属性选择器,查找带有id属性的标签
# print('查找带有id属性的标签', soup.select('li[id]'))
# 查找指定属性的标签
# print('查找指定属性的标签', soup.select('li[id="l11"]'))
# 层级选择器
# 后代选择器
# print('后代选择器',soup.select('div li'))
# 字带选择器
# print('字带选择器',soup.select('div ul>a'))
# 找到所有的a和li标签
# print('找到所有的a和li标签', soup.select('a,li'))


# 节点信息.获取标签内容
# li_list = soup.select('li')
# 以下三种方法都可以,注意:如果标签对象中只有内容,以下三种方式都可以,如果标签中还有标签,需要使用get_text())
# print('获取标签内容:', li_list[0].string)
# print('获取标签内容:', li_list[0].getText())
# print('获取标签内容:', li_list[0].get_text())

# 节点属性/获取节点的属性, 三种方式,第三种不推荐
obj = soup.select('a')[0]
print('节点属性', obj.attrs['href'])
print('节点属性', obj.attrs.get('href'))
print('节点属性', obj.get('href'))
