# _*_ coding : utf-8 _*_
# @Time: 2022/12/14 5:58 PM
# @Author : 张安然
# @File : 'file_define
# @Project : python_space
"""文件读取方法"""
import json
from typing import List

from data_define import Record


class FileReader:
    def __init__(self, path):
        self.path = path

    def read_file(self) -> List[Record]:
        """将数据转换为Record对象"""
        pass


class TextFileReader(FileReader):

    def read_file(self) -> List[Record]:
        __record_list: List[Record] = []
        with open(self.path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                line = line.strip().split(',')
                record = Record(line[0], line[1], int(line[2]), line[3])
                __record_list.append(record)

        return __record_list


class JsonFileReader(FileReader):

    def read_file(self) -> List[Record]:
        __record_list: List[Record] = []
        with open(self.path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                line = json.loads(line)
                record = Record(line['date'], line['order_id'], int(line['money']), line['province'])
                __record_list.append(record)

        return __record_list


if __name__ == '__main__':
    tfr = TextFileReader("../json/063_销售数据分析2月.text")
    record_list_f = tfr.read_file()
    trj = JsonFileReader("../json/063_销售数据分析1月.json")
    record_list_j = trj.read_file()
