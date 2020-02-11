import scrapy

class PriceSpider(scrapy.Spider):
    name = "price"

    def start_requests(self):
        urls = [
            "https://tarkov-market.ru/en",
            "https://eft-loot.com"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.body)