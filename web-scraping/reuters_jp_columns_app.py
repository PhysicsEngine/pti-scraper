#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reuters_jp_columns_scraper import ReutersJpColummsScraper
from reuters_html2content import ReutersHtml2Content
from scraping_lib import ScrapingLib
from writer import Writer
from db_connect import DbConnect

# Usage:
# $ PTI_HOST=153.126.154.182 PTI_USER=pti PTI_PASSWORD=gussan_gologo13 PTI_DB=pti python2 app.py
if __name__ == '__main__':
  conn = DbConnect()
  scraper = ReutersJpColummsScraper(ReutersJpColummsScraper.LOG_PATH)
  html2content = ReutersHtml2Content(conn.get())
  writer = Writer(conn.get())
  page = 1
  while True:
    for url in scraper.get_url_list():
      full_url = ReutersJpColummsScraper.get_full_url(url)
      soup = scraper.get_soup(full_url)
      content = html2content.parse(full_url, soup)
      if content:
          writer.write_articles_file(content)
      else:
          print("content registration error")
    scraper.load_more_content() 
