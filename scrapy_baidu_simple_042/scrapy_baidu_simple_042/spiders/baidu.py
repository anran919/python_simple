import scrapy


class BaiduSpider(scrapy.Spider):
    #  爬虫的名字 ,用于运行爬虫的时候使用的值
    name = 'baidu'
    # 起始的地址,指第一次要访问的域名
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("response : ", response)
        pass
