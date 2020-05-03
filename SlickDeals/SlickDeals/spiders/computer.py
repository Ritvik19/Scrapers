# -*- coding: utf-8 -*-
import scrapy


class ComputerSpider(scrapy.Spider):
    name = 'computer'
    allowed_domains = ['slickdeals.net']
    start_urls = ['https://slickdeals.net/computer-deals/']

    def remove_characters(self, value):
        return value.strip('\xa0')

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a//text()").get(),
                'link': product.xpath(".//a//@href").get(),
                'store_name': self.remove_characters(product.xpath("normalize-space(.//span[@class='itemStore']/text())").get()),
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)