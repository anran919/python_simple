# _*_ coding : utf-8 _*_
# @Time: 2022/12/7 11:47 PM
# @Author : 张安然
# @File : '004_格式化输出_输入
# @Project : python_space

# 格式化输出
# 方式1
print('我的名字叫：%s ,我的年龄是:%d' % ("张安然", 10))
# 类型格式化
print('类型是%s' % type(10))
# float 需要控制经度 $m.df ,m标示宽度 ,n标示小数位
print('我的名字是:%s, 我的工资是%.2f' % ('anakin', 1253.99))
print('我的名字是:%s, 我的工资是%9.2f' % ('anakin', 1253.99))
# 输入
name = input("请输入的你的名字")
age = int(input('请输入你的年龄'))
salary = 19.99
# 方式2
print(f"我的名字叫{name},我的年龄是{age}")

# 方式3 快速格式化字符串
print(f'我的名字是{name},我的工资是{salary},我的年龄是{age}', 'tom', 12.99, 19)
