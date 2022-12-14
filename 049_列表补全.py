# _*_ coding : utf-8 _*_
# @Time: 2022/12/13 10:35 AM
# @Author : 张安然
# @File : '049_列表补全
# @Project : python_space

books = ['水浒传','红楼梦','三国演义','西游记']

# 增
books.insert(0,'金瓶梅')
books.append('资治通鉴')
books.extend(['孙子兵法','鬼谷子'])

# 删除
del books[1]
books.pop(1)
books.remove('三国演义') # 删除第一个符合条件的元素
# 清空
# books.clear()

# 统计某个元素在列表中的数量
count = books.count('鬼谷子')
print('统计某个元素在列表中的数量 :',count)

print(books)