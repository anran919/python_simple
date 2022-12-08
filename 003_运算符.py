# _*_ coding : utf-8 _*_
# @Time: 2022/12/7 11:28 PM
# @Author : 张安然
# @File : '003_运算符
# @Project : python_space

""" 计算
+ 加
- 减
* 乘
/ 除
// 取整数
% 取余数
** 指数
() 小括号,改变运算优先级
"""

""" 赋值运算符
a = b = c = 10
e, f, g = 11, 23, 44
"""

""" 复合运算符
+=
-=
*=
/=
//=
%=
**= 
"""

""" 比较运算符
==
!=
>
>= 
<
<=
"""

""" 逻辑运算符
and
or
not
"""

# ----------计算----------
price = 99.12
count = 10
print('+', price + count)
print('-', price - count)
print('*', price * count)
print('/', price / count)
print('//', price // count)
print('%', price % count)
print('**', price ** count)
print('()', (price + count) * 12)

# ----------赋值----------

a = b = c = 10
print(a, b, c)

e, f, g = 11, 23, 44
print(e, f, g)

# ----------复合运算符----------
print(a, b)
a += b
print(a, b)

# ----------逻辑运算符----------
a > 10 and print('a>10')
a < 10 and print('a>10')


