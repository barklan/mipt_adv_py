import scrapy
from ..items import MiptstreamItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['http://miptstream.ru/']
    start_urls = ['http://miptstream.ru/']

    def parse(self, response):
        allarticles = response.css('article.post')

        for article in allarticles:
            title = article.css('a.loop-entry-img-link::attr(title)').get()
            link = article.css('a.loop-entry-img-link::attr(href)').get()

            items = MiptstreamItem()
            items['title'] = title
            items['link'] = link

            yield items