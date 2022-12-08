# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 10:28 AM
# @Author : 张安然
# @File : '006_常用函数
# @Project : python_space


# 字符串高级

# len 获取长度
print(len('123'))
# find 查找
print('abc'.find('a'))
# startsWith, endsWith 判断
print('abc'.startswith('a'))
# count 计算出现次数
print('计算出现次数', 'abc'.count('a'))
# replace 替换内容
print('替换内容', 'abc'.replace('a', 'b'))
# split 通过参数和内容切割字符串
print('切割字符串', 'a,b,c'.split(','))
# upper,lower  大小写转换
print('大小写转换', 'abc'.upper())
# strip 去空格
print('去空格', 'a bc '.strip())
# join 字符串拼接
print('字符串拼接', 'abc'.join('efg'))

# 列表高级
values = ['大会员', '消息', '动态', '收藏', '历史']
print(values)
# 添加元素
values.append('创作中心')
values.insert(0, '首页')
values.extend(['番剧', '直播'])
print(values)

# 修改
values[0] = 'bilibili'
print(values)

# 查找元素
print('查找元素 in', '创作中心' in values)
print('查找元素 not in', '创作中心' not in values)

# 删除元素
#  del ,remove ,pop
values.remove('直播')
print('删除元素 remove', values)
del values[0]
print('删除元素 del', values)
values.pop()
print('删除元素 pop', values)

# 元组
# 元祖元素不可以修改
# 当元组中只有一个元素,需要在元素后面加上一个逗号:tuple_a = (1,)

