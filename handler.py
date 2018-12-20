import scrapy
from scrapy.crawler import CrawlerProcess

from crawlerproject.spiders.newspider import Newspider


def run(event, context):

    spider = event['spider']
    spider_class_name = spider.title()
    scrapy_class = globals()[spider_class_name]

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    })

    process.crawl(scrapy_class, domain='example.com')
    process.start()

if __name__ == "__main__":
    event = {
        'spider': 'newspider'
    }
    run(event, '')