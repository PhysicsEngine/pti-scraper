#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
import re
class ToyokeizaiMarketWatcher(object):
  BASE_URL = "http://toyokeizai.net/category/marketwatcher?page={0}&per_page=100"
  LOG_PATH = "/tmp/ToyokeizaiMarketWatcher.log"
  ARTICLE = "articles/-/"
  RE_ARTICLE = re.compile(ARTICLE)
  DOMEIN = "http://toyokeizai.net{0}?page=0"

  def __init__(self, log_path):
    self.scraping = ScrapingLib(log_path)

  @classmethod
  def get_target_url(cls, page):
    return cls.BASE_URL.format(page)

  @classmethod
  def get_full_url(cls, article_path):
    return cls.DOMEIN.format(article_path)

  def get_sorp(self, page):
    url = self.get_target_url(page)
    return self.scraping.get_sorp(url, ScrapingLib.TYPE_REQUESTS)

  def get_url_list(self, page):
    href_list = self.get_sorp(page).find_all("a", href=self.RE_ARTICLE)
    return map(lambda x: x.get("href"), href_list)


## test
if __name__ == '__main__':
  scraper = ToyokeizaiMarketWatcher(ToyokeizaiMarketWatcher.LOG_PATH)
  for article_path in  scraper.get_url_list(1):
    print ToyokeizaiMarketWatcher.get_full_url(article_path)
