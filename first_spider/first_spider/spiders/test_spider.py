# -*- coding: utf-8

from scrapy.spider import Spider
import json
from first_spider.items import FirstSpiderItem
from selenium import webdriver


class MiSpider(Spider):
    name = 'yunbi'
    start_urls = ['https://yunbi.com//api/v2/trades.json?market=btccny']

    #解析信息
    def parse(self, response):
        item = FirstSpiderItem()
        browser = webdriver.Chrome()
        browser.get(self.start_urls[0])
        jsonresponse = json.loads(response.body_as_unicode())
        a = jsonresponse[:]
        for i in range(0,len(a)):
            item['strike_time'] = a[i]['created_at']
            item['price'] = a[i]['price']
            item['amount'] = a[i]['volume']
            yield item





