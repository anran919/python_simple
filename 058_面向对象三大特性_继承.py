# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 2:44 PM
# @Author : 张安然
# @File : '057_面向对象三大特性
# @Project : python_space

class Phone:
    IMEI = None
    producer = None
    date = '2019年12月14日15:34:13'

    def call_by_4g(self):
        print('4G通话', self.producer)


# 单继承
class IPhoneX(Phone):
    face_id = None
    date = '2020年12月14日15:34:13'

    def call_by_5g(self):
        print('5G通话', self.face_id, self.producer)


x = IPhoneX()
x.producer = '厂商:富士康'
x.face_id = '面部识别: 结构光'
x.call_by_5g()
x.call_by_4g()


# 多继承
class NFC:
    nfc_type = '第五代'
    nfc_producer = '英伟达'
    date = '2021年12月14日15:34:13'

    def read_card(self):
        print('read_card', self.nfc_type, self.nfc_producer)

    def write_card(self):
        print('write_card', self.nfc_type, self.nfc_producer)


print('=============多继承=============')


class Remote:
    remote_type = '红外遥控'
    date = '2022年12月14日15:34:13'

    def control(self):
        print('遥控开启', self.remote_type)


class XiaoMi(Phone, NFC, Remote):
    # pass 如果类中没有其他属性和方法,使用pass补全
    msg = '谁他妈买小米'

    # 多个父类有相同的属性,会使用第一个定义的属性
    # 如果子类也定义了项目的属性,则使用子类定义的属性
    # 复写父类的属性
    # date = '2023年12月14日15:34:13'

    def sale(self):
        print('广播: ', self.msg)

    def call_by_5g(self):
        # 调用父类属性 方式一
        print('调用父类属性 方式一 Phone:', Phone.producer)
        print('调用父类属性 方式一 super:', super().producer)
        # 调用父类方法 方式一
        print('调用父类方法方式一 Phone call_by_4g:', Phone.call_by_4g(self))
        print('调用父类方法方式二 super call_by_4g:', super().call_by_4g())
        # 复写父类的方法
        print('使用最新5G通话', self.date)


mi = XiaoMi()
mi.call_by_4g()
mi.call_by_5g()
mi.control()
mi.read_card()
mi.write_card()
mi.sale()
print("date", mi.date)
