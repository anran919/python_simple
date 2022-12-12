import scrapy
import json

class TranslateSpider(scrapy.Spider):

    name = 'translate'
    allowed_domains = ['dict.youdao.com']
    start_urls = ['http://https://dict.youdao.com/keyword/key/']

    # post请求示例
    # 没有参数则start_urls,和parse()方法将没有意义
    # 使用start_requests 方法
    # def parse(self, response):
    #     pass

    # sh
    def start_requests(self):
        url = 'https://dict.youdao.com/keyword/key'
        data = {
            'text': '在线翻译',
            'lang': 'zh',
            'to': 'en'
        }
        # 发送请求
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_post_response)

    def parse_post_response(self,response):
        content = response.text
        content = json.loads(content,'utf-8')
        print('---content ---',content)