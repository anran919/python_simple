# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 8:34 PM
# @Author : 张安然
# @File : '064_MySQL_连接MySql
# @Project : python_space

from pymysql import Connection

conn = Connection(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    # 自动提交事务
    # autocommit=True
)
print(conn.get_server_info())

# 操作数据库
# 获取游标对象
cursor = conn.cursor()
conn.select_db('python_test')
# 创建表
cursor.execute('create table if not exists  test_01(id int auto_increment primary key ,name varchar(45),age int,info varchar(255));')
# 插入数据
cursor.execute("insert into test_01(name, age, info) values ('尴尬的铁根',69,'69岁扶墙对抗,金牌大厨')")
# 查询数据
cursor.execute('select * from test_01')

# 提交事务
conn.commit()
print(cursor.fetchall())
# 关闭cursor
cursor.close()
# 关闭数据库连接
conn.close()
