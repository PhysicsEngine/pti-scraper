#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os

class ReuterHtml2Content(object):
    def parse(self, soup):
        return map(lambda x: x.text, soup.find_all("p"))

## test
if __name__ == '__main__':
    scraper = ScrapingLib()
    html2content = ReuterHtml2Content()
    soup = scraper.get_sorp("http://jp.reuters.com/article/idJP2017020301002019?il=0");
    for a in html2content.parse(soup):
        print a

