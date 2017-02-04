#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
import re
class ReutersJpColummsScraper(object):
  BASE_URL = "http://jp.reuters.com/news/archive/jp_column?view=page&page={0}"
  LOG_PATH = "/tmp/ReutersJpColummsScraper.log"
  ARTICLE = "article"
  RE_ARTICLE = re.compile(ARTICLE)


  def __init__(self, log_path):
    self.scraping = ScrapingLib(log_path)

  @classmethod
  def get_target_url(cls, page):
    url = cls.BASE_URL.format(page)
    print url
    return url

  def get_sorp(self, page):
    url = self.get_target_url(page)
    return self.scraping.get_sorp(url, ScrapingLib.TYPE_REQUESTS)

  def get_url_list(self, page):
    href_list = self.get_sorp(page).find_all("a", href=self.RE_ARTICLE)
    return map(lambda x: x.get("href"), href_list)


## test
if __name__ == '__main__':
  scraper = ReutersJpColummsScraper(ReutersJpColummsScraper.LOG_PATH)
  print scraper.get_url_list(2)
