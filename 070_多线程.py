# _*_ coding : utf-8 _*_
# @Time: 2022/12/15 2:08 PM
# @Author : 张安然
# @File : '070_多线程
# @Project : python_space

import time

import threading


def sing(msg):
    while True:
        # print('唱歌...啦啦啦')
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        # print("跳舞了,💃🏻💃🏻💃🏻💃🏻💃🏻")
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 传参和启动线程
    dance_thread = threading.Thread(target=dance, args=("跳舞了,💃🏻💃🏻💃🏻💃🏻💃🏻",), name='dance')
    sing_thread = threading.Thread(target=sing, kwargs ={'msg': '啦啦啦啦,🎤🎤🎤🎤'}, name='sing')
    sing_thread.start()
    dance_thread.start()
