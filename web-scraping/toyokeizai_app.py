#!/usr/bin/env python
# -*- coding: utf-8 -*-
from toyokeizai_html2content import ToyokeizaiHtml2Content
from toyokeizai_marketwatcher import ToyokeizaiMarketWatcher
from scraping_lib import ScrapingLib
from writer import Writer
from db_connect import DbConnect
import sys

# Usage:
# $ PTI_HOST=153.126.154.182 PTI_USER=pti PTI_PASSWORD=gussan_gologo13 PTI_DB=pti python2 app.py
if __name__ == '__main__':
    conn = DbConnect()
    scraper = ToyokeizaiMarketWatcher(ToyokeizaiMarketWatcher.LOG_PATH)
    lib = ScrapingLib()
    html2content = ToyokeizaiHtml2Content(conn.get())
    writer = Writer(conn.get())

    page = 1
    while True:
        for url in scraper.get_url_list(page):
            full_url = ToyokeizaiMarketWatcher.get_full_url(url)
            soup = lib.get_sorp(full_url)
            content = html2content.parse(full_url, soup)
            #writer.replace_author(content)
            writer.write_articles_file(content)
        ++page
