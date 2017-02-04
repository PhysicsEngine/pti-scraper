#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os

class ToyokeizaiHtml2Content(object):
  def parse(self, soup):
    return map(lambda x: x.get_text(), soup.find_all("p"))

## test
if __name__ == '__main__':
  scraper = ScrapingLib()
  html2content = ToyokeizaiHtml2Content()
  soup = scraper.get_sorp("http://toyokeizai.net/articles/-/155794?page=0")

  for p in  html2content.parse(soup):
    print p
