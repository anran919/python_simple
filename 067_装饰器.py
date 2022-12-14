# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 11:08 PM
# @Author : 张安然
# @File : '067_装饰器
# @Project : python_space


def sleep():
    import time
    import random
    print('睡眠开始')
    time.sleep(random.randint(1, 5))


def outer(fun):
    def inner():
        print('我准备睡觉了')
        fun()
        print('我睡醒了')

    return inner


out = outer(sleep)
out()
