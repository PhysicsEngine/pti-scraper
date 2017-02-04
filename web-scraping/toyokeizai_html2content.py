#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
from bs4 import BeautifulSoup
from selenium import webdriver
from content import Content
import requests
import os
import pytz
from datetime import datetime

class ToyokeizaiHtml2Content(object):
  def parse(self, full_url, soup):
      return Content(
              "1",
              "\n".join(map(lambda x: x.get_text(), soup.find_all("p"))),
              full_url,
              self.parse_time(self.get_revision_date(soup).split("+")[0]),
              soup.title.string)

  def get_revision_date(self, soup):
    for tag in soup.find_all("meta"):
      if tag.get("name", None) == "cXenseParse:recs:publishtime":
        print tag.get("content", None)
        return tag.get("content", None)
    return "2017-02-04 11:22:33" # fuck

  def parse_time(self, tstr):
    try:
      # ex) "Fri Feb 03 10:56:58 UTC 2017"
      return datetime.strptime(tstr, "%a %b %d %H:%M:%S %Z %Y").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Tokyo'))
    except ValueError:
      # 2017-01-30T06:00:00+09:00
      # ex) "2017-02-03T10:56:58+0000"
      return datetime.strptime(tstr, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Tokyo'))
    raise ValueError

## test
if __name__ == '__main__':
  html2content = ToyokeizaiHtml2Content()
  print html2content.parse_time("2017-01-30T06:00:00")

  scraper = ScrapingLib()
  url = "http://toyokeizai.net/articles/-/155794?page=0"
  soup = scraper.get_sorp(url)
  print html2content.parse(url, soup)
