# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 11:53 AM
# @Author : 张安然
# @File : '008_字典
# @Project : python_space

# 增,删,改,查

dog = {
    'name': 'timi',
    'age': 19,
    'color': 'yellow',
}
print(dog)
# 查
print(dog['name'])
print(dog.get('name'))

# 改
dog['name'] = 'jerry'
print('改:', dog)

# 删
# 删除某个元素
del dog['age']
print('删除一个:', dog)
# 清空字典
dog.clear()
print('清空字典:', dog)
# 删除字典
# del dog

# 增
dog['sex'] = 1
print('增:', dog)

