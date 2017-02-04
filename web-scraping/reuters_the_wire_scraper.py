#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib

class ReutersTheWireScraper(object):
  LIST_URL = "http://jp.reuters.com/theWire"
  ARTICLE_URL = "http://jp.reuters.com/article/{0}?sp=true"
  LOG_PATH = "/tmp/ReutersTheWireScraper.log"
  
  def __init__(self, log_path):
      self.scraping = ScrapingLib(log_path)
  
  @classmethod
  def get_target_url(cls, article_url):
      return cls.BASE_URL.format(article_url)
  
  def get_list_url(self, type):
    return self.scraping.get_sorp(self.LIST_URL, type)
  
## test
if __name__ == '__main__':
  scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
  print scraper.get_list_url("")
