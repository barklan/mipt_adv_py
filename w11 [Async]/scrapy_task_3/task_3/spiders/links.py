import scrapy
from ..items import Task3Item


class LinksSpider(scrapy.Spider):
    name = "links"

    def read_from(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    # def start_requests(self):
    #     urls = self.read_from('urls.txt')

    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = read_from('urls.txt')

    def parse(self, response):
        alllinks = response.css('a')

        for link in alllinks:
            text = link.css('::text').get()
            href = link.css('::attr(href)').get()
            
            items = Task3Item()
            items['text'] = text
            items['href'] = href

            yield items