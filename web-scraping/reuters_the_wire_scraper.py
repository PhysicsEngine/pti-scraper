#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
import re

class ReutersTheWireScraper(object):
  LIST_URL = "http://jp.reuters.com/theWire"
  ARTICLE = "article"
  ARTICLE_URL = "http://jp.reuters.com/article/"
  RE_ARTICLE = re.compile(ARTICLE)
  LOG_PATH = "/tmp/ReutersTheWireScraper.log"
  ARTICLE_PARAM = "?sp=true"
  
  def __init__(self, log_path):
      self.scraping = ScrapingLib(log_path)
  
  @classmethod
  def get_target_url(cls, article_url):
      return cls.BASE_URL.format(article_url)
  
  def get_url_list(self):
    href_list = self.scraping.get_sorp(self.LIST_URL, ScrapingLib.TYPE_DRIVER).find_all("a", href=self.RE_ARTICLE)
    return map(lambda x: x.get("href"), href_list)
  
## test
if __name__ == '__main__':
  scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
  print scraper.get_url_list()
