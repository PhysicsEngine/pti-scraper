#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os

class ReutersHtml2Content(object):
    def parse(self, soup):
        return "\n".join(map(lambda x: x.text, soup.find_all("p")))

## test
if __name__ == '__main__':
    scraper = ScrapingLib()
    html2content = ReuterHtml2Content()
    soup = scraper.get_sorp("http://jp.reuters.com/article/idJP2017020301002019?sp=true");
    print html2content.parse(soup)

