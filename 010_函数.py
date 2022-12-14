# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 2:10 PM
# @Author : 张安然
# @File : '010_函数
# @Project : python_space


def f1():
    print("这是一个f1函数")


def f2(a, b):
    return a + b


f1()

print(f2(2, 4))


# 返回多个返回值, 返回的是一个元组.tuple
def f3(a, b):
    return a, b


# m, n = f3(1, 2)
# print(f'函数返回多个值 {m},{n}')

value = f3(1, 2)
print(f'函数返回多个值 {type(value)}')


# 默认参数,默认参数必须下载最后
def f4(name, age=18):
    print(F'名字{name},年龄{age}')


f4("tom")


# 不定长参数 :位置不定长  ,以元组形式接收
def f5(*args):
    print(f'不定长参数{args},类型{type(args)}')


f5('lks', 'Jack', 17)


# 不定长参数 :关键字不定长 ,以字典形式接收
def f6(**kwargs):
    print(f'关键字传递{kwargs},类型{type(kwargs)}')


f6(name='jack', salary=19.99, age=17)


# 函数作为参数传递

def f7(f):
    result = f(1, 2)
    print("sum:", result)


def f8(a, b):
    return a + b


f7(f8)

# 匿名函数
f7(lambda x, y: x + y)
f7(lambda x, y: x * y)
