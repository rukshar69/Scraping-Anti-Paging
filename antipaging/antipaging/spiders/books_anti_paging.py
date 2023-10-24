from typing import Iterable
import scrapy
from scrapy.http import Request

'''
items scraped: 1000
elapsed time: 4.61
'''

class BooksAntiPagingSpider(scrapy.Spider):
    name = "books_anti_paging"
    allowed_domains = ["books.toscrape.com"]
    #start_urls = ["https://x.com"]
    url = 'http://books.toscrape.com/catalogue/page-{}.html'

    def start_requests(self):
        for i in range(1, 51):
            yield scrapy.Request(self.url.format(i))
    def parse(self, response):
        for s in response.xpath('//ol[@class]/li'):
            title = s.xpath('.//img/@alt').get()
            yield {
                'title': title
            }
