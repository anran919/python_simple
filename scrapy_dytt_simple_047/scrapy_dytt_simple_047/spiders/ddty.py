import scrapy
from ..items import ScrapyDyttSimple047Item


class DdtySpider(scrapy.Spider):
    name = 'ddty'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/oumei/list_7_1.html']

    def parse(self, response):
        a_list = response.xpath('//ul//table//td[2]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            details_url = 'https://www.ygdy8.net/' + href
            print('--------', name, details_url)
            yield scrapy.Request(url=details_url, callback=self.parse_details, meta={'name': name})

    def parse_details(self, response):
        cover = response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        print('d_url:', cover)
        name = response.meta['name']
        movie = ScrapyDyttSimple047Item(name=name, cover=cover)
        yield  movie
