# _*_ coding : utf-8 _*_
# @Time: 2022/12/7 10:22 PM
# @Author : 张安然
# @File : '008_变量定义
# @Project : python_space

weather = '今天天气很好,天晴了!'
print(weather)

'''
变量类型:
    Number 
        int
        long(长整型,也可以代表8进制和16进制),python2中使用,python3中不使用
        float(浮点数)
        complex(复数)
    bool 
        True
        False
    String (字符串)
    List (列表)
    Tuple (元组)
    Dictionary(字典)
'''

# 数据有类型,变量没有类型.通过type(变量名)查看数据类型
# 一般不需要声明变量的数据类型
# int float
count: int = 10
price: float = 12.12
print(count)
print(price)

# boolean
visible: bool = False
print(visible)

# String
message = '成功!'
print(message)
lesson: str = "小白基础速'Python'通过!"
print(lesson)
# 查看变量的数据类型
print(type(lesson))

# list
menus = ['文件', '编辑', '视图', '导航', count]
print(menus)

# 元组
ages = (10, 11, 12, 23)
print(ages)
print(type(ages))

# 字典
person = {
    'name': 'zar',
    'age': ages[0]
}
print(person)
print(type(person))

# 类型转换
p = int(price)
print(p)
f = float(count)
print(f)
s = str(price)
print(s)
b = bool(count)
print(b)
print(float('3.1415'))
print(str(True))
print(bool(-1))  # Ture ,非0都为True
print(bool(0))  # False

# 元组转str
print(str(ages))
#  list转str
print(str(menus))
#  字典t转str
print(str(person))
# 元组转list
print(list(ages))
# list转元组
print(tuple(menus))

# 字符串拼接
# 使用+
print(str(price) + ' : ' + str(count))
