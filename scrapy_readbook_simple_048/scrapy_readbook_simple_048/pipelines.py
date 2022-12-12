# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class ScrapyReadbookSimple048Pipeline:
    def open_spider(self, spider):
        self.fp = open('dushu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


# 加载settings文件
from scrapy.utils.project import get_project_settings
class MySqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.db_name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    def connect(self):
        print('connect')
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset=self.charset)
        self.cursor = self.conn.cursor()
        self.count =1

    def process_item(self, item, spider):
        sql = "insert into books (name,src) values ('{}','{}')".format(item['name'], item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        self.count =self.count+1
        print('------',self.count)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
