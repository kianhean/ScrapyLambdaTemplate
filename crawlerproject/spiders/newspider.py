import scrapy


class NewSpider(scrapy.Spider):
    name = 'newspider'
    start_urls = ['example.com']

    def parse(self, response):

        yield {
            'url': response.request.url
        }
