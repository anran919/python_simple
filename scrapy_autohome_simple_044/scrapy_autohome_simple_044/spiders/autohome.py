import scrapy


class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['www.autohome.com.cn/car/0_0-0.0_0.0-0-0-0-0-0-6-0-0/']
    start_urls = ['http://www.autohome.com.cn/car/0_0-0.0_0.0-0-0-0-0-0-6-0-0//']

    def parse(self, response):
        # //ul[@class='rank-list-ul']//li/h4
        car_name_n_list = response.xpath("//ul[@class='rank-list-ul']//li/h4/a/text()")
        car_price_n_list = response.xpath("//ul[@class='rank-list-ul']/li/div/a[@class='red']/text()")
        # print('==========', car_name_n_list)
        for n_name in car_name_n_list:
            print(n_name.extract())
