#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reuters_the_wire_scraper import ReutersTheWireScraper
from reuters_html2content import ReutersHtml2Content
from scraping_lib import ScrapingLib
from writer import Writer

# Usage:
# $ PTI_HOST=153.126.154.182 PTI_USER=pti PTI_PASSWORD=gussan_gologo13 PTI_DB=pti python2 app.py
if __name__ == '__main__':
  scraper = ReutersJpColummsScraper(ReutersJpColummsScraper.LOG_PATH)
  html2content = ReutersHtml2Content()
  writer = Writer()
  page = 1
  while True:
    sorp = scraper.get_sorp(page)
    content = html2content.parse(full_url, soup)
    writer.write(content)

