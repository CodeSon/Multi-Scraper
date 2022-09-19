import scrapy


class GhanawebSpider(scrapy.Spider):
    name = 'ghanaweb'
    allowed_domains = ['ghanaweb.com']
    start_urls = ['http://ghanaweb.com/']

    def parse(self, response):
        pass
