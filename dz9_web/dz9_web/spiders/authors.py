import scrapy
import json
import os

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'authors.json'
    }
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

 
    def parse(self, response):

        for quote in response.xpath("//div[@class='quote']"):
            author_name = quote.xpath("span/small[@class='author']/text()").get()
            next_link = quote.xpath("span/a/@href").get()
            author_link = response.urljoin(next_link)
            yield scrapy.Request(author_link, callback=self.parse_author, meta={'author_name': author_name})

    def parse_author(self, response):
        author_name = response.meta['author_name']
        born_date = response.xpath("//span[@class='author-born-date']/text()").get()
        born_location = response.xpath("//span[@class='author-born-location']/text()").get()
        author_description = response.xpath("//div[@class = 'author-description']/text()").get()
        yield {
            'fullname': author_name,
            'born_date': born_date,
            'born_location': born_location,
            'description': author_description.strip()
            }

