import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://quanguo.58.com/']
    start_urls = ['https://quanguo.58.com/']

    def parse(self, response):
        # response.text 返回字符出纳
        # response.body 返回二进制
        type_list = response.xpath('//div[*]/div[*]/div[*]/div/div[*]/div[*]/a')
        # 提取selector对象的data属性值
        print('提取selector对象的data属性值:', type_list[0].extract())
        # 提取selector列表的第一个值
        print('提取selector列表的第一个值:', type_list[0].extract_first())

