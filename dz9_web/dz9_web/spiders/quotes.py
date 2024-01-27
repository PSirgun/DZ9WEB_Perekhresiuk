import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'quotes.json'
    }
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath("span[@class='text']/text()").get(),
                'author': quote.xpath("span/small[@class='author']/text()").get(),
                'tags': quote.xpath("div[@class='tags']/a[@class='tag']/text()").getall()
            }
