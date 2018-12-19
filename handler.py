import scrapy
from scrapy.crawler import CrawlerProcess

from crawlerproject.spiders.newspider import NewSpider


def run(event, context):

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    })

    process.crawl(NewSpider, domain='example.com')
    process.start()

if __name__ == "__main__":
    run('', '')