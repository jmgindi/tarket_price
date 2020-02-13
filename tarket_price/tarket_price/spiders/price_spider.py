import os
import scrapy
import selenium

from time import sleep

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class PriceSpider(scrapy.Spider):
    name = "price"
    start_urls = [
        "https://eft-loot.com",
        "https://tarkov-market.ru/en",
        ]

    def parse(self, response):
        # set header
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.6 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            }

        # options setup
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-web-security")
        options.add_argument("--no-sandbox")
        caps = options.to_capabilities()

        # setup driver        
        self.driver = webdriver.Chrome(os.environ.get("CHROME_DRIVER"))

        for _url in start_urls:
            self.driver.get(self.start_urls[_url])
            
            prev_bottom = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(7)
                cur_bottom = self.driver.execute_script("return document.body.scrollHeight")
                if cur_bottom == prev_bottom:
                    break
                prev_bottom = cur_bottom
                sleep(1.2)
            
            text = self.driver.page_source
            print(text)
#            scrapy_selector = Selector(text=self.driver.page_source)
