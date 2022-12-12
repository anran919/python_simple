import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyReadbookSimple048Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1175_1.html']

    rules = (
        # 使用正则
        # Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=False), # 爬取13页
        Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=True),  # 爬取所有页
    )

    def parse_item(self, response):
        image_list = response.xpath("//div[@class='book-info']//img")
        for img in image_list:
            name = img.xpath('./@alt').extract_first()
            src = img.xpath('./@data-original').extract_first()
            book = ScrapyReadbookSimple048Item(name=name, src=src)
            yield book
