# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 10:00 PM
# @Author : 张安然
# @File : '__init__.py
# @Project : python_space
from typing import List

# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 9:29 PM
# @Author : 张安然
# @File : '065_MySql数据库综合应用
# @Project : python_space

from pymysql import Connection
from data_define import Record
from file_define import TextFileReader, JsonFileReader

if __name__ == '__main__':
    conn = Connection(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        charset='utf8'
    )
    print(conn.get_server_info())
    cursor = conn.cursor()
    conn.select_db('python_test')
    #
    # {"date": "2022-01-01", "order_id": "HN20220130", "money": "21566", "province": "湖南"}
    # {"date": "2022-01-05", "order_id": "HB20220130", "money": "41566", "province": "湖北"}
    cursor.execute(
        "create table if not exists sale_info(id int auto_increment primary key , `date` datetime ,order_id varchar(45) ,money decimal ,province varchar(25))")
    # 插入数据
    # cursor.execute(f"insert into sale_info(date, order_id, money, province) values ('2022-12-01', 'HN20221201', {21566}, '湖南');")

    tfr = TextFileReader("../json/063_销售数据分析2月.text")
    record_list_2: List[Record] = tfr.read_file()
    trj = JsonFileReader("../json/063_销售数据分析1月.json")
    record_list_1: List[Record] = trj.read_file()
    all_list: List[Record] = record_list_1 + record_list_2
    for v in all_list:
        print(v.province)
        query = f"insert into sale_info(date, order_id, money, province) values ('{v.date}', '{v.order_id}', {v.money}, '{v.province}');"
        print(query)
        cursor.execute(query)

    # 查询数据
    cursor.execute("select * from sale_info")
    print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()
