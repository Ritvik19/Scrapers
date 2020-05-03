# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class LiveCoinSpider(scrapy.Spider):
    name = 'livecoin'

    allowed_domains = ['www.livecoin.net/en']
    
    start_urls = [
        'https://www.livecoin.net/en'
    ]
    
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.livecoin.net/en")
        
        usd_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        usd_tab[4].click() 
        
        self.html = driver.page_source
        
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }
        
