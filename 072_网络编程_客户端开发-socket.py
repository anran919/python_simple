# _*_ coding : utf-8 _*_
# @Time: 2022/12/15 2:30 PM
# @Author : 张安然
# @File : 072_网络编程_客户端开发-socket
# @Project : python_space

# 导入socket
import socket

# 创建socket对象
client = socket.socket()
# 连接到服务端
client.connect(('127.0.0.1', 8845))

try:
    while True:
        # 发送消息
        msg = input('请输入要发送的内容 : ')
        if msg == 'exit':
            break
        client.send(f'{msg}'.encode('utf-8'))

        # 返回机收到的消息
        data = client.recv(1024)
        print(f"服务端: {data.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    # 关闭连接
    client.close()
