# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdangSimple046Pipeline:
    # 爬虫开始前执行
    def open_spider(self, spider):
        print('+++++++++++')
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 方式一,多次操作文件.不推荐
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item)  )
        # 方式二 open_spider 打开文件,close_spider 关闭文件
        self.fp.write(str(item))
        return item

    # 爬虫结束后执行
    def close_spider(self, spider):
        print('-----------')
        self.fp.close()



import urllib.request

# 开启多条管道,两步
# 1. 自定义类
# 2. 需要在settings中开启管道
class MyDangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = item.get('src')
        print('----url-----',url)
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
