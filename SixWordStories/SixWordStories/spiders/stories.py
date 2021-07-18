# -*- coding: utf-8 -*-
import scrapy


class StoriesSpider(scrapy.Spider):
    name = "stories"
    allowed_domains = ["www.sixwordstories.net"]
    start_urls = ["http://www.sixwordstories.net/"]

    def parse(self, response):
        for div in response.css("div.post h2"):
            yield {"story": " ".join(div.css(" ::text").getall())}

        prev_url = response.css(".prev a::attr(href)").get()
        if prev_url is not None:
            yield response.follow(url=prev_url, callback=self.parse)
