#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
import re

class ReutersTheWireScraper(object):
  LIST_URL = "http://jp.reuters.com/theWire"
  ARTICLE = "article"
  RE_ARTICLE = re.compile(ARTICLE)
  LOG_PATH = "/tmp/ReutersTheWireScraper.log"
  ARTICLE_PARAM = "?sp=true"
  DOMAIN = "http://jp.reuters.com"
  
  def __init__(self, log_path):
      self.scraping = ScrapingLib(log_path)
      self.scraping.get(self.LIST_URL)
      
  def get_sorp(self):
    return self.scraping.get_latest_sorp()
  
  def get_url_list(self):
    href_list = self.get_sorp().find_all("a", href=self.RE_ARTICLE)
    url_list = map(lambda x: x.get("href"), href_list)
    if(len(url_list) > 20):
      del url_list[0:19]
    return url_list

  def load_more_content(self):
    self.scraping.clickByClassName("more-load")

  @classmethod
  def get_full_url(cls, article_path):
    return cls.DOMAIN + article_path

## test
if __name__ == '__main__':
  scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
  scraper.load_more_content()
  scraper.load_more_content()
  print scraper.get_url_list()
  print len(scraper.get_url_list())
