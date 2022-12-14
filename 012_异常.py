# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 4:03 PM
# @Author : 张安然
# @File : '012_异常
# @Project : python_space
try:
    r = open('data.txt', 'r')
    print(r.read())
    r.close()
except FileNotFoundError:
    print("文件不存在")

# 捕获所有异常
try:
    r = open('data.txt', 'r')
    10 / 0
except(FileNotFoundError, ZeroDivisionError) as e:  # 捕获多个异常
    print(e)
except Exception as e:  # 捕获所以异常
    print(e)
else:  # 没有异常
    print('没有异常')
finally:
    print('finally ,无论如何都要执行')  # 一定执行
