### 使用CrawlSpider

```puthon
    scrapy startproject scrapy_readbook_simple_048
    cd scrapy_readbook_simple_048/scrapy_readbook_simple_048/spider
    scrapy genspider -t crawl read https://www.dushu.com/book/1175_2.html 
    # 使用正则
    Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=False),
    # 创建数据库,表,字段
    # 安装pymysql
    # 在pipeline中操作数据库,连接,打开,插入,关闭
```

### 指定日志级别和日志文件
```python
# 指定日志级别,以下二选一
LOG_LEVEL ='WARNING'
LOG_FILE ='执行日志.log'
```
