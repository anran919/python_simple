# _*_ coding : utf-8 _*_
# @Time: 2022/12/8 12:30 PM
# @Author : 张安然
# @File : '009_遍历
# @Project : python_space


dog = {'name': 'tom', "sex": 1, 'ag8': 3}

# keys()
for key in dog.keys():
    print(key)

# values()
for value in dog.values():
    print(value)

# items()
for key, value in dog.items():
    print(key, value)

# item
for item in dog.items():
    print(item[0])
    print(item[1])

# key
# key name value tom
# key sex value 1
# key ag8 value 3
for key in dog:
    print("key", key, 'value', dog[key])
