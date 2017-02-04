#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
import re

class ReutersJpColummsScraper(object):
  BASE_URL = "http://jp.reuters.com/news/archive/jp_column?view=page&page={0}"
  LOG_PATH = "/tmp/ReutersJpColummsScraper.log"
  ARTICLE = "article"
  RE_ARTICLE = re.compile(ARTICLE)
  DOMAIN = "http://jp.reuters.com"

  def __init__(self, log_path):
    self.scraping = ScrapingLib(log_path)
    self.page = 1

  def get_target_url(self):
    url = self.BASE_URL.format(self.page)
    #print url
    return url

  def get_soup(self, url):
    return self.scraping.get_sorp(url, ScrapingLib.TYPE_REQUESTS)

  def get_url_list(self):
    href_list = self.get_soup(self.get_target_url()).find_all("a", href=self.RE_ARTICLE)
    return map(lambda x: x.get("href"), href_list)

  def load_more_content(self):
    self.page += 1

  @classmethod
  def get_full_url(cls, article_path):
    return cls.DOMAIN + article_path



## test
if __name__ == '__main__':
  scraper = ReutersJpColummsScraper(ReutersJpColummsScraper.LOG_PATH)
  #print scraper.get_url_list()
