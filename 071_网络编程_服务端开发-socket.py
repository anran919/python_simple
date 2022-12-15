# _*_ coding : utf-8 _*_
# @Time: 2022/12/15 2:30 PM
# @Author : 张安然
# @File : '071_网络编程_服务端开发-socket
# @Project : python_space

# 导入socket
import socket

# 创建socket对象
service = socket.socket()
# 绑定ip和端口
service.bind(('127.0.0.1', 8845))
# 监听端口
service.listen(1)
# 等待客户端连接
conn, address = service.accept()
print(f'接收到了客户端的连接,客户端的信息是address: {address}')
try:
    while True:
        # 接收客户端信息
        data: str = conn.recv(1024).decode('utf-8')
        print(f'客户端:{data}')
        # 发送回复信息
        msg = input('请输入你要和客户端回复的消息:')
        if msg == 'exit':
            break
        msg = msg.encode('utf-8')
        conn.send(msg)
except Exception as e:
    print(e)
finally:
    # 关闭连接
    conn.close()
    service.close()

