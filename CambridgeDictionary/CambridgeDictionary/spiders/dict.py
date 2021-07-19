# -*- coding: utf-8 -*-
import scrapy


class DictSpider(scrapy.Spider):
    name = "dict"
    allowed_domains = ["dictionary.cambridge.org"]

    def __init__(self, query="", **kwargs):
        self.start_urls = [f"https://dictionary.cambridge.org/dictionary/english/{query}/"]
        super().__init__(**kwargs)

    def parse(self, response):
        word = response.css("span.hw.dhw::text").get()
        pos = [" ".join(pos.css(" ::text").getall()) for pos in response.css("div.pos-header")[0].css("span.pos.dpos")]
        div = response.css("div.entry-body__el")[0]
        meanings = [
            {
                "meaning": " ".join(meaning.css(" ::text").getall()).strip(),
                "example": " ".join(example.css(" ::text").getall()).strip(),
            }
            for meaning, example in zip(div.css("div.def.ddef_d.db"), div.css("div.def-body.ddef_b"))
        ]
        yield {"word": word, "pos": pos, "meanings": meanings}
