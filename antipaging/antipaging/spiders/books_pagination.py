import scrapy

'''
items scraped: 1000
elapsed time: 44.85
'''

class BooksPaginationSpider(scrapy.Spider):
    name = "books_pagination"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for s in response.xpath('//ol[@class]/li'):
            title = s.xpath('.//img/@alt').get()
            yield {
                'title': title
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page)) #.follow(next_page, callback=self.parse)
