import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['yahoo.com']
    start_urls = ['http://yahoo.com/']

    def parse(self, response):
        pass
