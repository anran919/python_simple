# _*_ coding : utf-8 _*_
# @Time: 2022/12/9 8:53 PM
# @Author : 张安然
# @File : '027_jsonpath_解析json
# @Project : python_space

import jsonpath
import json

# 获取豆瓣电影所有的演员
obj = json.load(open('豆瓣电影.json', 'r', encoding='utf-8'))
# actors = jsonpath.jsonpath(obj, '$[*].actors')
actors = jsonpath.jsonpath(obj, '$..actors')
# print(actors[0])
# 获取最后一部电影的分类
# last_type = jsonpath.jsonpath(obj, '$.[(@.length-1)].types')
# print(last_type)
# 获取前两本电影的演员
# first_authors = jsonpath.jsonpath(obj, '$..actors[:2]')
# print(first_authors)

