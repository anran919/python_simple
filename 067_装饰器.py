# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 11:08 PM
# @Author : 张安然
# @File : '067_装饰器
# @Project : python_space


# 装饰器,方法一

def sleep():
    import time
    import random
    print('睡眠开始')
    time.sleep(random.randint(1, 5))


#
def outer(fun):
    def inner():
        print('我准备睡觉了')
        fun()
        print('我睡醒了')

    return inner


out = outer(sleep)
out()


# 装饰器,方法二

def outer1(func):
    def inner():
        print('我要睡觉了----')
        func()
        print('我睡醒了-----')

    return inner


@outer1
def sleep1():
    import random
    import time
    print('睡眠中---')
    time.sleep(random.randint(1, 5))


sleep1()
