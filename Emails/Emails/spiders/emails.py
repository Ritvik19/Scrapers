# -*- coding: utf-8 -*-
import scrapy, re, bs4
from fuzzywuzzy import fuzz
from urllib.parse import urlparse

EMAIL = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
CSS = re.compile(r'<style(.|\n)*?>(.|\n)*?</style>')
JS = re.compile(r'<script(.|\n)*?>(.|\n)*?</script>')
HTML = re.compile(r'<(.|\n)*?>')
striptext = lambda x: re.sub(r"\s+", ' ', x).strip()


class EmailsSpider(scrapy.Spider):
    name = 'emails'
    
    def __init__(self, start_url, thresh=0, restrict_domain=True, **kwargs):
        self.start_urls = [start_url]
        if bool(restrict_domain):
            self.allowed_domains = [urlparse(start_url).netloc]
        
        self.crawled = []
        self.thresh = float(thresh)
        
        super().__init__(**kwargs)

    def parse(self, response):
        self.crawled.append(response.request.url)
        contents  = response.text
        contents = CSS.sub('\n', contents)
        contents = JS.sub('\n', contents)
        contents = HTML.sub('\n', contents)
        contents = re.sub(r"\s+", ' ', contents)
        
        for email in EMAIL.findall(contents):
            yield {'email': email}
        
        ressoup = bs4.BeautifulSoup(response.text, 'lxml')
        for anchor in ressoup.find_all("a"):
            _ = anchor.getText()
            if "href" in anchor.attrs:
                link = anchor.attrs["href"]
            else:
                link = ''

            if fuzz.token_set_ratio(_, 'about us') > self.thresh or fuzz.token_set_ratio(_, 'contact us') > self.thresh:
                if link not in self.crawled:
                    yield response.follow(url=link, callback=self.parse)
