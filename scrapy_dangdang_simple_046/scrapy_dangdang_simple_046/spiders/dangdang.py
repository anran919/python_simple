import scrapy

# from scrapy_dangdang_simple_046.items import ScrapyDangdangSimple046Item

from ..items import ScrapyDangdangSimple046Item


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    # allowed_domains = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1']
    # allowed_domains = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-2']
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1/']
    base_url = 'http://bang.dangdang.com/books/bestsellers'
    page = 1

    def parse(self, response):
        # name  //ul[@class='bang_list clearfix bang_list_mode']//li//div[@class='pic']/a/img/@alt
        # src:  //ul[@class='bang_list clearfix bang_list_mode']//li//div[@class='pic']/a/img/@src
        # price: //ul[@class='bang_list clearfix bang_list_mode']//li//div[@class='price']/p/span[@class='price_n']/text()
        li_path = "//ul[@class='bang_list clearfix bang_list_mode']//li"
        li_list = response.xpath(li_path)
        for li in li_list:
            name = li.xpath(".//div[@class='pic']/a/img/@alt").extract_first()
            src = li.xpath(".//div[@class='pic']/a/img/@src").extract_first()
            price = li.xpath(".//div[@class='price']/p/span[@class='price_n']/text()").extract_first()
            book = ScrapyDangdangSimple046Item(src=src, name=name, price=price)
            #           获取一个book 就交给pipeline,需要在settings 开启管道
            yield book
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + '/01.00.00.00.00.00-recent30-0-0-1-' + str(self.page) + ''
            #           调用parse方法
            #           scrapy.Request() 就是get请求
            #            callback是要执行的函数,不需要加()
            yield scrapy.Request(url=url, callback=self.parse)
