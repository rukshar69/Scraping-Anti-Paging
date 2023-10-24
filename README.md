# Scraping-Anti-Paging
Avoiding pagination while using Scrapy to save time

# Why Pagination in Scraping is a Bad Idea

We have a basic spider to scrape book titles named [books_pagination](https://github.com/rukshar69/Scraping-Anti-Paging/blob/main/antipaging/antipaging/spiders/books_pagination.py). Here, we are using the basic pagination code to traverse the next pages. The code is as follows:

```python 
next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
```

Such code does not effectively utilize Scrapy's concurrency. As such the scraping time increases. For this spider, to scrape 1000 books from 50 pages, it will take about 45 seconds.

# Anti-Paging Technique

It's advisable to avoid such pagination mehtod whenever possible. For this case, it is possible. Here, we observe a pattern of urls that the website uses to go from one page to another. The pattern is: **http://books.toscrape.com/catalogue/page-<page_number>.html**. The range of page number is 1 to 50. A loop is then used to generate the urls for all the pages and using **yield scrapy.Request**, the urls are sent to the spider.

The modified spider is [books_anti_paging](https://github.com/rukshar69/Scraping-Anti-Paging/blob/main/antipaging/antipaging/spiders/books_anti_paging.py)

For this spider, to scrape 1000 books from 50 pages, it will take about 5 seconds. This spider is **9 times** faster than the previous one that uses tradional pagination technique.

